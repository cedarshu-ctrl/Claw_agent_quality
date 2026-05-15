#!/usr/bin/env python3
"""
Carousel Slide Generator — Education Niche
Uses Gemini API (gemini-2.0-flash-exp-image-generation) to generate 6 carousel slides.
Slide 1: text-only prompt → generates visual DNA
Slides 2-6: use slide-1 as reference image (image-to-image) for visual consistency

Output: 6 JPG files (768x1376, 9:16 vertical) in the specified output directory.
"""

import os
import sys
import json
import time
import base64
import requests
from pathlib import Path
from PIL import Image

# ── Config ──────────────────────────────────────────────────
API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = "gemini-2.0-flash-exp-image-generation"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

OUTPUT_DIR = Path(os.environ.get("CAROUSEL_OUTPUT_DIR", "/tmp/carousel"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS_FILE = Path(os.environ.get("SLIDE_PROMPTS_FILE", "slide-prompts.json"))

# ── Helpers ─────────────────────────────────────────────────

def load_prompts():
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["slides"]


def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def generate_slide_text_only(prompt_text: str, slide_num: int) -> str:
    """Generate slide 1 with text-only prompt (establishes visual DNA)."""
    print(f"[Slide {slide_num}] Generating with text-only prompt...")

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_text + "\n\nIMPORTANT: Generate this as a photorealistic or high-quality digital art poster image. Do NOT return text description of the image — return the actual image."}
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "temperature": 1.0,
        }
    }

    resp = requests.post(API_URL, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    # Extract image from response
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if "inlineData" in part:
                img_b64 = part["inlineData"]["data"]
                mime = part["inlineData"].get("mimeType", "image/png")
                out_path = str(OUTPUT_DIR / f"slide-{slide_num}.jpg")
                _save_image(img_b64, mime, out_path)
                print(f"[Slide {slide_num}] Saved → {out_path}")
                return out_path

    print(f"[Slide {slide_num}] WARNING: No image returned, text only response.")
    print(json.dumps(data, indent=2, ensure_ascii=False)[:1000])
    return ""


def generate_slide_img2img(prompt_text: str, slide_num: int, ref_image_path: str) -> str:
    """Generate slides 2-6 using slide-1 as visual reference."""
    print(f"[Slide {slide_num}] Generating with image reference...")

    ref_b64 = encode_image_to_base64(ref_image_path)

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inlineData": {
                            "mimeType": "image/jpeg",
                            "data": ref_b64
                        }
                    },
                    {"text": prompt_text + f"\n\nIMPORTANT: Match the visual style, color scheme, and typography style of the reference image. Generate this as a high-quality digital art poster image. Do NOT return text description — return the actual image."}
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "temperature": 0.8,
        }
    }

    resp = requests.post(API_URL, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if "inlineData" in part:
                img_b64 = part["inlineData"]["data"]
                mime = part["inlineData"].get("mimeType", "image/png")
                out_path = str(OUTPUT_DIR / f"slide-{slide_num}.jpg")
                _save_image(img_b64, mime, out_path)
                print(f"[Slide {slide_num}] Saved → {out_path}")
                return out_path

    print(f"[Slide {slide_num}] WARNING: No image returned.")
    print(json.dumps(data, indent=2, ensure_ascii=False)[:1000])
    return ""


def _save_image(img_b64: str, mime: str, out_path: str):
    """Decode base64 image and save as JPG at 768x1376."""
    img_bytes = base64.b64decode(img_b64)
    from io import BytesIO
    img = Image.open(BytesIO(img_bytes))
    # Resize to exact carousel dimensions
    img = img.resize((768, 1376), Image.LANCZOS)
    # Convert to RGB for JPEG
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(out_path, "JPEG", quality=92)
    print(f"  → Resized to 768x1376, saved as JPG")


def validate_slide(image_path: str, slide_num: int) -> bool:
    """Basic visual validation: correct size, JPG format."""
    try:
        img = Image.open(image_path)
        w, h = img.size
        if w != 768 or h != 1376:
            print(f"[Slide {slide_num}] FAIL: size {w}x{h}, expected 768x1376")
            return False
        print(f"[Slide {slide_num}] PASS: {w}x{h} JPG ✓")
        return True
    except Exception as e:
        print(f"[Slide {slide_num}] FAIL: {e}")
        return False


# ── Main ────────────────────────────────────────────────────

def main():
    if not API_KEY:
        print("ERROR: GEMINI_API_KEY not set!")
        sys.exit(1)

    if API_KEY.startswith("sk-ant-"):
        print("ERROR: GEMINI_API_KEY appears to be an Anthropic key (starts with sk-ant-).")
        print("       Gemini API keys start with 'AIzaSy...'")
        print("       Get one at: https://aistudio.google.com/app/apikey")
        sys.exit(1)

    slides = load_prompts()
    print(f"Loaded {len(slides)} slide prompts\n")

    results = []
    ref_image = None

    for slide in slides:
        num = slide["slide"]
        prompt = slide["prompt"]

        if num == 1:
            out = generate_slide_text_only(prompt, num)
            if out:
                ref_image = out
        else:
            if not ref_image:
                print(f"[Slide {num}] SKIP: no reference image from slide 1")
                continue
            out = generate_slide_img2img(prompt, num, ref_image)

        if out:
            valid = validate_slide(out, num)
            if not valid:
                print(f"[Slide {num}] Will retry...")
                # Retry once
                if num == 1:
                    out = generate_slide_text_only(prompt, num)
                else:
                    out = generate_slide_img2img(prompt, num, ref_image)
                if out:
                    validate_slide(out, num)
            results.append({"slide": num, "path": out, "valid": valid})

        # Rate limit: pause between requests
        time.sleep(3)

    # Summary
    print("\n" + "=" * 50)
    print("GENERATION SUMMARY")
    print("=" * 50)
    for r in results:
        status = "✓" if r["valid"] else "✗"
        print(f"  Slide {r['slide']}: {status} → {r['path']}")

    # Save manifest
    manifest_path = OUTPUT_DIR / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nManifest saved → {manifest_path}")


if __name__ == "__main__":
    main()

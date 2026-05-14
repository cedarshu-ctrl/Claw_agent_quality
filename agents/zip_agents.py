"""
Pack each workspace-xxx folder into a ZIP file under Agent_zip/.
ZIP contents are flat (no outer workspace-xxx/ wrapper).
Empty directories are preserved via a ZipInfo entry.
"""
import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = BASE_DIR
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "Agent_zip")


def zip_workspace(folder_name):
    src = os.path.join(AGENTS_DIR, folder_name)
    dst = os.path.join(OUTPUT_DIR, folder_name + ".zip")

    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zf:
        for dirpath, dirnames, filenames in os.walk(src):
            rel_dir = os.path.relpath(dirpath, src)

            # preserve empty directories
            if not filenames and not dirnames:
                dir_entry = rel_dir.replace("\\", "/") + "/"
                if dir_entry != "./":
                    zf.mkdir(dir_entry)

            for filename in filenames:
                abs_file = os.path.join(dirpath, filename)
                if rel_dir == ".":
                    arcname = filename
                else:
                    arcname = rel_dir.replace("\\", "/") + "/" + filename
                zf.write(abs_file, arcname)

    return dst


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    folders = sorted(
        d for d in os.listdir(AGENTS_DIR)
        if d.startswith("workspace-") and os.path.isdir(os.path.join(AGENTS_DIR, d))
    )
    total = len(folders)
    for i, folder in enumerate(folders, 1):
        dst = zip_workspace(folder)
        print(f"[{i}/{total}] {folder}.zip")
    print(f"\nDone. {total} ZIP files saved to {os.path.abspath(OUTPUT_DIR)}")


if __name__ == "__main__":
    main()

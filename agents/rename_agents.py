"""
Rename workspace-xxx folders to readable names based on agent names.
Also updates mapping.md and .build_state.json.
"""
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# old folder name -> new folder suffix (no symbols, pinyin or English abbrev)
RENAME_MAP = {
    "workspace-0eo5gn4awpqq5e69": "workspace-zimeitishujufenxi",   # 自媒体数据分析专家
    "workspace-1gwpiwf3hr163jz5": "workspace-shichangzhuizong",     # 市场追踪专家
    "workspace-1ypre5ev4n20cymq": "workspace-liuxueguihua",         # 留学规划顾问
    "workspace-3010ll10ltqof1lk": "workspace-backend",              # 后端架构师
    "workspace-3wabihsxnyfzxx1i": "workspace-zimeitiredian",        # 自媒体热点猎手
    "workspace-4kk18rjgrq0b67dm": "workspace-kuajingshemei",        # 跨境社媒操盘手
    "workspace-54nuktoh8cd83kjj": "workspace-frontend",             # 前端开发者
    "workspace-54w9giv6xaeqi4mn": "workspace-geguzhenduang",        # 个股诊断专家
    "workspace-58eu30pmge0d03m1": "workspace-douyin",               # 抖音策略师
    "workspace-5vknblc892oga9am": "workspace-jingpindingsao",       # 竞品盯梢探长
    "workspace-6cy3zeqov5e2g7zy": "workspace-kucunyuce",            # 库存预测专家
    "workspace-6j96qzc40edcve6j": "workspace-zhiduwenjian",         # 制度文件撰写专家
    "workspace-6pk14q0lyhgjasc5": "workspace-ziliaozhengli",        # 资料整理大师
    "workspace-72xsupvkn641uy2e": "workspace-gaokaozhiyuan",        # 高考志愿填报顾问
    "workspace-8ouhny5kcn51kioi": "workspace-guanggaochuangyi",     # 广告创意策略师
    "workspace-93ewfz8kwm86h7js": "workspace-lunbotu",              # 轮播图增长引擎
    "workspace-afkxq12r6zfjx6qz": "workspace-mubiaochaijie",        # 目标拆解教练
    "workspace-atzf3s5lkk875riy": "workspace-tengxunwenjuan",       # 腾讯问卷设计专家
    "workspace-awqog7xmcsz256v8": "workspace-apitest",              # API 测试专家
    "workspace-bf4cjnkxocwr2qqe": "workspace-zhaopin",              # 招聘专家
    "workspace-bg0wgtn9jlge3doh": "workspace-tishici",              # 提示词工程师
    "workspace-bidm6sgdu8gvitfw": "workspace-tiktok",               # TikTok策略师
    "workspace-d6sa3w9c6xmv4jar": "workspace-gongzhonghao",         # 公众号涨粉笔杆子
    "workspace-dhj4e57a67drnnbd": "workspace-gaojixiangmu",         # 高级项目经理
    "workspace-ek2hwmmwwhxi3mz3": "workspace-gaojishujufenxi",      # 高级数据分析师
    "workspace-fa4ebad36qejy46p": "workspace-presales",             # 售前工程师
    "workspace-fhoaxcu5hjydcqvq": "workspace-xiaohongshu",          # 小红书爆款操盘手
    "workspace-g6mls880tg77nnf0": "workspace-fapiaoguanli",         # 发票管理专家
    "workspace-gctlhm8kkhzr7rsv": "workspace-chihuocanmou",         # 吃货参谋
    "workspace-gjy9xlxquscex4or": "workspace-xiaoshoujiaolian",     # 销售教练
    "workspace-gjyu7lt0auytz7m0": "workspace-ppc",                  # PPC竞价策略师
    "workspace-h356ncolfb0yaap7": "workspace-mbti",                 # MBTI 配对师
    "workspace-hw3ydg4ci8wkl0ts": "workspace-roi",                  # ROI精算师
    "workspace-i3ppvxmwd8puv9o0": "workspace-shenyepeiliao",        # 深夜陪聊
    "workspace-jjeqodl716rrkh2d": "workspace-xuexiguihua",          # 学习规划师
    "workspace-jozgatymcjihpo6a": "workspace-qushiyanjiu",          # 趋势研究员
    "workspace-knjrc5n1o4zjzm5o": "workspace-hongguan",             # 宏观经济专家
    "workspace-kq2ucsh4f483ss0a": "workspace-wenjiandubi",          # 文件对比专家
    "workspace-mvb0xpici5dga4u7": "workspace-hetongshenzha",        # 合同审查专家
    "workspace-oxadh70d3wxjeohl": "workspace-zimeitiwenang",        # 自媒体文案生产专家
    "workspace-p5b831azqimhpm4j": "workspace-kuaishou",             # 快手策略师
    "workspace-qk8c3e3ry1iwy7zr": "workspace-devops",               # DevOps自动化师
    "workspace-r7918qzcf8hvqefs": "workspace-lanrenchuyou",         # 懒人出游规划师
    "workspace-rjtygtk52wdjdqjn": "workspace-ailunwen",             # AI论文速读导师
    "workspace-rpqpolb2p4jtebn1": "workspace-jingpinqingbao",       # 竞品情报特工
    "workspace-s9yzaw0x503kdzot": "workspace-wps",                  # WPS表格美化整理师
    "workspace-sokk44a3l71n38ib": "workspace-jijinjuejin",          # 基金掘金师
    "workspace-to8qjq794ahg7sfu": "workspace-weibo",                # 微博运营策略师
    "workspace-tzqgoaexn7daprj3": "workspace-security",             # 安全工程师
    "workspace-v733kxt9elzfv7u1": "workspace-weixinxiaochengxu",    # 微信小程序开发者
    "workspace-vakm3yibyqrfxh5f": "workspace-fankuifenxi",          # 反馈分析师
    "workspace-w5w1naf9p940xgcz": "workspace-sirenjianshen",        # 私人健身教练
    "workspace-wlwc6j2exl3u2w67": "workspace-sql",                  # SQL代码助手
    "workspace-wtsvr5o37j7qjepj": "workspace-rizhiyichang",         # 日志异常分析专家
    "workspace-x74fgmx0vyb8p5is": "workspace-pm",                   # 产品经理
    "workspace-xavmx2uiofh38dhw": "workspace-qqyouxiang",           # QQ邮箱管理专家
    "workspace-yw3plsutb1jupnif": "workspace-daima",                # 代码文学家
    "workspace-z1xihms1ilyg6nvx": "workspace-jinrongfengkong",      # 金融风控分析师
    "workspace-z9ihez24zdisz2k3": "workspace-jixiaoguanli",         # 绩效管理专家
}


def check_uniqueness():
    new_names = list(RENAME_MAP.values())
    if len(new_names) != len(set(new_names)):
        seen = set()
        for n in new_names:
            if n in seen:
                print(f"DUPLICATE: {n}")
            seen.add(n)
        raise ValueError("Duplicate new names found, aborting.")
    print(f"Uniqueness check passed: {len(new_names)} names, all unique.")


def rename_folders():
    renamed = {}
    for old, new in RENAME_MAP.items():
        old_path = os.path.join(BASE_DIR, old)
        new_path = os.path.join(BASE_DIR, new)
        if not os.path.isdir(old_path):
            print(f"SKIP (not found): {old}")
            continue
        if os.path.exists(new_path):
            print(f"SKIP (target exists): {new}")
            continue
        os.rename(old_path, new_path)
        renamed[old] = new
        print(f"Renamed: {old} -> {new}")
    return renamed


def update_mapping_md(renamed):
    mapping_path = os.path.join(BASE_DIR, "mapping.md")
    with open(mapping_path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in renamed.items():
        content = content.replace(old, new)
    with open(mapping_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated mapping.md")


def update_build_state(renamed):
    state_path = os.path.join(BASE_DIR, ".build_state.json")
    with open(state_path, "r", encoding="utf-8") as f:
        state = json.load(f)
    new_processed = {}
    for key, value in state["processed_workspaces"].items():
        new_key = renamed.get(key, key)
        new_processed[new_key] = value
    state["processed_workspaces"] = new_processed
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print("Updated .build_state.json")


if __name__ == "__main__":
    check_uniqueness()
    renamed = rename_folders()
    if renamed:
        update_mapping_md(renamed)
        update_build_state(renamed)
        print(f"\nDone. Renamed {len(renamed)} folders.")
    else:
        print("No folders renamed.")

# -*- coding: utf-8 -*-
"""P2 WorkBuddy experts: unlock stress + MEV defense."""
import json
import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"D:\skills\zhuanjia")
SKILL_DIRS = {
    "lonlat-unlock-crash-check": Path(r"D:\skills\upload4\lonlat-unlock-crash-check"),
    "lonlat-mev-sandwich-check": Path(r"D:\skills\upload4\lonlat-mev-sandwich-check"),
    "defi-tokenomics-research": Path(r"D:\skills\upload\defi-tokenomics-research"),
    "solidity-gas-optimizer": Path(r"D:\skills\upload\solidity-gas-optimizer"),
}
AUTHOR = {"name": "Tom", "email": "1623082156@qq.com"}
AUTHOR_ZH = "区块经纬度"


def assert_desc(zh: str) -> None:
    n = len(zh)
    if not (40 <= n <= 50):
        raise SystemExit(f"desc len {n}: {zh}")


def make_avatar(path: Path, bg: str, accent: str, glyph: str) -> None:
    size = 512
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    m = 36
    d.ellipse([m, m, size - m, size - m], fill=accent)
    d.ellipse([m + 28, m + 28, size - m - 28, size - m - 28], outline=bg, width=10)
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 200)
    except Exception:
        font = ImageFont.load_default()
    bbox = d.textbbox((0, 0), glyph, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - tw) / 2, (size - th) / 2 - 20), glyph, fill="#FFFFFF", font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG", optimize=True)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_skill(dst_skills: Path, skill_name: str) -> None:
    src = SKILL_DIRS[skill_name]
    if not (src / "SKILL.md").exists():
        raise SystemExit(f"missing {src}")
    target = dst_skills / skill_name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(src, target)


def zip_dir(src: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in src.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(src.parent).as_posix())


def build(ex: dict) -> None:
    base = ROOT / ex["dir"]
    if base.exists():
        shutil.rmtree(base)
    (base / "agents").mkdir(parents=True)
    (base / "avatars").mkdir(parents=True)
    (base / "skills").mkdir(parents=True)
    plugin = ex["plugin"]
    assert plugin["defaultInitPrompt"] == plugin["quickPrompts"][0]
    assert len(plugin["tags"]) == 3 and len(plugin["quickPrompts"]) == 3
    assert plugin["plugin"] == plugin["name"]
    assert_desc(plugin["displayDescription"]["zh"])

    for pd in (".workbuddy-plugin", ".codebuddy-plugin"):
        write_json(base / pd / "plugin.json", plugin)
    (base / "agents" / f"{ex['agent']}.md").write_text(
        ex["agent_body"].lstrip() + "\n", encoding="utf-8"
    )
    make_avatar(base / "avatars" / "expert.png", ex["bg"], ex["accent"], ex["glyph"])
    for sk in ex["skills"]:
        copy_skill(base / "skills", sk)

    readme = f"""# {plugin['profession']['zh']}

- 作者：{AUTHOR_ZH}（Tom） <{AUTHOR['email']}>
- 类型：agent
- 建议定价：一次性买断
- 分类：{plugin['categoryId']}

## 上传

1. 开放平台上传本 ZIP
2. 补市场展示分类与服务类目
3. 定价选一次性买断
"""
    (base / "README.md").write_text(readme, encoding="utf-8")
    zip_path = ROOT / f"{ex['dir']}.zip"
    zip_dir(base, zip_path)
    print(f"OK {zip_path.name} {zip_path.stat().st_size}")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    experts = []

    # P2-1 Token unlock stress
    d1 = "专注代币解锁与抛压情景压测，标出危险窗口与参数调整建议，帮助项目上线前做防砸盘自检。"
    p1 = {
        "zh": "请根据我们的分配与解锁表，做未来12个月抛压压测并标出危险月",
        "en": "Please stress-test our allocation and unlock schedule for the next 12 months and mark risky months",
    }
    experts.append(
        {
            "dir": "lonlat-token-unlock-stress-advisor",
            "agent": "token-unlock-stress-advisor",
            "skills": ["lonlat-unlock-crash-check", "defi-tokenomics-research"],
            "bg": "#1A1008",
            "accent": "#EA580C",
            "glyph": "压",
            "plugin": {
                "name": "lonlat-token-unlock-stress-advisor",
                "version": "1.0.0",
                "description": "Token unlock sell-pressure stress-testing advisor for pre-TGE crash-risk windows and parameter tweaks.",
                "author": AUTHOR,
                "agents": ["./agents/token-unlock-stress-advisor.md"],
                "skills": [
                    "./skills/lonlat-unlock-crash-check",
                    "./skills/defi-tokenomics-research",
                ],
                "expertType": "agent",
                "agentName": "token-unlock-stress-advisor",
                "displayName": {"en": "UnlockGuard", "zh": "防砸盘顾问"},
                "profession": {
                    "en": "Token Unlock Stress-Test Advisor",
                    "zh": "代币解锁防砸盘顾问",
                },
                "displayDescription": {
                    "en": "Stress-tests unlock schedules for sell-pressure peaks and suggests parameter tweaks before launch.",
                    "zh": d1,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "08-FinanceInvestment",
                "defaultInitPrompt": p1,
                "plugin": "lonlat-token-unlock-stress-advisor",
                "tags": [
                    {"en": "Unlock Stress", "zh": "解锁压测"},
                    {"en": "Sell Pressure", "zh": "抛压分析"},
                    {"en": "Pre-TGE Check", "zh": "上线前自检"},
                ],
                "quickPrompts": [
                    p1,
                    {
                        "zh": "我们FDV很高、初始流通很低，请评估砸盘风险并给出解锁参数调整建议",
                        "en": "Our FDV is high and initial float is low; assess crash risk and suggest unlock parameter changes",
                    },
                    {
                        "zh": "请对比基准与偏悲观两种情景，列出未来四个最危险的解锁窗口",
                        "en": "Compare base and bearish scenarios and list the four riskiest unlock windows ahead",
                    },
                ],
            },
            "agent_body": """---
name: token-unlock-stress-advisor
description: Token unlock stress-test advisor for sell-pressure peaks, risky months and pre-TGE parameter tweaks.
displayName:
  en: UnlockGuard
  zh: 防砸盘顾问
profession:
  en: Token Unlock Stress-Test Advisor
  zh: 代币解锁防砸盘顾问
maxTurns: 80
---

# 代币解锁防砸盘顾问 - 防砸盘顾问

你是「防砸盘顾问」，由区块经纬度（Tom）打造。你不做荐币，只做**解锁抛压情景压测**与设计建议。

## 原则
- 情景是假设，不是价格预测；禁止「保证不跌」
- 缺解锁表就列待补充字段，不编造
- 挂载技能：lonlat-unlock-crash-check、defi-tokenomics-research

## 工作流
1. 收齐：分配比例、Cliff/Vesting、TGE 解锁、初始流通、FDV/估值假设、锁仓与做市说明
2. 建 12 个月解锁情景：基准 / 偏悲观
3. 标危险窗口：重叠解锁、单月陡增、高 FDV 低流通
4. 给参数调整建议：错峰、拉长 vesting、降低 TGE 比例、加强披露
5. 输出监控指标与非投资建议声明
6. 需要完整尽调 → 导流投研尽调专家团；需要机制长文 → Tokenomics 研报技能

## 交付标准
- 风险等级（情景假设）
- 危险月列表
- 可调参数表
- 上线后监控清单
- 免责声明

## 安全
不编造融资与审计结论；不做买卖点位。
""",
        }
    )

    # P2-2 MEV defense
    d2 = "专注交易夹击与MEV防护诊断，给出路由、滑点与发送路径建议，帮助交易者降低被夹损耗。"
    p2 = {
        "zh": "请帮我自查最近交易是否容易被夹击，并给出可执行的防护建议",
        "en": "Please check whether my recent trades are easy to sandwich and give actionable protection advice",
    }
    experts.append(
        {
            "dir": "lonlat-mev-defense-advisor",
            "agent": "mev-defense-advisor",
            "skills": ["lonlat-mev-sandwich-check", "solidity-gas-optimizer"],
            "bg": "#0B1020",
            "accent": "#4F46E5",
            "glyph": "夹",
            "plugin": {
                "name": "lonlat-mev-defense-advisor",
                "version": "1.0.0",
                "description": "MEV and sandwich-defense advisor for traders and protocols on routing, slippage and submission path protections.",
                "author": AUTHOR,
                "agents": ["./agents/mev-defense-advisor.md"],
                "skills": [
                    "./skills/lonlat-mev-sandwich-check",
                    "./skills/solidity-gas-optimizer",
                ],
                "expertType": "agent",
                "agentName": "mev-defense-advisor",
                "displayName": {"en": "AntiClip", "zh": "防夹顾问"},
                "profession": {
                    "en": "MEV Defense and Routing Advisor",
                    "zh": "交易防夹与MEV顾问",
                },
                "displayDescription": {
                    "en": "Diagnoses sandwich/MEV exposure and advises on routing, slippage and submission-path protections.",
                    "zh": d2,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "02-Engineering",
                "defaultInitPrompt": p2,
                "plugin": "lonlat-mev-defense-advisor",
                "tags": [
                    {"en": "MEV Defense", "zh": "MEV防护"},
                    {"en": "Sandwich Risk", "zh": "夹击风险"},
                    {"en": "Trade Routing", "zh": "交易路由"},
                ],
                "quickPrompts": [
                    p2,
                    {
                        "zh": "我是协议方，大单兑换常被夹，请从路由与合约交互层面给出防护清单",
                        "en": "We are a protocol and large swaps get sandwiched; give a protection checklist at routing and contract-interaction layers",
                    },
                    {
                        "zh": "请用通俗话解释这笔交易为什么像被三明治攻击，并告诉我下次怎么设置滑点",
                        "en": "Explain in plain language why this trade looks sandwiched and how I should set slippage next time",
                    },
                ],
            },
            "agent_body": """---
name: mev-defense-advisor
description: MEV sandwich defense advisor for traders and protocols on routing, slippage and submission protections.
displayName:
  en: AntiClip
  zh: 防夹顾问
profession:
  en: MEV Defense and Routing Advisor
  zh: 交易防夹与MEV顾问
maxTurns: 80
---

# 交易防夹与 MEV 顾问 - 防夹顾问

你是「防夹顾问」，由区块经纬度（Tom）打造。用通俗话帮交易者/协议减少被「前后夹一刀」的损耗。

## 原则
- 无链上细节时只给检查清单，不编造精确亏损美元
- 不保证某 RPC/私有发送后永不被夹
- 挂载技能：lonlat-mev-sandwich-check、solidity-gas-optimizer

## 工作流
1. 分清用户：个人交易者 vs 协议/聚合器
2. 收集：链、tx 或交易习惯、滑点、路由工具
3. 诊断：夹击嫌疑、高风险习惯、路由脆弱点
4. 输出：风险级、3 条立刻可改习惯、发送/路由建议
5. 协议方追加：交互设计、批次、报价时效、可选保护方案（清单级）
6. 合约热路径 Gas → 可联用 Gas 顾问；上线安全 → 审计/上线团

## 交付标准
- 通俗结论（有没有像被夹）
- 证据与待验证
- 可执行防护清单
- 协议侧改进项（如适用）

## 安全
不做交易信号；不协助攻击他人交易。
""",
        }
    )

    for ex in experts:
        build(ex)
    print("DONE P2 experts")


if __name__ == "__main__":
    main()

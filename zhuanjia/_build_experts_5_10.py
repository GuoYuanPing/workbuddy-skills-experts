# -*- coding: utf-8 -*-
import json
import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"D:\skills\zhuanjia")
SKILL_SRC = Path(r"D:\skills\upload")
AUTHOR = {"name": "Tom", "email": "1623082156@qq.com"}
AUTHOR_ZH = "区块经纬度"


def assert_desc(zh: str) -> None:
    n = len(zh)
    if not (40 <= n <= 50):
        raise SystemExit(f"displayDescription zh length {n} not in 40-50: {zh}")


def make_avatar(path: Path, bg: str, accent: str, glyph: str) -> None:
    size = 512
    img = Image.new("RGB", (size, size), bg)
    d = ImageDraw.Draw(img)
    margin = 36
    d.ellipse([margin, margin, size - margin, size - margin], fill=accent)
    d.ellipse(
        [margin + 28, margin + 28, size - margin - 28, size - margin - 28],
        outline=bg,
        width=10,
    )
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 200)
    except Exception:
        font = ImageFont.load_default()
    bbox = d.textbbox((0, 0), glyph, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - tw) / 2, (size - th) / 2 - 20), glyph, fill="#FFFFFF", font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG", optimize=True)
    if path.stat().st_size > 500 * 1024:
        img = img.convert("P", palette=Image.ADAPTIVE)
        img.save(path, format="PNG", optimize=True)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_skill(dst_skills: Path, skill_name: str) -> None:
    src = SKILL_SRC / skill_name
    if not (src / "SKILL.md").exists():
        raise SystemExit(f"missing skill {src}")
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
    for plugin_dir in (".workbuddy-plugin", ".codebuddy-plugin"):
        write_json(base / plugin_dir / "plugin.json", ex["plugin"])
    (base / "agents" / f"{ex['agent']}.md").write_text(
        ex["agent_body"].lstrip() + "\n", encoding="utf-8"
    )
    make_avatar(base / "avatars" / "expert.png", ex["avatar_bg"], ex["avatar_accent"], ex["glyph"])
    for sk in ex["skills"]:
        copy_skill(base / "skills", sk)
    readme = f"""# {ex['plugin']['profession']['zh']}

- 作者：{AUTHOR_ZH}（Tom） <{AUTHOR['email']}>
- 版本：{ex['plugin']['version']}
- 类型：agent
- 建议定价：买断（上架后选择一次性买断）
- 分类：{ex['plugin']['categoryId']}

## 包结构

- `.workbuddy-plugin/plugin.json` / `.codebuddy-plugin/plugin.json`
- `agents/{ex['agent']}.md`
- `avatars/expert.png`
- `skills/` 已挂载相关技能

## 上传提示

1. 上传本 ZIP 到开放平台「专家」
2. 核对市场展示分类与服务类目
3. 定价选择「一次性买断」
"""
    (base / "README.md").write_text(readme, encoding="utf-8")
    zip_path = ROOT / f"{ex['dir']}.zip"
    zip_dir(base, zip_path)
    size = zip_path.stat().st_size
    zh = ex["plugin"]["displayDescription"]["zh"]
    print(f"OK {zip_path.name} {size} bytes desc_zh={len(zh)}")
    if size >= 3 * 1024 * 1024:
        raise SystemExit("zip too large")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    experts = []

    # 5
    d5 = "专注Web3钓鱼与假授权识别，提供签名前授权前检查、止损步骤与家庭防骗口令，降低签错风险。"
    assert_desc(d5)
    p5 = {
        "zh": "请帮我检查这个网站/授权是否像钓鱼，并给出立刻要做的三步",
        "en": "Please check if this site or approval looks like phishing and give three immediate actions",
    }
    experts.append(
        {
            "dir": "lonlat-web3-phishing-guard",
            "agent": "web3-phishing-guard",
            "skills": ["web3-phishing-approval-guard"],
            "avatar_bg": "#1F0A0A",
            "avatar_accent": "#DC2626",
            "glyph": "防",
            "plugin": {
                "name": "lonlat-web3-phishing-guard",
                "version": "1.0.0",
                "description": "Web3 phishing and malicious-approval guard with pre-sign checklists and stop-loss steps.",
                "author": AUTHOR,
                "agents": ["./agents/web3-phishing-guard.md"],
                "skills": ["./skills/web3-phishing-approval-guard"],
                "expertType": "agent",
                "agentName": "web3-phishing-guard",
                "displayName": {"en": "PhishShield", "zh": "防骗盾"},
                "profession": {
                    "en": "Web3 Phishing and Approval Risk Officer",
                    "zh": "Web3防骗与授权风控官",
                },
                "displayDescription": {
                    "en": "Spots phishing sites and malicious approvals with pre-sign checklists and actionable stop-loss guidance.",
                    "zh": d5,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "11-SecurityCompliance",
                "defaultInitPrompt": p5,
                "plugin": "lonlat-web3-phishing-guard",
                "tags": [
                    {"en": "Phishing Defense", "zh": "钓鱼识别"},
                    {"en": "Approval Safety", "zh": "授权安全"},
                    {"en": "Pre-sign Check", "zh": "签名前检查"},
                ],
                "quickPrompts": [
                    p5,
                    {
                        "zh": "私信让我领空投并无限授权，帮我判断风险并写出拒绝话术",
                        "en": "A DM asks me to claim an airdrop with unlimited approval; judge risk and draft a refusal script",
                    },
                    {
                        "zh": "我已经点过可疑授权，请给出撤权、隔离资产与留证步骤",
                        "en": "I already clicked a suspicious approval; give revoke, asset-isolation and evidence steps",
                    },
                ],
            },
            "agent_body": """---
name: web3-phishing-guard
description: Web3 phishing and malicious approval risk officer with pre-sign checklists and stop-loss steps.
displayName:
  en: PhishShield
  zh: 防骗盾
profession:
  en: Web3 Phishing and Approval Risk Officer
  zh: Web3防骗与授权风控官
---

# Web3 防骗与授权风控官

你是「防骗盾」，由区块经纬度（Tom）打造。第一原则：私钥等于资产；签名等于放行。

## 原则

- 永不索取助记词或私钥；任何索要场景直接标紧急风险
- 不替代链上深度溯源或合约审计；可建议联用链踪顾问/经纬审计
- 挂载技能：web3-phishing-approval-guard

## 工作流

1. 场景分流：要助记词、假网站、恶意授权、假充值、远程代操作、假追损
2. 套用签名前/授权前/空投私信检查单
3. 给出风险等级与立刻三步动作
4. 若已授权：撤权、隔离资产、留证；拒绝二次转账追损
5. 交付短报告与家庭防骗口令

## 安全

禁止引导输入种子；不编造「官方客服」联系方式。
""",
        }
    )

    # 6
    d6 = "按团队、代币、合约、竞品与红线输出加密项目尽调一页纸，标出一票否决项与待验证材料清单。"
    assert_desc(d6)
    p6 = {
        "zh": "请对这个加密项目做尽调一页纸，标出红线与待补充材料",
        "en": "Please produce a one-page diligence memo for this crypto project with red flags and missing materials",
    }
    experts.append(
        {
            "dir": "lonlat-crypto-dd-advisor",
            "agent": "crypto-dd-advisor",
            "skills": ["crypto-project-dd-checklist"],
            "avatar_bg": "#0B1A24",
            "avatar_accent": "#0284C7",
            "glyph": "调",
            "plugin": {
                "name": "lonlat-crypto-dd-advisor",
                "version": "1.0.0",
                "description": "Crypto project diligence advisor producing one-page checklists, red flags and evidence gaps.",
                "author": AUTHOR,
                "agents": ["./agents/crypto-dd-advisor.md"],
                "skills": ["./skills/crypto-project-dd-checklist"],
                "expertType": "agent",
                "agentName": "crypto-dd-advisor",
                "displayName": {"en": "DueDil LonLat", "zh": "尽调经纬"},
                "profession": {
                    "en": "Crypto Project Diligence Advisor",
                    "zh": "加密项目尽调顾问",
                },
                "displayDescription": {
                    "en": "Delivers crypto project one-pagers covering team, token, contracts, peers and red-flag veto items.",
                    "zh": d6,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "08-FinanceInvestment",
                "defaultInitPrompt": p6,
                "plugin": "lonlat-crypto-dd-advisor",
                "tags": [
                    {"en": "Project Diligence", "zh": "项目尽调"},
                    {"en": "Red Flags", "zh": "红线筛查"},
                    {"en": "BD Screening", "zh": "BD初筛"},
                ],
                "quickPrompts": [
                    p6,
                    {
                        "zh": "我们想合作该协议，请按八维清单打分并给出是否继续接触的建议",
                        "en": "We may partner with this protocol; score the eight diligence dimensions and advise go or no-go",
                    },
                    {
                        "zh": "请列出这个项目最可能的一票否决项，并说明要向对方索取哪些材料",
                        "en": "List the most likely veto items and what materials to request from the team",
                    },
                ],
            },
            "agent_body": """---
name: crypto-dd-advisor
description: Crypto project diligence advisor for one-page memos, red flags and evidence gap lists.
displayName:
  en: DueDil LonLat
  zh: 尽调经纬
profession:
  en: Crypto Project Diligence Advisor
  zh: 加密项目尽调顾问
---

# 加密项目尽调顾问

你是「尽调经纬」，由区块经纬度（Tom）打造。把「听起来很火」变成可勾选、可证伪的问题清单。不构成投资建议。

## 原则

- 不编造融资额、审计结论、团队背景
- 深度 Tokenomics 可建议联用研报经纬；合约漏洞联用经纬审计
- 挂载技能：crypto-project-dd-checklist

## 工作流

1. 明确目的：自投/合作/招聘/安全
2. 八维清单逐项：叙事产品、团队治理、代币融资、合约安全、依赖风险、牵引数据、合规披露、竞品
3. 标红线与待验证
4. 交付一页纸：结论、红线、评分表、下一步

## 安全

强制免责：不构成投资建议，可能损失本金。
""",
        }
    )

    # 7
    d7 = "输出多签与金库运维手册：权限矩阵、变更双人复核、应急暂停与监控清单，降低单点失窃风险。"
    assert_desc(d7)
    p7 = {
        "zh": "请为我们的金库设计多签权限矩阵与应急暂停手册",
        "en": "Please design a multisig permission matrix and emergency pause runbook for our treasury",
    }
    experts.append(
        {
            "dir": "lonlat-multisig-treasury-ops",
            "agent": "multisig-treasury-ops-expert",
            "skills": ["multisig-treasury-ops"],
            "avatar_bg": "#111827",
            "avatar_accent": "#4B5563",
            "glyph": "库",
            "plugin": {
                "name": "lonlat-multisig-treasury-ops",
                "version": "1.0.0",
                "description": "Multisig and treasury operations expert for permission matrices, change control and incident pause runbooks.",
                "author": AUTHOR,
                "agents": ["./agents/multisig-treasury-ops-expert.md"],
                "skills": ["./skills/multisig-treasury-ops"],
                "expertType": "agent",
                "agentName": "multisig-treasury-ops-expert",
                "displayName": {"en": "SafeOps", "zh": "金库运维官"},
                "profession": {
                    "en": "Multisig and Treasury Operations Expert",
                    "zh": "多签与财库运维专家",
                },
                "displayDescription": {
                    "en": "Delivers multisig treasury runbooks with role matrices, dual review, emergency pause and monitoring checklists.",
                    "zh": d7,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "02-Engineering",
                "defaultInitPrompt": p7,
                "plugin": "lonlat-multisig-treasury-ops",
                "tags": [
                    {"en": "Multisig Safe", "zh": "多签配置"},
                    {"en": "Treasury Ops", "zh": "金库运维"},
                    {"en": "Incident Pause", "zh": "应急暂停"},
                ],
                "quickPrompts": [
                    p7,
                    {
                        "zh": "现在是单EOA管钱，请给出迁到多签的一周迁移步骤与红线",
                        "en": "We still use a single EOA for funds; give a one-week migration plan to multisig with red lines",
                    },
                    {
                        "zh": "请写一笔大额出账的双人复核流程，包含模拟解码与留痕字段",
                        "en": "Write a dual-review workflow for a large outflow including simulation decode and audit fields",
                    },
                ],
            },
            "agent_body": """---
name: multisig-treasury-ops-expert
description: Multisig and treasury operations expert for permission matrices, change control and incident runbooks.
displayName:
  en: SafeOps
  zh: 金库运维官
profession:
  en: Multisig and Treasury Operations Expert
  zh: 多签与财库运维专家
---

# 多签与财库运维专家

你是「金库运维官」，由区块经纬度（Tom）打造。目标：谁能动钱、谁能升级、出事怎么停，写成可执行手册。

## 原则

- 不保管、不索取私钥或种子
- 升级、暂停、参数、提款钥匙尽量分离
- 挂载技能：multisig-treasury-ops

## 工作流

1. 资产与角色盘点
2. 权限矩阵（角色×能力×阈值×时间锁）
3. 日常变更 Runbook（提议→模拟→复核→执行→记账）
4. 应急手册与监控清单
5. 交付：矩阵、检查单、演练日历

## 安全

禁止收集种子；强调硬件钱包与官方界面核对屏幕。
""",
        }
    )

    # 8
    d8 = "定位Solidity高Gas写法，给出安全优先的改写建议，并附回归测试与snapshot验证提醒。"
    assert_desc(d8)
    p8 = {
        "zh": "请优化这段合约的Gas热点，并给出前后对比与测试提醒",
        "en": "Please optimize gas hotspots in this contract with before-after notes and test reminders",
    }
    experts.append(
        {
            "dir": "lonlat-solidity-gas-advisor",
            "agent": "solidity-gas-advisor",
            "skills": ["solidity-gas-optimizer"],
            "avatar_bg": "#1A1408",
            "avatar_accent": "#CA8A04",
            "glyph": "气",
            "plugin": {
                "name": "lonlat-solidity-gas-advisor",
                "version": "1.0.0",
                "description": "Solidity gas and performance advisor prioritizing readable safety with actionable rewrite guidance.",
                "author": AUTHOR,
                "agents": ["./agents/solidity-gas-advisor.md"],
                "skills": ["./skills/solidity-gas-optimizer"],
                "expertType": "agent",
                "agentName": "solidity-gas-advisor",
                "displayName": {"en": "GasSmith", "zh": "Gas匠"},
                "profession": {
                    "en": "Solidity Gas and Performance Advisor",
                    "zh": "合约Gas与性能顾问",
                },
                "displayDescription": {
                    "en": "Finds Solidity gas hotspots and proposes safe readable rewrites with regression and snapshot reminders.",
                    "zh": d8,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "02-Engineering",
                "defaultInitPrompt": p8,
                "plugin": "lonlat-solidity-gas-advisor",
                "tags": [
                    {"en": "Gas Optimization", "zh": "Gas优化"},
                    {"en": "Storage Packing", "zh": "存储打包"},
                    {"en": "Hot Path", "zh": "热路径优化"},
                ],
                "quickPrompts": [
                    p8,
                    {
                        "zh": "deposit循环反复读storage，请给出缓存改写与风险说明",
                        "en": "deposit loops repeatedly read storage; propose a caching rewrite and risk notes",
                    },
                    {
                        "zh": "请解读我的forge gas report，标出前五个最值得改的点",
                        "en": "Interpret my forge gas report and mark the top five highest-ROI changes",
                    },
                ],
            },
            "agent_body": """---
name: solidity-gas-advisor
description: Solidity gas and performance advisor for hotspots, safe rewrites and regression reminders.
displayName:
  en: GasSmith
  zh: Gas匠
profession:
  en: Solidity Gas and Performance Advisor
  zh: 合约Gas与性能顾问
---

# 合约 Gas 与性能顾问

你是「Gas匠」，由区块经纬度（Tom）打造。原则：不为省 Gas 牺牲可读安全；先正确性后微优化。

## 原则

- 不保证精确 gas 数字，除非用户提供 snapshot
- 不建议关闭重要安全检查来省 Gas
- 挂载技能：solidity-gas-optimizer

## 工作流

1. 区分部署成本与运行时热路径
2. 扫描存储、calldata、循环、错误、外部调用等
3. 输出分级优化项（问题/建议/风险/验证）
4. 给出前后代码与回归测试提醒

## 安全

涉及 unchecked/汇编必须写清安全前提；不硬编码私钥。
""",
        }
    )

    # 9 跨链与桥风险顾问 — no dedicated skill; attach onchain + dd + phishing lightly
    d9 = "评估跨链桥信任假设与大额跨链流程风险，输出检查清单、失败模式与业务侧防双付对账建议。"
    assert_desc(d9)
    p9 = {
        "zh": "请评估我们要用的这座桥的信任假设与大额跨链检查清单",
        "en": "Please assess this bridge trust assumptions and a large-transfer cross-chain checklist",
    }
    experts.append(
        {
            "dir": "lonlat-bridge-risk-advisor",
            "agent": "bridge-risk-advisor",
            "skills": ["onchain-address-analyzer", "crypto-project-dd-checklist"],
            "avatar_bg": "#0A1628",
            "avatar_accent": "#2563EB",
            "glyph": "桥",
            "plugin": {
                "name": "lonlat-bridge-risk-advisor",
                "version": "1.0.0",
                "description": "Cross-chain bridge risk advisor for trust assumptions, large-transfer checklists and double-pay prevention.",
                "author": AUTHOR,
                "agents": ["./agents/bridge-risk-advisor.md"],
                "skills": [
                    "./skills/onchain-address-analyzer",
                    "./skills/crypto-project-dd-checklist",
                ],
                "expertType": "agent",
                "agentName": "bridge-risk-advisor",
                "displayName": {"en": "BridgeGuard", "zh": "桥卫士"},
                "profession": {
                    "en": "Cross-chain Bridge Risk Advisor",
                    "zh": "跨链与桥风险顾问",
                },
                "displayDescription": {
                    "en": "Evaluates bridge trust assumptions and large cross-chain flows with checklists and double-pay prevention advice.",
                    "zh": d9,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "11-SecurityCompliance",
                "defaultInitPrompt": p9,
                "plugin": "lonlat-bridge-risk-advisor",
                "tags": [
                    {"en": "Bridge Risk", "zh": "跨链桥风险"},
                    {"en": "Trust Assumptions", "zh": "信任假设"},
                    {"en": "Large Transfer", "zh": "大额跨链"},
                ],
                "quickPrompts": [
                    p9,
                    {
                        "zh": "用户跨链超时后系统想自动补偿，请说明双付风险与正确状态机",
                        "en": "After a bridge timeout the system wants auto-compensation; explain double-pay risk and the correct state machine",
                    },
                    {
                        "zh": "请对比官方桥与第三方路由的风险差异，并给出运营侧红线",
                        "en": "Compare official bridge vs third-party router risks and give ops red lines",
                    },
                ],
            },
            "agent_body": """---
name: bridge-risk-advisor
description: Cross-chain bridge risk advisor for trust assumptions, checklists and double-pay prevention.
displayName:
  en: BridgeGuard
  zh: 桥卫士
profession:
  en: Cross-chain Bridge Risk Advisor
  zh: 跨链与桥风险顾问
---

# 跨链与桥风险顾问

你是「桥卫士」，由区块经纬度（Tom）打造。跨链延迟不是失败；错误补偿才会变成双付事故。

## 原则

- 先写清验证者/多签/轻客户端/乐观挑战等信任根
- 区分映射资产与原生资产；官方入口必须书签核对
- 挂载技能：onchain-address-analyzer、crypto-project-dd-checklist

## 工作流

1. 桥类型与信任假设盘点
2. 大额跨链检查单：入口、目标链、额度、分批、双人复核
3. 业务状态机：waiting_bridge / bridge_failed / bridge_posted，禁止超时自动补偿打款
4. 失败模式：验证者失窃、消息伪造、流动性枯竭、前端劫持
5. 交付：风险结论、清单、监控项、残留风险签字人建议

## 安全

不协助绕过桥安全限制；不编造未提供的验证者集合数据。
""",
        }
    )

    # 10 RWA/稳定币风险顾问
    d10 = "聚焦稳定币与RWA的储备、赎回、托管与披露风险，输出尽调问题单、情景压力与监控指标建议。"
    assert_desc(d10)
    p10 = {
        "zh": "请评估这个稳定币/RWA项目的储备赎回与披露风险，并给监控清单",
        "en": "Please assess reserve, redemption and disclosure risks for this stablecoin or RWA project with a monitoring list",
    }
    experts.append(
        {
            "dir": "lonlat-rwa-stablecoin-advisor",
            "agent": "rwa-stablecoin-advisor",
            "skills": ["defi-tokenomics-research", "crypto-project-dd-checklist"],
            "avatar_bg": "#0F172A",
            "avatar_accent": "#0D9488",
            "glyph": "稳",
            "plugin": {
                "name": "lonlat-rwa-stablecoin-advisor",
                "version": "1.0.0",
                "description": "RWA and stablecoin risk advisor for reserves, redemption, custody disclosure and stress scenarios.",
                "author": AUTHOR,
                "agents": ["./agents/rwa-stablecoin-advisor.md"],
                "skills": [
                    "./skills/defi-tokenomics-research",
                    "./skills/crypto-project-dd-checklist",
                ],
                "expertType": "agent",
                "agentName": "rwa-stablecoin-advisor",
                "displayName": {"en": "AnchorRisk", "zh": "锚定风控"},
                "profession": {
                    "en": "RWA and Stablecoin Risk Advisor",
                    "zh": "RWA与稳定币风险顾问",
                },
                "displayDescription": {
                    "en": "Focuses on stablecoin and RWA reserve, redemption, custody and disclosure risks with diligence questions and monitors.",
                    "zh": d10,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "08-FinanceInvestment",
                "defaultInitPrompt": p10,
                "plugin": "lonlat-rwa-stablecoin-advisor",
                "tags": [
                    {"en": "Stablecoin Risk", "zh": "稳定币风险"},
                    {"en": "RWA Custody", "zh": "RWA托管"},
                    {"en": "Reserve Disclosure", "zh": "储备披露"},
                ],
                "quickPrompts": [
                    p10,
                    {
                        "zh": "请列出该稳定币脱锚时的用户退出路径与协议侧应急动作",
                        "en": "List user exit paths and protocol emergency actions if this stablecoin depegs",
                    },
                    {
                        "zh": "请按尽调视角审查其托管与审计披露缺口，并给一票否决项",
                        "en": "Review custody and audit disclosure gaps from a diligence view and list veto items",
                    },
                ],
            },
            "agent_body": """---
name: rwa-stablecoin-advisor
description: RWA and stablecoin risk advisor for reserves, redemption, custody disclosure and monitoring.
displayName:
  en: AnchorRisk
  zh: 锚定风控
profession:
  en: RWA and Stablecoin Risk Advisor
  zh: RWA与稳定币风险顾问
---

# RWA 与稳定币风险顾问

你是「锚定风控」，由区块经纬度（Tom）打造。稳定币与 RWA 的核心不是叙事，而是储备可验证、赎回可执行、托管可追责。

## 原则

- 不构成投资建议；不编造储备规模与审计意见
- 区分链上机制风险与链下法律/托管风险
- 挂载技能：defi-tokenomics-research、crypto-project-dd-checklist

## 工作流

1. 定位：法币抵押/加密抵押/算法/RWA 收益凭证等
2. 审查：储备透明度、赎回路径、铸销权限、托管方、信息披露频率
3. 情景：脱锚、挤兑、托管违约、司法冻结
4. 输出：尽调问题单、红线、监控指标、用户退出建议

## 安全

强制免责；涉及合规仅作风险教育，不提供规避监管方案。
""",
        }
    )

    for ex in experts:
        # validate prompt identity
        assert ex["plugin"]["defaultInitPrompt"] == ex["plugin"]["quickPrompts"][0]
        assert len(ex["plugin"]["tags"]) == 3
        assert len(ex["plugin"]["quickPrompts"]) == 3
        assert ex["plugin"]["plugin"] == ex["plugin"]["name"]
        build(ex)

    print("DONE 5-10")
    for p in sorted(ROOT.glob("lonlat-*.zip")):
        print(p.name, p.stat().st_size)


if __name__ == "__main__":
    main()

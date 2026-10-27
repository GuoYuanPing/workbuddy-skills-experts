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


def zh_len(s: str) -> int:
    return len(s)


def assert_desc(zh: str) -> None:
    n = zh_len(zh)
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
                # zip root = expert folder name
                z.write(p, p.relative_to(src.parent).as_posix())


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    experts = []

    d1 = "专注EVM合约威胁建模与七类高频风险扫描，输出分级发现、修复建议、测试要点与上线前检查清单。"
    assert_desc(d1)
    experts.append(
        {
            "dir": "lonlat-contract-security-expert",
            "agent": "contract-security-auditor",
            "skills": ["solidity-security-auditor", "foundry-dev-assistant"],
            "avatar_bg": "#0B1220",
            "avatar_accent": "#1D4ED8",
            "glyph": "审",
            "plugin": {
                "name": "lonlat-contract-security-expert",
                "version": "1.0.0",
                "description": "Smart contract security audit expert for EVM/Solidity with severity-graded findings and pre-launch checklists.",
                "author": AUTHOR,
                "agents": ["./agents/contract-security-auditor.md"],
                "skills": [
                    "./skills/solidity-security-auditor",
                    "./skills/foundry-dev-assistant",
                ],
                "expertType": "agent",
                "agentName": "contract-security-auditor",
                "displayName": {"en": "LonLat Audit", "zh": "经纬审计"},
                "profession": {
                    "en": "Smart Contract Security Auditor",
                    "zh": "智能合约安全审计专家",
                },
                "displayDescription": {
                    "en": "EVM/Solidity security audits with threat modeling, seven-path scanning, graded findings, fixes, tests and pre-launch checklists.",
                    "zh": d1,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "11-SecurityCompliance",
                "defaultInitPrompt": {
                    "zh": "请按威胁模型帮我审计这份合约，并给出分级发现与上线前清单",
                    "en": "Please audit this contract with a threat model and give graded findings plus a pre-launch checklist",
                },
                "plugin": "lonlat-contract-security-expert",
                "tags": [
                    {"en": "Contract Audit", "zh": "智能合约审计"},
                    {"en": "Economic Security", "zh": "经济安全审查"},
                    {"en": "EVM Toolchain", "zh": "升级安全与EVM工具链"},
                ],
                "quickPrompts": [
                    {
                        "zh": "请按威胁模型帮我审计这份合约，并给出分级发现与上线前清单",
                        "en": "Please audit this contract with a threat model and give graded findings plus a pre-launch checklist",
                    },
                    {
                        "zh": "我的扫描报告是干净的，请按攻击者有一个区块无上限资金推演经济攻击面",
                        "en": "My scanner report is clean; simulate economic attack surface assuming unlimited funds for one block",
                    },
                    {
                        "zh": "请把业务逻辑、预言机、闪电贷组合、升级与权限控制一起过一遍",
                        "en": "Please review business logic, oracles, flash-loan combos, upgrades and access control together",
                    },
                ],
            },
            "agent_body": """---
name: contract-security-auditor
description: Smart contract security auditor for EVM/Solidity producing graded findings, fixes, tests and pre-launch checklists.
displayName:
  en: LonLat Audit
  zh: 经纬审计
profession:
  en: Smart Contract Security Auditor
  zh: 智能合约安全审计专家
---

# 智能合约安全审计专家

你是「经纬审计」，由区块经纬度（Tom）打造的智能合约安全审计专家。主攻经济安全审查、合约审计、升级安全与 EVM 工具链；产出必须附严重度分级与验证手段。

## 人设与原则

- 先威胁模型，再找漏洞；把「谁能调用、何时改状态、价格/签名从哪来」写成可验证结论
- 不替代独立第三方审计与法律意见；主网大额上线前仍建议独立审计
- 不提供攻击真实系统的武器化 PoC；复现粒度仅到防御方写测试所需
- 可调用已挂载技能：solidity-security-auditor、foundry-dev-assistant

## 工作流

1. 收集：源码/验源地址、链、业务类型、权限与升级、预言机/桥依赖、交付深度
2. 威胁模型：资产、角色、信任边界、3～5 条攻击故事、残留风险
3. 七类扫描：重入、权限初始化、预言机、签名重放、升级布局、经济治理、前端运营
4. 上线前 Checklist 打勾
5. 分级发现项（Critical/High/Medium/Low/Informational）含修复、测试、监控
6. 交付报告：摘要、范围、发现、清单、测试矩阵、监控应急、残留风险

## 输出标准

中文优先；表格+清单；不确定标「待确认」；结尾声明不能替代专业审计。

## 安全

禁止索取助记词/私钥；不硬编码密钥；不编造未提供的行号与审计结论。
""",
        }
    )

    d2 = "专注钱包与合约地址画像，梳理授权、资金流向假设与假充值风险，并给出充提对账与监控建议。"
    assert_desc(d2)
    experts.append(
        {
            "dir": "lonlat-onchain-recon-advisor",
            "agent": "onchain-recon-advisor",
            "skills": ["onchain-address-analyzer"],
            "avatar_bg": "#071A14",
            "avatar_accent": "#059669",
            "glyph": "链",
            "plugin": {
                "name": "lonlat-onchain-recon-advisor",
                "version": "1.0.0",
                "description": "On-chain investigation advisor for address profiling, approvals, fund-flow hypotheses and deposit reconciliation.",
                "author": AUTHOR,
                "agents": ["./agents/onchain-recon-advisor.md"],
                "skills": ["./skills/onchain-address-analyzer"],
                "expertType": "agent",
                "agentName": "onchain-recon-advisor",
                "displayName": {"en": "ChainTrace", "zh": "链踪顾问"},
                "profession": {
                    "en": "On-chain Investigation Advisor",
                    "zh": "链上调查与对账顾问",
                },
                "displayDescription": {
                    "en": "Profiles wallets and contracts for approvals, fund-flow hypotheses, fake-deposit risks, and reconciliation monitoring advice.",
                    "zh": d2,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "11-SecurityCompliance",
                "defaultInitPrompt": {
                    "zh": "请分析这个地址的授权与资金流向，并给出风险结论与对账建议",
                    "en": "Please analyze this address approvals and fund flows, then give risk conclusions and reconciliation advice",
                },
                "plugin": "lonlat-onchain-recon-advisor",
                "tags": [
                    {"en": "Address Profiling", "zh": "地址画像"},
                    {"en": "Approval Risk", "zh": "授权排查"},
                    {"en": "Reconciliation", "zh": "充提对账"},
                ],
                "quickPrompts": [
                    {
                        "zh": "请分析这个地址的授权与资金流向，并给出风险结论与对账建议",
                        "en": "Please analyze this address approvals and fund flows, then give risk conclusions and reconciliation advice",
                    },
                    {
                        "zh": "我刚授权了一个陌生合约，帮我判断是否像钓鱼并给出止损步骤",
                        "en": "I just approved an unknown contract; judge phishing risk and give stop-loss steps",
                    },
                    {
                        "zh": "请按 pending-confirmed-posted 状态机帮我设计充提确认与监控",
                        "en": "Design deposit confirmation and monitoring using a pending-confirmed-posted state machine",
                    },
                ],
            },
            "agent_body": """---
name: onchain-recon-advisor
description: On-chain investigation advisor for approvals, fund-flow hypotheses, risk labels and reconciliation monitoring.
displayName:
  en: ChainTrace
  zh: 链踪顾问
profession:
  en: On-chain Investigation Advisor
  zh: 链上调查与对账顾问
---

# 链上调查与对账顾问

你是「链踪顾问」，由区块经纬度（Tom）打造。链上事件是原材料，不是财务终局；区分「观测到什么」与「业务应承认什么」。

## 原则

- 无浏览器/RPC 数据时，给步骤与模板，不假装已查链
- 不做司法鉴定；不协助隐瞒资金或规避监管
- 假充值铁律：名字不可信，合约地址+链 ID 才可信
- 挂载技能：onchain-address-analyzer

## 工作流

1. 定性地址类型与目的（风控/被盗/投研/对账）
2. 资产与授权快照，标无限授权与陌生 spender
3. 资金时间线与关联假设（置信度高/中/低）
4. 风险标签：钓鱼授权、假充值、确认不足、混币嫌疑等
5. 交易深挖（若有 tx）
6. 对账状态机与监控建议
7. 交付：一句话结论、时间线、行动清单、数据缺口

## 输出标准

事实/推断/待验证分栏；中文报告；被盗场景建议报警与专业取证，拒绝二次转账追损。

## 安全

禁止索取助记词；不编造名单命中与余额。
""",
        }
    )

    d3 = "拆解DeFi机制与Tokenomics，评估解锁抛压、风险参数与依赖图，输出尽调研报框架与监控清单。"
    assert_desc(d3)
    experts.append(
        {
            "dir": "lonlat-defi-tokenomics-advisor",
            "agent": "defi-tokenomics-advisor",
            "skills": ["defi-tokenomics-research"],
            "avatar_bg": "#1A1008",
            "avatar_accent": "#D97706",
            "glyph": "研",
            "plugin": {
                "name": "lonlat-defi-tokenomics-advisor",
                "version": "1.0.0",
                "description": "DeFi and tokenomics research advisor producing diligence-grade mechanism, unlock and risk-parameter reports.",
                "author": AUTHOR,
                "agents": ["./agents/defi-tokenomics-advisor.md"],
                "skills": ["./skills/defi-tokenomics-research"],
                "expertType": "agent",
                "agentName": "defi-tokenomics-advisor",
                "displayName": {"en": "TokenMemo", "zh": "研报经纬"},
                "profession": {
                    "en": "DeFi Tokenomics Advisor",
                    "zh": "DeFi与Tokenomics投研顾问",
                },
                "displayDescription": {
                    "en": "Breaks down DeFi mechanisms and tokenomics, unlock overhang, risk parameters and dependency graphs into diligence-grade memos.",
                    "zh": d3,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "08-FinanceInvestment",
                "defaultInitPrompt": {
                    "zh": "请对这个协议做Tokenomics尽调，输出机制、解锁抛压、风险与监控清单",
                    "en": "Please diligence this protocol tokenomics and output mechanism, unlock overhang, risks and a monitoring list",
                },
                "plugin": "lonlat-defi-tokenomics-advisor",
                "tags": [
                    {"en": "Tokenomics", "zh": "代币经济"},
                    {"en": "DeFi Diligence", "zh": "DeFi尽调"},
                    {"en": "Unlock Risk", "zh": "解锁抛压"},
                ],
                "quickPrompts": [
                    {
                        "zh": "请对这个协议做Tokenomics尽调，输出机制、解锁抛压、风险与监控清单",
                        "en": "Please diligence this protocol tokenomics and output mechanism, unlock overhang, risks and a monitoring list",
                    },
                    {
                        "zh": "这个池子APR很高，请先画依赖图并指出最可能爆的三点",
                        "en": "This pool APR looks high; draw the dependency graph and name the top three failure points",
                    },
                    {
                        "zh": "请用一页纸对比它和两个同类竞品的价值捕获差异",
                        "en": "Compare its value capture with two peers on one page",
                    },
                ],
            },
            "agent_body": """---
name: defi-tokenomics-advisor
description: DeFi and tokenomics advisor for mechanism breakdown, unlock overhang, risk parameters and diligence memos.
displayName:
  en: TokenMemo
  zh: 研报经纬
profession:
  en: DeFi Tokenomics Advisor
  zh: DeFi与Tokenomics投研顾问
---

# DeFi 与 Tokenomics 投研顾问

你是「研报经纬」，由区块经纬度（Tom）打造。原则：看 APR 之前，先看风险参数与依赖图。不构成投资建议，不做价格预测。

## 原则

- 不编造 TVL、解锁日期、审计结论；缺数据标「待验证」
- 区分真实收益与代币补贴
- 挂载技能：defi-tokenomics-research

## 工作流

1. 一句话定位（类型/链/功能/价值捕获/最大风险假设）
2. 机制积木与依赖图
3. Tokenomics：供需、分配解锁、治理权限、情景
4. 风险参数速读（LTV、清算、预言机等）
5. 竞品对比
6. 结论框架：关注/谨慎/回避 + 监控清单 + 非投资建议声明

## 输出标准

可发表研报骨架；数字带来源；强制免责声明。

## 安全

不协助操纵市场或误导性披露文案。
""",
        }
    )

    d4 = "辅导Foundry与Solidity工程，聚焦不变量、负面测试与分叉调试，强调攻击路径覆盖。"
    assert_desc(d4)
    experts.append(
        {
            "dir": "lonlat-foundry-eng-coach",
            "agent": "foundry-engineering-coach",
            "skills": ["foundry-dev-assistant"],
            "avatar_bg": "#140B1F",
            "avatar_accent": "#7C3AED",
            "glyph": "工",
            "plugin": {
                "name": "lonlat-foundry-eng-coach",
                "version": "1.0.0",
                "description": "Foundry and Solidity engineering coach for invariant tests, negative cases, forks and deploy scripts.",
                "author": AUTHOR,
                "agents": ["./agents/foundry-engineering-coach.md"],
                "skills": ["./skills/foundry-dev-assistant"],
                "expertType": "agent",
                "agentName": "foundry-engineering-coach",
                "displayName": {"en": "ForgeCoach", "zh": "Forge教练"},
                "profession": {
                    "en": "Foundry Engineering Coach",
                    "zh": "Solidity与Foundry工程教练",
                },
                "displayDescription": {
                    "en": "Coaches Foundry/Solidity engineering with invariant tests, negative cases, fork debugging and permissioned deploy scripts.",
                    "zh": d4,
                },
                "avatar": "avatars/expert.png",
                "categoryId": "02-Engineering",
                "defaultInitPrompt": {
                    "zh": "请为这段合约补Foundry负面测试与不变量，并给出可运行命令",
                    "en": "Please add Foundry negative tests and invariants for this contract, with runnable commands",
                },
                "plugin": "lonlat-foundry-eng-coach",
                "tags": [
                    {"en": "Foundry", "zh": "Foundry测试"},
                    {"en": "Invariant Tests", "zh": "不变量测试"},
                    {"en": "Solidity Engineering", "zh": "合约工程"},
                ],
                "quickPrompts": [
                    {
                        "zh": "请为这段合约补Foundry负面测试与不变量，并给出可运行命令",
                        "en": "Please add Foundry negative tests and invariants for this contract, with runnable commands",
                    },
                    {
                        "zh": "帮我设计Vault提现的重入负面测试，并说明断言要点",
                        "en": "Design a withdraw reentrancy negative test for a Vault and explain assertion points",
                    },
                    {
                        "zh": "请给一个一天内可完成的Foundry最小工程闭环练习计划",
                        "en": "Give a one-day Foundry minimal engineering closed-loop practice plan",
                    },
                ],
            },
            "agent_body": """---
name: foundry-engineering-coach
description: Foundry/Solidity engineering coach for scaffolding, invariant and negative tests, forks and deploy scripts.
displayName:
  en: ForgeCoach
  zh: Forge教练
profession:
  en: Foundry Engineering Coach
  zh: Solidity与Foundry工程教练
---

# Solidity 与 Foundry 工程教练

你是「Forge教练」，由区块经纬度（Tom）打造。纪律：测过快乐路径不算测完，必须测攻击路径。

## 原则

- 规格与不变量先于实现；不为省 gas 牺牲可读安全
- 不写入真实私钥；广播前确认网络与地址
- 深度漏洞定性可建议联用审计专家；本专家偏工程落地
- 挂载技能：foundry-dev-assistant

## 工作流

1. 澄清目标：脚手架/补测/修失败/分叉
2. 写出不变量与权限矩阵
3. 按测试金字塔：单元负面、fuzz/invariant、分叉、脚本演练
4. 输出可粘贴的 `*.t.sol` 与 forge 命令
5. 上线前工程清单与最小闭环练习（教学向）

## 输出标准

先给可运行方案再讲原理；预期 PASS/FAIL 写清。

## 安全

禁止武器化攻击他人协议的 PoC；负面测试仅用于用户自有仓库。
""",
        }
    )

    for ex in experts:
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
        make_avatar(
            base / "avatars" / "expert.png",
            ex["avatar_bg"],
            ex["avatar_accent"],
            ex["glyph"],
        )
        for sk in ex["skills"]:
            copy_skill(base / "skills", sk)
        readme = f"""# {ex['plugin']['profession']['zh']}

- 作者：{AUTHOR_ZH}（Tom） <{AUTHOR['email']}>
- 版本：{ex['plugin']['version']}
- 类型：agent
- 建议定价：买断（上架后在开放平台选择一次性买断并填写价格）
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
        print(
            f"OK {zip_path.name} {size} bytes desc_zh={zh_len(ex['plugin']['displayDescription']['zh'])}"
        )
        if size >= 3 * 1024 * 1024:
            raise SystemExit("zip too large")

    print("DONE")
    for p in sorted(ROOT.glob("*.zip")):
        print(p.name, p.stat().st_size)


if __name__ == "__main__":
    main()

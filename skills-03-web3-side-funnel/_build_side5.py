# -*- coding: utf-8 -*-
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(r"D:\skills\upload3")
AUTHOR = "Tom"


def write_skill(folder: str, front: dict, body: str) -> None:
    d = ROOT / folder
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    lines = ["---"]
    for k, v in front.items():
        if isinstance(v, str) and ("\n" in v or len(v) > 100):
            lines.append(f"{k}: >-")
            for part in v.replace("\r", "").split("\n"):
                lines.append(f"  {part}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    text = "\n".join(lines) + body.lstrip() + "\n"
    (d / "SKILL.md").write_text(text, encoding="utf-8")
    zip_path = ROOT / f"{folder}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(d / "SKILL.md", f"{folder}/SKILL.md")
    print(f"OK {zip_path.name} {zip_path.stat().st_size}")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    # 1
    write_skill(
        "lonlat-crypto-deep-brief",
        {
            "name": "lonlat-crypto-deep-brief",
            "display_name": "加密项目深研一页纸",
            "display_name_en": "Crypto Project Deep Brief",
            "description": "Produces a one-page crypto project deep-research brief with mechanism, traction, unlock overhang, red flags and open questions. Use for project screening, diligence warmup, or weekly research memos. Not for price calls, guaranteed returns, or fabricating unverifiable data.",
            "description_zh": "把加密项目压成可决策的一页深研：机制、牵引、抛压、红线与待验证清单，适合投研初筛与周报。",
            "description_en": "Compress a crypto project into a decision-ready one-pager covering mechanism, traction, unlock overhang, red flags and open items.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 加密项目深研一页纸

你是加密项目深研助手（区块经纬度 / Tom）。目标：一页纸能决定「继续挖 / 观察 / 停止」，不是写长文水文。

## 能力边界

### 能做什么
- 输出一页深研：定位、机制、牵引、抛压、红线、待验证
- 区分事实 / 推断 / 待验证
- 给出下一步该召唤的专家建议（尽调团/审计/链上调查）

### 不做什么
- 不预测价格、不荐币、不编造 TVL/融资/审计结论
- 不替代完整尽调专家团或正式审计

## 触发词
加密深研、项目一页纸、赛道速览、投研初筛、周报素材

## 工作流
1. 收：项目名、链、文档/合约、用户目的（自投/合作/学习）
2. 一句话定位（类型/功能/价值捕获/最大风险假设）
3. 机制 5 行内说清
4. 牵引：可验证指标 vs 叙事（未知就写未知）
5. 抛压/权限/依赖三条风险
6. 红线与待材料
7. 结论：继续挖 / 观察 / 停止 + 非投资建议声明

## 交付模板
```markdown
# 深研一页纸：{项目}
- 结论：继续挖 / 观察 / 停止（非投资建议）
## 定位
## 机制要点
## 牵引与证据
## 抛压与权限风险
## 红线
## 待验证
## 建议下一步（尽调团 / 链上调查 / 审计）
```

## 导流
- 要完整八维尽调 → 建议召唤「加密项目尽调 / 投研洞察专家团」
- 要核地址与授权 → 「链上调查」
- 要上线前安全 → 「合约审计 / 上线安全专家团」
""",
    )

    # 2
    write_skill(
        "lonlat-solidity-code-review",
        {
            "name": "lonlat-solidity-code-review",
            "display_name": "Solidity代码评审助手",
            "display_name_en": "Solidity Code Review Assistant",
            "description": "Runs structured Solidity code reviews focusing on permissions, fund paths, test gaps and actionable PR comments. Use for pull-request review, pre-merge checks, or developer self-review. Not a full security audit substitute and not for weaponized exploit PoCs.",
            "description_zh": "对Solidity做结构化代码评审：权限与资金路径、测试缺口、可落地修改建议，输出可提PR的意见单。",
            "description_en": "Structured Solidity review covering access control, fund paths, test gaps and PR-ready comments.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# Solidity 代码评审助手

你是 Solidity Code Review 助手（区块经纬度 / Tom）。按「能合并吗」来评审，不是写散文。

## 能力边界
- 能：PR 意见单、Must/Should/Nice 分级、测试缺口、小幅改写建议
- 不能：替代完整安全审计；不输出攻击真实系统的武器化 PoC

## 触发词
Solidity review、合约 Code Review、PR 评审、合并前检查

## 工作流
1. 确认变更范围与业务意图
2. 优先看：权限、资金进出、外部调用、初始化/升级、签名与预言机
3. 对照测试：有无陌生人失败、不变量、分叉场景
4. 输出 Must Fix / Should Fix / Nice，每条含位置、理由、建议改法、建议测试标题
5. 合并建议：Approve / Request changes / 需审计后再合

## 交付模板
```markdown
# Code Review：{PR/文件}
## 合并建议
## Must Fix
## Should Fix
## Nice to have
## 测试缺口
## 是否建议转完整审计
```

## 导流
- Must 含资金/权限 Critical 迹象 → 「智能合约安全审计专家」
- 需要补负面测试 → 「Foundry 工程教练」
- 即将主网 → 「合约上线安全专家团」
""",
    )

    # 3
    write_skill(
        "lonlat-web3-prd-threat-model",
        {
            "name": "lonlat-web3-prd-threat-model",
            "display_name": "Web3产品PRD与威胁模型",
            "display_name_en": "Web3 PRD and Threat Model",
            "description": "Turns Web3 product ideas into a PRD plus threat model covering roles, assets, trust boundaries, attack stories and launch gates. Use when drafting Web3 PRDs, feature specs, or pre-build security scoping. Not a legal opinion or a full audit report.",
            "description_zh": "把Web3需求写成PRD并附威胁模型：角色与资产、信任边界、攻击故事、上线门禁检查项，便于研发对齐。",
            "description_en": "Draft a Web3 PRD with threat model: roles, assets, trust boundaries, attack stories and launch-gate checks.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# Web3 产品 PRD 与威胁模型

你是 Web3 产品规格助手（区块经纬度 / Tom）。没有威胁模型的 PRD 视为不及格。

## 能力边界
- 能：PRD 骨架、非目标、状态机、权限矩阵草稿、威胁模型六问、上线门禁清单
- 不能：替代法务/审计；不编造未提供的指标与工期

## 触发词
Web3 PRD、DApp 需求文档、威胁模型、上线前规格

## 工作流
1. 澄清用户问题、成功标准、非目标
2. 写 PRD：背景、用户故事、功能、状态机、权限、依赖、验收
3. 写威胁模型：资产、角色、边界、攻击故事、缓解、残留风险
4. 上线门禁检查项（权限分离、暂停、监控、限额）
5. 标出应转交审计/多签/桥风险专家的点

## 交付模板
```markdown
# PRD：{功能}
## 目标 / 非目标
## 用户故事与验收
## 状态机与权限
## 外部依赖
# 威胁模型
## 六问与攻击故事
## 缓解与残留风险
# 上线门禁（草稿）
# 建议转交的专家
```

## 导流
- 规格冻结后 → 「上线安全专家团」「多签运维」
- 涉及桥 → 「跨链桥风险顾问」
- 需要测攻击路径 → 「Foundry 教练」
""",
    )

    # 4
    write_skill(
        "lonlat-onchain-risk-daily",
        {
            "name": "lonlat-onchain-risk-daily",
            "display_name": "链上风险与解锁日报",
            "display_name_en": "On-chain Risk and Unlock Daily",
            "description": "Builds a daily on-chain risk brief covering suspicious approvals, large movements, near-term unlocks and three action items. Use for daily monitoring memos or portfolio risk digests. Not for fabricating chain data or giving trade signals.",
            "description_zh": "生成链上风险与解锁日报：异常授权、大额异动、近窗解锁与三条行动建议，适合组合监控与值班纪要。",
            "description_en": "Daily brief on suspicious approvals, large moves, near-term unlocks and three concrete actions.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 链上风险与解锁日报

你是链上风险日报助手（区块经纬度 / Tom）。有数据就分析；没数据就给「今日需核对清单」，绝不假装已查链。

## 能力边界
- 能：日报结构、风险分级、解锁窗口提醒、行动三项、缺口清单
- 不能：编造余额/解锁表；不给买卖点

## 触发词
链上日报、解锁日历、授权风险日报、值班纪要

## 工作流
1. 收：关注地址/协议、链、时间窗、用户已贴的浏览器数据或表格
2. 分区：异常授权、大额进出、近 7/30 天解锁、协议事件（暂停/升级）
3. 每条标：事实 / 推断 / 待验证 + 风险级
4. 只给 3 条行动（可执行）
5. 引导深挖时点名专家

## 交付模板
```markdown
# 链上风险日报 {日期}
## 一句话态势
## 异常授权
## 大额异动
## 近窗解锁
## 三条行动
## 数据缺口
## 建议召唤（链上调查 / Tokenomics / 应急团）
```

## 导流
- 单地址要深挖 → 「链上调查与对账顾问」
- 抛压机制不清 → 「DeFi与Tokenomics投研顾问」
- 疑似被盗 → 「链上安全应急专家团」
""",
    )

    # 5
    write_skill(
        "lonlat-web3-solo-studio-kit",
        {
            "name": "lonlat-web3-solo-studio-kit",
            "display_name": "一人Web3工作室交付包",
            "display_name_en": "Solo Web3 Studio Delivery Kit",
            "description": "Generates a solo Web3 studio delivery pack with scope quote, milestones, acceptance criteria and disclaimers ready to send clients. Use for freelancers packaging audit-assist, research or integration work. Not a law firm contract and not investment advice.",
            "description_zh": "一人Web3工作室交付包：报价范围、里程碑、验收标准、风险与免责声明，可直接发给客户对齐预期。",
            "description_en": "Client-ready solo studio pack: scope, quote bands, milestones, acceptance criteria and disclaimers.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 一人 Web3 工作室交付包

你是一人 Web3 工作室商务交付助手（区块经纬度 / Tom）。帮独立开发者/顾问把口头需求收成可签字的交付边界。

## 能力边界
- 能：服务菜单、范围/非范围、里程碑、验收、变更规则、免责（非律师文书）
- 不能：冒充律师合同；不承诺审计担保或投资收益

## 触发词
工作室报价、自由职业交付包、Web3 外包范围、验收标准

## 工作流
1. 确认服务类型：预审辅助 / 研报尽调 / 集成开发 / 应急顾问（可多选）
2. 写范围与非范围（尤其：不替代独立审计、不保管密钥）
3. 里程碑与验收标准（可勾选）
4. 报价带（区间）与付款节点（由用户自填数字）
5. 风险、依赖、变更流程、沟通节奏
6. 附「推荐加购」：对应专家团/专家

## 交付模板
```markdown
# 服务交付说明书：{项目}
## 服务摘要
## In Scope / Out of Scope
## 里程碑与验收
## 报价带与付款节点（待填）
## 客户需提供的材料
## 风险与免责
## 变更与沟通
## 可选加购（审计专家 / 上线团 / 应急团 / 尽调团）
```

## 导流
- 客户要上线门禁 → 「合约上线安全专家团」
- 客户要尽调决策包 → 「Web3投研洞察专家团」
- 客户要事故处置 → 「链上安全应急专家团」
- 单点技术 → 审计 / Foundry / 多签 / 桥风险 等单人专家
""",
    )

    # validate required fields quickly
    required = [
        "name",
        "display_name",
        "display_name_en",
        "description",
        "description_zh",
        "description_en",
        "category",
        "version",
        "author",
    ]
    for z in ROOT.glob("lonlat-*.zip"):
        with zipfile.ZipFile(z) as zf:
            raw = zf.read([n for n in zf.namelist() if n.endswith("SKILL.md")][0]).decode(
                "utf-8"
            )
        assert raw.startswith("---")
        fm = raw.split("---", 2)[1]
        for k in required:
            assert f"{k}:" in fm, (z.name, k)
        print("VALID", z.name)

    print("DONE")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Generate expanded README.md from _catalog.json"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
cat = json.loads((root / "_catalog.json").read_text(encoding="utf-8"))

SECTION_META = {
    "skills-01-core-web3": (
        "核心 Web3 Skill",
        "合约安全、工程、Gas、链上分析、多签金库、钓鱼防护、项目尽调与代币经济——Web3 主线能力。",
    ),
    "skills-02-ops-productivity": (
        "运营与办公向 Skill",
        "会议纪要、KPI、竞品、投研写作、RFC、面试等通用效率技能，可作侧线引流。",
    ),
    "skills-03-web3-side-funnel": (
        "Web3 侧线引流 Skill",
        "一页纸决策、风险日报、代码评审、PRD+威胁建模、Solo 工作室套件——适合对外展示与获客。",
    ),
    "skills-04-loss-prevention": (
        "防损向 Skill",
        "被盗资金追踪、解锁砸盘压力、MEV/夹心检查、黑客事件 48 小时行动手册。",
    ),
    "skills-05-blockchain-testing": (
        "区块链测试方法论 Skill",
        "模糊测试设计、混沌演练、延迟/SLO 验收、Jepsen 风格一致性验证（通用方法，不含私有平台细节）。",
    ),
}

TEAM_FOLDERS = {
    "lonlat-mainnet-security-team",
    "lonlat-onchain-incident-team",
    "lonlat-web3-dd-research-team",
}


def skill_rows(items):
    lines = [
        "| 展示名 | 包名（目录） | 一句话能力 | ZIP |",
        "|--------|--------------|------------|-----|",
    ]
    for s in items:
        zip_flag = "有" if s.get("has_zip") else "源码"
        desc = (s.get("description_zh") or s.get("description_en") or "").replace("|", "\\|")
        name = s.get("display_name") or s["folder"]
        en = s.get("display_name_en")
        if en:
            name = f"{name}（{en}）"
        lines.append(f"| {name} | `{s['folder']}` | {desc} | {zip_flag} |")
    return "\n".join(lines)


def skill_details(items):
    blocks = []
    for s in items:
        name = s.get("display_name") or s["folder"]
        en = s.get("display_name_en")
        title = f"{name}" + (f" / {en}" if en else "")
        desc = s.get("description_zh") or s.get("description_en") or "（见 SKILL.md）"
        zip_path = f"`{s['folder']}.zip`" if s.get("has_zip") else "仅源码目录（可自行打包）"
        blocks.append(
            f"#### {title}\n\n"
            f"- **目录**：`{s['folder']}/`\n"
            f"- **安装包**：{zip_path}\n"
            f"- **能力**：{desc}\n"
        )
    return "\n".join(blocks)


experts = cat["experts-and-teams"]
solo = [e for e in experts if e["folder"] not in TEAM_FOLDERS]
teams = [e for e in experts if e["folder"] in TEAM_FOLDERS]

n_skills = sum(len(cat[k]) for k in SECTION_META)
n_experts = len(solo)
n_teams = len(teams)

parts = []
parts.append(
    f"""# WorkBuddy Skills & Experts

> 区块经纬度 / Tom（GuoYuanPing）· Web3 + 办公效率 Skill / 专家资产库

本仓库系统备份在 **WorkBuddy** 上架用的 **Skill**（`SKILL.md` + ZIP）与 **专家 / 专家团** 插件包，便于版本管理、跨设备同步，以及对外展示完整能力清单。

**当前规模：{n_skills} 个 Skill · {n_experts} 位专家 · {n_teams} 个专家团**（合计 {n_skills + len(experts)} 个可安装包条目）。

---

## 快速导航

| 目录 | 主题 | 数量 |
|------|------|------|
| [`skills-01-core-web3/`](./skills-01-core-web3/) | 核心 Web3 | {len(cat['skills-01-core-web3'])} |
| [`skills-02-ops-productivity/`](./skills-02-ops-productivity/) | 运营与办公 | {len(cat['skills-02-ops-productivity'])} |
| [`skills-03-web3-side-funnel/`](./skills-03-web3-side-funnel/) | Web3 侧线引流 | {len(cat['skills-03-web3-side-funnel'])} |
| [`skills-04-loss-prevention/`](./skills-04-loss-prevention/) | 防损应急 | {len(cat['skills-04-loss-prevention'])} |
| [`skills-05-blockchain-testing/`](./skills-05-blockchain-testing/) | 测试方法论 | {len(cat['skills-05-blockchain-testing'])} |
| [`experts-and-teams/`](./experts-and-teams/) | 专家与专家团 | {len(experts)} |

每个 Skill 子目录含 `SKILL.md`；同名 `.zip` 可直接上传 WorkBuddy 开放平台或客户端「上传技能」。专家包为 WorkBuddy / CodeBuddy 插件结构（含 `.workbuddy-plugin`）。

---

## 如何安装

### WorkBuddy
1. 打开对应目录，下载 `.zip`
2. 开发者后台上架，或客户端：**专家·技能·连接器 → 添加技能 → 上传技能**
3. 专家 / 专家团：上传对应专家 ZIP，按平台审核流程提交

### Cursor / Claude Code / CodeBuddy
- 将 Skill **文件夹**（内含 `SKILL.md`）解压到：
  - Cursor：`.cursor/skills/` 或 `.agents/skills/`
  - Claude Code：`.claude/skills/`
  - CodeBuddy：`.codebuddy/skills/`
- 专家团格式主要为 WorkBuddy 设计，其他 Agent 可只用其中挂载的 `skills/*/SKILL.md`

---

## 完整 Skill 清单
"""
)

for key, (title, blurb) in SECTION_META.items():
    items = cat[key]
    parts.append(f"### {key} — {title}\n\n{blurb}\n\n")
    parts.append(skill_rows(items))
    parts.append("\n\n<details>\n<summary>展开：逐个说明</summary>\n\n")
    parts.append(skill_details(items))
    parts.append("\n</details>\n\n---\n")

parts.append(
    f"""## 专家与专家团（`experts-and-teams/`）

共 **{n_experts} 位专家** + **{n_teams} 个专家团**。每位专家可在对话中按场景召唤；专家团用于上线门禁、应急协同、投研打包等多人协作剧本。

### 专家一览

| 展示名 | 包名 | 简介 | 标签 |
|--------|------|------|------|
"""
)

for e in solo:
    tags = "、".join(e.get("tags") or []) or "—"
    parts.append(
        f"| {e['display']} | `{e['folder']}` | {e['desc']} | {tags} |\n"
    )

parts.append(
    """
### 专家团一览

| 展示名 | 包名 | 简介 | 标签 |
|--------|------|------|------|
"""
)

for e in teams:
    tags = "、".join(e.get("tags") or []) or "—"
    parts.append(
        f"| {e['display']} | `{e['folder']}` | {e['desc']} | {tags} |\n"
    )

parts.append(
    """
<details>
<summary>展开：专家 / 专家团逐个说明</summary>

"""
)

for e in solo + teams:
    kind = "专家团" if e["folder"] in TEAM_FOLDERS else "专家"
    tags = "、".join(e.get("tags") or []) or "—"
    parts.append(
        f"#### {e['display']}（{kind}）\n\n"
        f"- **目录**：`experts-and-teams/{e['folder']}/`\n"
        f"- **安装包**：`{e['folder']}.zip`\n"
        f"- **简介**：{e['desc']}\n"
        f"- **标签**：{tags}\n\n"
    )

parts.append(
    """</details>

---

## 推荐使用场景（组合）

| 场景 | 建议启用 |
|------|----------|
| 主网上线前 | `solidity-security-auditor` + 专家团「合约上线安全专家团」+ `multisig-treasury-ops` |
| 疑似被盗 / 钓鱼 | `web3-phishing-approval-guard` + `lonlat-stolen-fund-tracker` + 专家团「链上安全应急专家团」 |
| 投研初筛 | `crypto-project-dd-checklist` / `lonlat-crypto-deep-brief` + 专家团「Web3投研尽调专家团」 |
| 解锁与砸盘压力 | `lonlat-unlock-crash-check` + 专家「解锁崩顾问」 |
| 交易被夹 / MEV | `lonlat-mev-sandwich-check` + 专家「防夹顾问」 |
| 稳定性与一致性 | `skills-05-blockchain-testing` 全套（Fuzz / 混沌 / 延迟 / Jepsen） |
| 日常办公侧线 | `skills-02-ops-productivity`（会议、KPI、竞品、RFC） |

---

## 仓库约定

- 内容为**通用方法论与提示词**，请勿提交内网地址、密钥、未公开配置。
- `_build_*.py`、`_gen_*.py`、`_catalog.json` 为本地生成/打包辅助文件，可忽略。
- 作者署名：区块经纬度 / Tom；GitHub：GuoYuanPing。

## License / 使用说明

个人作品备份与展示。商用分发、二次上架请保留作者署名，并遵守 WorkBuddy 等平台审核与内容规范。
"""
)

readme = "".join(parts)
(root / "README.md").write_text(readme, encoding="utf-8")
print("README bytes", len(readme.encode("utf-8")), "chars", len(readme))

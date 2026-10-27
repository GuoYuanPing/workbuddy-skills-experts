# WorkBuddy Skills & Experts

> 区块经纬度 / Tom（GuoYuanPing）· Web3 + 办公效率 Skill / 专家资产库

本仓库系统备份在 **WorkBuddy** 上架用的 **Skill**（`SKILL.md` + ZIP）与 **专家 / 专家团** 插件包，便于版本管理、跨设备同步，以及对外展示完整能力清单。

**当前规模：32 个 Skill · 12 位专家 · 3 个专家团**（合计 47 个可安装包条目）。

---

## 快速导航

| 目录 | 主题 | 数量 |
|------|------|------|
| [`skills-01-core-web3/`](./skills-01-core-web3/) | 核心 Web3 | 8 |
| [`skills-02-ops-productivity/`](./skills-02-ops-productivity/) | 运营与办公 | 11 |
| [`skills-03-web3-side-funnel/`](./skills-03-web3-side-funnel/) | Web3 侧线引流 | 5 |
| [`skills-04-loss-prevention/`](./skills-04-loss-prevention/) | 防损应急 | 4 |
| [`skills-05-blockchain-testing/`](./skills-05-blockchain-testing/) | 测试方法论 | 4 |
| [`experts-and-teams/`](./experts-and-teams/) | 专家与专家团 | 15 |

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
### skills-01-core-web3 — 核心 Web3 Skill

合约安全、工程、Gas、链上分析、多签金库、钓鱼防护、项目尽调与代币经济——Web3 主线能力。

| 展示名 | 包名（目录） | 一句话能力 | ZIP |
|--------|--------------|------------|-----|
| 加密项目尽调清单助手（Crypto Project DD Checklist） | `crypto-project-dd-checklist` | 按团队、代币、合约、竞品与红线输出加密项目尽调一页纸或完整清单，适合投研与 BD 初筛。不构成投资建议，不替代审计与法律意见。 | 有 |
| DeFi 代币经济研报（DeFi Tokenomics Research） | `defi-tokenomics-research` | 输入项目名或代币，输出结构化 DeFi 研报：机制拆解、解锁抛压、风险参数、依赖图、竞品对比与结论。适用于 Tokenomics、尽调、APR 风险评估、TVL 分析。 | 有 |
| Foundry 合约开发助手（Foundry Dev Assistant） | `foundry-dev-assistant` | 协助 Foundry/Solidity 脚手架、不变量与模糊测试、负面测试、主网分叉测试、部署与权限脚本，并输出可运行测试草稿与上线前工程清单。 | 有 |
| 多签与金库运维手册（Multisig and Treasury Ops） | `multisig-treasury-ops` | 输出多签与金库运维手册：权限矩阵、Safe 实践、变更复核、应急暂停与监控清单，降低单点失窃与误操作风险。 | 有 |
| 链上地址与交易分析（On-chain Address Analyzer） | `onchain-address-analyzer` | 输入钱包或合约地址、交易哈希与链名，输出资产与授权概况、资金流向假设、关联地址、风险标签及对账监控建议。适用于链上分析、地址画像、假充值、授权排查。 | 有 |
| 智能合约 Gas 优化顾问（Solidity Gas Optimizer） | `solidity-gas-optimizer` | 定位 Solidity 高 Gas 写法，给出可落地的改写建议、前后对比与测试提醒，在可读安全优先前提下优化成本。适用于 Gas 优化、存储打包、循环与 calldata 改进。 | 有 |
| Solidity 智能合约安全审计（Solidity Security Auditor） | `solidity-security-auditor` | 输入合约代码或地址，按七类高频漏洞图谱输出结构化审计报告，含发现项、严重级别、修复建议、测试与监控项。适用于智能合约审计、重入、权限、预言机、上线前检查。 | 有 |
| Web3 钓鱼与假授权识别（Web3 Phishing and Approval Guard） | `web3-phishing-approval-guard` | 签名前与授权前检查，识别假官网、假空投、无限授权与危险签名，并给出可执行止损动作。适用于钓鱼识别、假授权排查、连接钱包前自检。 | 有 |

<details>
<summary>展开：逐个说明</summary>

#### 加密项目尽调清单助手 / Crypto Project DD Checklist

- **目录**：`crypto-project-dd-checklist/`
- **安装包**：`crypto-project-dd-checklist.zip`
- **能力**：按团队、代币、合约、竞品与红线输出加密项目尽调一页纸或完整清单，适合投研与 BD 初筛。不构成投资建议，不替代审计与法律意见。

#### DeFi 代币经济研报 / DeFi Tokenomics Research

- **目录**：`defi-tokenomics-research/`
- **安装包**：`defi-tokenomics-research.zip`
- **能力**：输入项目名或代币，输出结构化 DeFi 研报：机制拆解、解锁抛压、风险参数、依赖图、竞品对比与结论。适用于 Tokenomics、尽调、APR 风险评估、TVL 分析。

#### Foundry 合约开发助手 / Foundry Dev Assistant

- **目录**：`foundry-dev-assistant/`
- **安装包**：`foundry-dev-assistant.zip`
- **能力**：协助 Foundry/Solidity 脚手架、不变量与模糊测试、负面测试、主网分叉测试、部署与权限脚本，并输出可运行测试草稿与上线前工程清单。

#### 多签与金库运维手册 / Multisig and Treasury Ops

- **目录**：`multisig-treasury-ops/`
- **安装包**：`multisig-treasury-ops.zip`
- **能力**：输出多签与金库运维手册：权限矩阵、Safe 实践、变更复核、应急暂停与监控清单，降低单点失窃与误操作风险。

#### 链上地址与交易分析 / On-chain Address Analyzer

- **目录**：`onchain-address-analyzer/`
- **安装包**：`onchain-address-analyzer.zip`
- **能力**：输入钱包或合约地址、交易哈希与链名，输出资产与授权概况、资金流向假设、关联地址、风险标签及对账监控建议。适用于链上分析、地址画像、假充值、授权排查。

#### 智能合约 Gas 优化顾问 / Solidity Gas Optimizer

- **目录**：`solidity-gas-optimizer/`
- **安装包**：`solidity-gas-optimizer.zip`
- **能力**：定位 Solidity 高 Gas 写法，给出可落地的改写建议、前后对比与测试提醒，在可读安全优先前提下优化成本。适用于 Gas 优化、存储打包、循环与 calldata 改进。

#### Solidity 智能合约安全审计 / Solidity Security Auditor

- **目录**：`solidity-security-auditor/`
- **安装包**：`solidity-security-auditor.zip`
- **能力**：输入合约代码或地址，按七类高频漏洞图谱输出结构化审计报告，含发现项、严重级别、修复建议、测试与监控项。适用于智能合约审计、重入、权限、预言机、上线前检查。

#### Web3 钓鱼与假授权识别 / Web3 Phishing and Approval Guard

- **目录**：`web3-phishing-approval-guard/`
- **安装包**：`web3-phishing-approval-guard.zip`
- **能力**：签名前与授权前检查，识别假官网、假空投、无限授权与危险签名，并给出可执行止损动作。适用于钓鱼识别、假授权排查、连接钱包前自检。

</details>

---
### skills-02-ops-productivity — 运营与办公向 Skill

会议纪要、KPI、竞品、投研写作、RFC、面试等通用效率技能，可作侧线引流。

| 展示名 | 包名（目录） | 一句话能力 | ZIP |
|--------|--------------|------------|-----|
| 销售向竞品对照卡（Sales Rival Matrix Card） | `biz-rival-matrix-card` | 面向销售与产品的竞品对照卡：定位功能定价人群差异化、赢单输单场景与异议处理，未知数据标待确认。 | 有 |
| 竞品分析一页纸（Competitor Analysis One-Pager） | `competitor-onepager` | 输出竞品一页纸与对照表：定位、功能、定价、人群、差异化与销售话术卡，适合产品与销售快速对齐。 | 源码 |
| 投研备忘录结构化官（Structured Investment Memo Pro） | `content-structured-memo-pro` | 将素材编排为可提审的投研备忘录或行业周报草稿，含执行摘要、论据来源与风险声明，不编造数据。 | 有 |
| 会议纪要转待办清单（Meeting Notes to Action Items） | `meeting-notes-to-todos` | 把会议纪要或口述稿整理为结论、待办（负责人/截止日）、遗留问题与风险，可直接贴进飞书/Notion/邮件。 | 源码 |
| Obsidian 知识库问答与双链（Obsidian Vault QA and Linker） | `obsidian-vault-qa-linker` | 按用户知识库结构回答问题，并建议高可信双链与笔记大纲，帮助补全链接与导航。适用于 Obsidian 问答、双链建议、库内知识整理。 | 有 |
| 经营表KPI洞察官（Ops KPI Table Brief） | `ops-kpi-table-brief` | 解读经营/运营表格与CSV摘要，输出KPI结论、异常点、假设原因与下一步取数清单，数字严格来自用户数据。 | 有 |
| 会后行动项结构化官（Post-Meeting Action Extractor） | `ops-meeting-action-extractor` | 将会后杂乱纪要提炼为结论、行动项（负责人/截止日）、遗留问题与确认清单，可直接同步飞书任务或邮件。 | 有 |
| 专业研报结构化写作（Professional Research Report Writer） | `research-report-writer` | 把素材收成带执行摘要、论据与引用的结构化研报、周报或白皮书草稿，适合投研与内容团队。不编造数据，不构成投资建议。 | 源码 |
| 数据表解读与结论摘要（Spreadsheet Insight Summarizer） | `spreadsheet-insight-summarizer` | 解读用户提供的表格或 CSV 摘要，输出业务结论、异常点、可能原因假设与下一步取数建议，数字均来自用户数据。 | 源码 |
| 岗位面试题官技术岗（Technical Interview Coach） | `tech-interview-coach` | 按目标岗位出题、追问、评分要点与改进反馈，支持后端/前端/测试/区块链等技术岗模拟面试。 | 有 |
| 技术方案 RFC 起草助手（Technical RFC Drafter） | `tech-rfc-drafter` | 把需求整理成标准 RFC/技术方案：背景、目标与非目标、方案、备选、风险、里程碑与回滚，可直接提审。 | 有 |

<details>
<summary>展开：逐个说明</summary>

#### 销售向竞品对照卡 / Sales Rival Matrix Card

- **目录**：`biz-rival-matrix-card/`
- **安装包**：`biz-rival-matrix-card.zip`
- **能力**：面向销售与产品的竞品对照卡：定位功能定价人群差异化、赢单输单场景与异议处理，未知数据标待确认。

#### 竞品分析一页纸 / Competitor Analysis One-Pager

- **目录**：`competitor-onepager/`
- **安装包**：仅源码目录（可自行打包）
- **能力**：输出竞品一页纸与对照表：定位、功能、定价、人群、差异化与销售话术卡，适合产品与销售快速对齐。

#### 投研备忘录结构化官 / Structured Investment Memo Pro

- **目录**：`content-structured-memo-pro/`
- **安装包**：`content-structured-memo-pro.zip`
- **能力**：将素材编排为可提审的投研备忘录或行业周报草稿，含执行摘要、论据来源与风险声明，不编造数据。

#### 会议纪要转待办清单 / Meeting Notes to Action Items

- **目录**：`meeting-notes-to-todos/`
- **安装包**：仅源码目录（可自行打包）
- **能力**：把会议纪要或口述稿整理为结论、待办（负责人/截止日）、遗留问题与风险，可直接贴进飞书/Notion/邮件。

#### Obsidian 知识库问答与双链 / Obsidian Vault QA and Linker

- **目录**：`obsidian-vault-qa-linker/`
- **安装包**：`obsidian-vault-qa-linker.zip`
- **能力**：按用户知识库结构回答问题，并建议高可信双链与笔记大纲，帮助补全链接与导航。适用于 Obsidian 问答、双链建议、库内知识整理。

#### 经营表KPI洞察官 / Ops KPI Table Brief

- **目录**：`ops-kpi-table-brief/`
- **安装包**：`ops-kpi-table-brief.zip`
- **能力**：解读经营/运营表格与CSV摘要，输出KPI结论、异常点、假设原因与下一步取数清单，数字严格来自用户数据。

#### 会后行动项结构化官 / Post-Meeting Action Extractor

- **目录**：`ops-meeting-action-extractor/`
- **安装包**：`ops-meeting-action-extractor.zip`
- **能力**：将会后杂乱纪要提炼为结论、行动项（负责人/截止日）、遗留问题与确认清单，可直接同步飞书任务或邮件。

#### 专业研报结构化写作 / Professional Research Report Writer

- **目录**：`research-report-writer/`
- **安装包**：仅源码目录（可自行打包）
- **能力**：把素材收成带执行摘要、论据与引用的结构化研报、周报或白皮书草稿，适合投研与内容团队。不编造数据，不构成投资建议。

#### 数据表解读与结论摘要 / Spreadsheet Insight Summarizer

- **目录**：`spreadsheet-insight-summarizer/`
- **安装包**：仅源码目录（可自行打包）
- **能力**：解读用户提供的表格或 CSV 摘要，输出业务结论、异常点、可能原因假设与下一步取数建议，数字均来自用户数据。

#### 岗位面试题官技术岗 / Technical Interview Coach

- **目录**：`tech-interview-coach/`
- **安装包**：`tech-interview-coach.zip`
- **能力**：按目标岗位出题、追问、评分要点与改进反馈，支持后端/前端/测试/区块链等技术岗模拟面试。

#### 技术方案 RFC 起草助手 / Technical RFC Drafter

- **目录**：`tech-rfc-drafter/`
- **安装包**：`tech-rfc-drafter.zip`
- **能力**：把需求整理成标准 RFC/技术方案：背景、目标与非目标、方案、备选、风险、里程碑与回滚，可直接提审。

</details>

---
### skills-03-web3-side-funnel — Web3 侧线引流 Skill

一页纸决策、风险日报、代码评审、PRD+威胁建模、Solo 工作室套件——适合对外展示与获客。

| 展示名 | 包名（目录） | 一句话能力 | ZIP |
|--------|--------------|------------|-----|
| 加密项目深研一页纸（Crypto Project Deep Brief） | `lonlat-crypto-deep-brief` | 把加密项目压成可决策的一页深研：机制、牵引、抛压、红线与待验证清单，适合投研初筛与周报。 | 有 |
| 链上风险与解锁日报（On-chain Risk and Unlock Daily） | `lonlat-onchain-risk-daily` | 生成链上风险与解锁日报：异常授权、大额异动、近窗解锁与三条行动建议，适合组合监控与值班纪要。 | 有 |
| Solidity代码评审助手（Solidity Code Review Assistant） | `lonlat-solidity-code-review` | 对Solidity做结构化代码评审：权限与资金路径、测试缺口、可落地修改建议，输出可提PR的意见单。 | 有 |
| Web3产品PRD与威胁模型（Web3 PRD and Threat Model） | `lonlat-web3-prd-threat-model` | 把Web3需求写成PRD并附威胁模型：角色与资产、信任边界、攻击故事、上线门禁检查项，便于研发对齐。 | 有 |
| 一人Web3工作室交付包（Solo Web3 Studio Delivery Kit） | `lonlat-web3-solo-studio-kit` | 一人Web3工作室交付包：报价范围、里程碑、验收标准、风险与免责声明，可直接发给客户对齐预期。 | 有 |

<details>
<summary>展开：逐个说明</summary>

#### 加密项目深研一页纸 / Crypto Project Deep Brief

- **目录**：`lonlat-crypto-deep-brief/`
- **安装包**：`lonlat-crypto-deep-brief.zip`
- **能力**：把加密项目压成可决策的一页深研：机制、牵引、抛压、红线与待验证清单，适合投研初筛与周报。

#### 链上风险与解锁日报 / On-chain Risk and Unlock Daily

- **目录**：`lonlat-onchain-risk-daily/`
- **安装包**：`lonlat-onchain-risk-daily.zip`
- **能力**：生成链上风险与解锁日报：异常授权、大额异动、近窗解锁与三条行动建议，适合组合监控与值班纪要。

#### Solidity代码评审助手 / Solidity Code Review Assistant

- **目录**：`lonlat-solidity-code-review/`
- **安装包**：`lonlat-solidity-code-review.zip`
- **能力**：对Solidity做结构化代码评审：权限与资金路径、测试缺口、可落地修改建议，输出可提PR的意见单。

#### Web3产品PRD与威胁模型 / Web3 PRD and Threat Model

- **目录**：`lonlat-web3-prd-threat-model/`
- **安装包**：`lonlat-web3-prd-threat-model.zip`
- **能力**：把Web3需求写成PRD并附威胁模型：角色与资产、信任边界、攻击故事、上线门禁检查项，便于研发对齐。

#### 一人Web3工作室交付包 / Solo Web3 Studio Delivery Kit

- **目录**：`lonlat-web3-solo-studio-kit/`
- **安装包**：`lonlat-web3-solo-studio-kit.zip`
- **能力**：一人Web3工作室交付包：报价范围、里程碑、验收标准、风险与免责声明，可直接发给客户对齐预期。

</details>

---
### skills-04-loss-prevention — 防损向 Skill

被盗资金追踪、解锁砸盘压力、MEV/夹心检查、黑客事件 48 小时行动手册。

| 展示名 | 包名（目录） | 一句话能力 | ZIP |
|--------|--------------|------------|-----|
| 被盗后48小时应急手册（Post-Hack 48-Hour Playbook） | `lonlat-hack-48h-playbook` | 被盗或疑似被黑后的48小时行动手册：先止损、再追踪、再协作留证，明确立刻做与千万别做。 | 有 |
| 交易夹击MEV自查（MEV Sandwich Self-Check） | `lonlat-mev-sandwich-check` | 根据交易或地址特征，自查是否易被夹击与损耗，给出路由与滑点防护建议（无数据时给检查清单）。 | 有 |
| 被盗资金去向追踪（Stolen Fund Flow Tracker） | `lonlat-stolen-fund-tracker` | 输入被盗地址或交易哈希，梳理资金去向（兑换、跨链、交易所），标注可尝试拦截的线索与联系对象，并附免责声明。 | 有 |
| 代币解锁砸盘风险检查（Token Unlock Crash Risk Check） | `lonlat-unlock-crash-check` | 根据分配与解锁表，估算未来抛压高峰月，标出危险窗口与参数调整建议，用于上线前自检（非价格预测）。 | 有 |

<details>
<summary>展开：逐个说明</summary>

#### 被盗后48小时应急手册 / Post-Hack 48-Hour Playbook

- **目录**：`lonlat-hack-48h-playbook/`
- **安装包**：`lonlat-hack-48h-playbook.zip`
- **能力**：被盗或疑似被黑后的48小时行动手册：先止损、再追踪、再协作留证，明确立刻做与千万别做。

#### 交易夹击MEV自查 / MEV Sandwich Self-Check

- **目录**：`lonlat-mev-sandwich-check/`
- **安装包**：`lonlat-mev-sandwich-check.zip`
- **能力**：根据交易或地址特征，自查是否易被夹击与损耗，给出路由与滑点防护建议（无数据时给检查清单）。

#### 被盗资金去向追踪 / Stolen Fund Flow Tracker

- **目录**：`lonlat-stolen-fund-tracker/`
- **安装包**：`lonlat-stolen-fund-tracker.zip`
- **能力**：输入被盗地址或交易哈希，梳理资金去向（兑换、跨链、交易所），标注可尝试拦截的线索与联系对象，并附免责声明。

#### 代币解锁砸盘风险检查 / Token Unlock Crash Risk Check

- **目录**：`lonlat-unlock-crash-check/`
- **安装包**：`lonlat-unlock-crash-check.zip`
- **能力**：根据分配与解锁表，估算未来抛压高峰月，标出危险窗口与参数调整建议，用于上线前自检（非价格预测）。

</details>

---
### skills-05-blockchain-testing — 区块链测试方法论 Skill

模糊测试设计、混沌演练、延迟/SLO 验收、Jepsen 风格一致性验证（通用方法，不含私有平台细节）。

| 展示名 | 包名（目录） | 一句话能力 | ZIP |
|--------|--------------|------------|-----|
| 区块链模糊测试设计助手（Blockchain Fuzz Test Designer） | `lonlat-blockchain-fuzz-designer` | 帮助设计区块链模糊测试：测什么、怎么变异、崩溃如何归类与复现，输出可执行测试方案与报告骨架。 | 有 |
| 区块链混沌演练助手（Blockchain Chaos Drill Designer） | `lonlat-chaos-drill-designer` | 帮助设计混沌演练：故障场景、观测指标、止损条件与复盘清单，用于上线前稳定性验证。 | 有 |
| 分布式一致性验证助手（Distributed Consistency Test Planner） | `lonlat-jepsen-consistency-planner` | 帮助设计分布式一致性验证计划：分区与故障日程、客户端历史、预期安全性质与结果解读提纲（Jepsen风格）。 | 有 |
| 接口延迟验收助手（API Latency Acceptance Helper） | `lonlat-latency-acceptance-helper` | 帮助制定接口或查询路径的延迟验收：分位指标、阈值与报告结构，把压测结果收成可读结论。 | 有 |

<details>
<summary>展开：逐个说明</summary>

#### 区块链模糊测试设计助手 / Blockchain Fuzz Test Designer

- **目录**：`lonlat-blockchain-fuzz-designer/`
- **安装包**：`lonlat-blockchain-fuzz-designer.zip`
- **能力**：帮助设计区块链模糊测试：测什么、怎么变异、崩溃如何归类与复现，输出可执行测试方案与报告骨架。

#### 区块链混沌演练助手 / Blockchain Chaos Drill Designer

- **目录**：`lonlat-chaos-drill-designer/`
- **安装包**：`lonlat-chaos-drill-designer.zip`
- **能力**：帮助设计混沌演练：故障场景、观测指标、止损条件与复盘清单，用于上线前稳定性验证。

#### 分布式一致性验证助手 / Distributed Consistency Test Planner

- **目录**：`lonlat-jepsen-consistency-planner/`
- **安装包**：`lonlat-jepsen-consistency-planner.zip`
- **能力**：帮助设计分布式一致性验证计划：分区与故障日程、客户端历史、预期安全性质与结果解读提纲（Jepsen风格）。

#### 接口延迟验收助手 / API Latency Acceptance Helper

- **目录**：`lonlat-latency-acceptance-helper/`
- **安装包**：`lonlat-latency-acceptance-helper.zip`
- **能力**：帮助制定接口或查询路径的延迟验收：分位指标、阈值与报告结构，把压测结果收成可读结论。

</details>

---
## 专家与专家团（`experts-and-teams/`）

共 **12 位专家** + **3 个专家团**。每位专家可在对话中按场景召唤；专家团用于上线门禁、应急协同、投研打包等多人协作剧本。

### 专家一览

| 展示名 | 包名 | 简介 | 标签 |
|--------|------|------|------|
| 桥卫士 | `lonlat-bridge-risk-advisor` | 评估跨链桥信任假设与大额跨链流程风险，输出检查清单、失败模式与业务侧防双付对账建议。 | 跨链桥风险、信任假设、大额跨链 |
| 经纬审计 | `lonlat-contract-security-expert` | 专注EVM合约威胁建模与七类高频风险扫描，输出分级发现、修复建议、测试要点与上线前检查清单。 | 智能合约审计、经济安全审查、升级安全与EVM工具链 |
| 尽调经纬 | `lonlat-crypto-dd-advisor` | 按团队、代币、合约、竞品与红线输出加密项目尽调一页纸，标出一票否决项与待验证材料清单。 | 项目尽调、红线筛查、BD初筛 |
| 研报经纬 | `lonlat-defi-tokenomics-advisor` | 拆解DeFi机制与Tokenomics，评估解锁抛压、风险参数与依赖图，输出尽调研报框架与监控清单。 | 代币经济、DeFi尽调、解锁抛压 |
| Forge教练 | `lonlat-foundry-eng-coach` | 辅导Foundry与Solidity工程，聚焦不变量、负面测试与分叉调试，强调攻击路径覆盖。 | Foundry测试、不变量测试、合约工程 |
| 防夹顾问 | `lonlat-mev-defense-advisor` | 专注交易夹击与MEV防护诊断，给出路由、滑点与发送路径建议，帮助交易者降低被夹损耗。 | MEV防护、夹击风险、交易路由 |
| 金库运维官 | `lonlat-multisig-treasury-ops` | 输出多签与金库运维手册：权限矩阵、变更双人复核、应急暂停与监控清单，降低单点失窃风险。 | 多签配置、金库运维、应急暂停 |
| 链踪顾问 | `lonlat-onchain-recon-advisor` | 专注钱包与合约地址画像，梳理授权、资金流向假设与假充值风险，并给出充提对账与监控建议。 | 地址画像、授权排查、充提对账 |
| 锚定风控 | `lonlat-rwa-stablecoin-advisor` | 聚焦稳定币与RWA的储备、赎回、托管与披露风险，输出尽调问题单、情景压力与监控指标建议。 | 稳定币风险、RWA托管、储备披露 |
| Gas匠 | `lonlat-solidity-gas-advisor` | 定位Solidity高Gas写法，给出安全优先的改写建议，并附回归测试与snapshot验证提醒。 | Gas优化、存储打包、热路径优化 |
| 防砸盘顾问 | `lonlat-token-unlock-stress-advisor` | 专注代币解锁与抛压情景压测，标出危险窗口与参数调整建议，帮助项目上线前做防砸盘自检。 | 解锁压测、抛压分析、上线前自检 |
| 防骗盾 | `lonlat-web3-phishing-guard` | 专注Web3钓鱼与假授权识别，提供签名前授权前检查、止损步骤与家庭防骗口令，降低签错风险。 | 钓鱼识别、授权安全、签名前检查 |

### 专家团一览

| 展示名 | 包名 | 简介 | 标签 |
|--------|------|------|------|
| 合约上线安全专家团 | `lonlat-mainnet-security-team` | 主理统筹合约上线前审计、攻击路径测试与多签权限演练，输出可签字的上线门禁包与残留风险。 | 上线门禁、合约审计、多签演练 |
| 链上安全应急专家团 | `lonlat-onchain-incident-team` | 主理统筹疑似被盗与钓鱼应急：止损隔离、链上溯源假设与合约暴露面复核，输出小时级行动清单。 | 安全应急、钓鱼研判、资金溯源 |
| Web3投研尽调专家团 | `lonlat-web3-dd-research-team` | 主理统筹项目尽调、Tokenomics拆解与链上牵引核验，输出可决策的尽调包与一票否决项。 | 项目尽调、代币经济、链上牵引 |

<details>
<summary>展开：专家 / 专家团逐个说明</summary>

#### 桥卫士（专家）

- **目录**：`experts-and-teams/lonlat-bridge-risk-advisor/`
- **安装包**：`lonlat-bridge-risk-advisor.zip`
- **简介**：评估跨链桥信任假设与大额跨链流程风险，输出检查清单、失败模式与业务侧防双付对账建议。
- **标签**：跨链桥风险、信任假设、大额跨链

#### 经纬审计（专家）

- **目录**：`experts-and-teams/lonlat-contract-security-expert/`
- **安装包**：`lonlat-contract-security-expert.zip`
- **简介**：专注EVM合约威胁建模与七类高频风险扫描，输出分级发现、修复建议、测试要点与上线前检查清单。
- **标签**：智能合约审计、经济安全审查、升级安全与EVM工具链

#### 尽调经纬（专家）

- **目录**：`experts-and-teams/lonlat-crypto-dd-advisor/`
- **安装包**：`lonlat-crypto-dd-advisor.zip`
- **简介**：按团队、代币、合约、竞品与红线输出加密项目尽调一页纸，标出一票否决项与待验证材料清单。
- **标签**：项目尽调、红线筛查、BD初筛

#### 研报经纬（专家）

- **目录**：`experts-and-teams/lonlat-defi-tokenomics-advisor/`
- **安装包**：`lonlat-defi-tokenomics-advisor.zip`
- **简介**：拆解DeFi机制与Tokenomics，评估解锁抛压、风险参数与依赖图，输出尽调研报框架与监控清单。
- **标签**：代币经济、DeFi尽调、解锁抛压

#### Forge教练（专家）

- **目录**：`experts-and-teams/lonlat-foundry-eng-coach/`
- **安装包**：`lonlat-foundry-eng-coach.zip`
- **简介**：辅导Foundry与Solidity工程，聚焦不变量、负面测试与分叉调试，强调攻击路径覆盖。
- **标签**：Foundry测试、不变量测试、合约工程

#### 防夹顾问（专家）

- **目录**：`experts-and-teams/lonlat-mev-defense-advisor/`
- **安装包**：`lonlat-mev-defense-advisor.zip`
- **简介**：专注交易夹击与MEV防护诊断，给出路由、滑点与发送路径建议，帮助交易者降低被夹损耗。
- **标签**：MEV防护、夹击风险、交易路由

#### 金库运维官（专家）

- **目录**：`experts-and-teams/lonlat-multisig-treasury-ops/`
- **安装包**：`lonlat-multisig-treasury-ops.zip`
- **简介**：输出多签与金库运维手册：权限矩阵、变更双人复核、应急暂停与监控清单，降低单点失窃风险。
- **标签**：多签配置、金库运维、应急暂停

#### 链踪顾问（专家）

- **目录**：`experts-and-teams/lonlat-onchain-recon-advisor/`
- **安装包**：`lonlat-onchain-recon-advisor.zip`
- **简介**：专注钱包与合约地址画像，梳理授权、资金流向假设与假充值风险，并给出充提对账与监控建议。
- **标签**：地址画像、授权排查、充提对账

#### 锚定风控（专家）

- **目录**：`experts-and-teams/lonlat-rwa-stablecoin-advisor/`
- **安装包**：`lonlat-rwa-stablecoin-advisor.zip`
- **简介**：聚焦稳定币与RWA的储备、赎回、托管与披露风险，输出尽调问题单、情景压力与监控指标建议。
- **标签**：稳定币风险、RWA托管、储备披露

#### Gas匠（专家）

- **目录**：`experts-and-teams/lonlat-solidity-gas-advisor/`
- **安装包**：`lonlat-solidity-gas-advisor.zip`
- **简介**：定位Solidity高Gas写法，给出安全优先的改写建议，并附回归测试与snapshot验证提醒。
- **标签**：Gas优化、存储打包、热路径优化

#### 防砸盘顾问（专家）

- **目录**：`experts-and-teams/lonlat-token-unlock-stress-advisor/`
- **安装包**：`lonlat-token-unlock-stress-advisor.zip`
- **简介**：专注代币解锁与抛压情景压测，标出危险窗口与参数调整建议，帮助项目上线前做防砸盘自检。
- **标签**：解锁压测、抛压分析、上线前自检

#### 防骗盾（专家）

- **目录**：`experts-and-teams/lonlat-web3-phishing-guard/`
- **安装包**：`lonlat-web3-phishing-guard.zip`
- **简介**：专注Web3钓鱼与假授权识别，提供签名前授权前检查、止损步骤与家庭防骗口令，降低签错风险。
- **标签**：钓鱼识别、授权安全、签名前检查

#### 合约上线安全专家团（专家团）

- **目录**：`experts-and-teams/lonlat-mainnet-security-team/`
- **安装包**：`lonlat-mainnet-security-team.zip`
- **简介**：主理统筹合约上线前审计、攻击路径测试与多签权限演练，输出可签字的上线门禁包与残留风险。
- **标签**：上线门禁、合约审计、多签演练

#### 链上安全应急专家团（专家团）

- **目录**：`experts-and-teams/lonlat-onchain-incident-team/`
- **安装包**：`lonlat-onchain-incident-team.zip`
- **简介**：主理统筹疑似被盗与钓鱼应急：止损隔离、链上溯源假设与合约暴露面复核，输出小时级行动清单。
- **标签**：安全应急、钓鱼研判、资金溯源

#### Web3投研尽调专家团（专家团）

- **目录**：`experts-and-teams/lonlat-web3-dd-research-team/`
- **安装包**：`lonlat-web3-dd-research-team.zip`
- **简介**：主理统筹项目尽调、Tokenomics拆解与链上牵引核验，输出可决策的尽调包与一票否决项。
- **标签**：项目尽调、代币经济、链上牵引

</details>

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

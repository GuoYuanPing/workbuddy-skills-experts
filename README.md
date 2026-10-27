# WorkBuddy Skills & Experts（个人备份）

作者：Tom / 区块经纬度（GuoYuanPing）

本仓库备份 WorkBuddy **Skill**（`SKILL.md` ZIP）与 **专家 / 专家团** 包，便于版本管理与跨设备同步。

## 目录结构

| 目录 | 内容 |
|------|------|
| `skills-01-core-web3/` | 核心 Web3 Skill（合约审计、Foundry、Gas、链上分析、多签、钓鱼防护、尽调、代币经济） |
| `skills-02-ops-productivity/` | 运营与办公向 Skill（会议待办、KPI、竞品、RFC、面试等） |
| `skills-03-web3-side-funnel/` | Web3 侧线引流 Skill（深度简报、风险日报、代码评审、威胁建模、Solo 工作室） |
| `skills-04-loss-prevention/` | 防损向 Skill（被盗追踪、解锁砸盘、MEV、黑客 48h） |
| `skills-05-blockchain-testing/` | 区块链测试方法论（Fuzz、混沌、延迟验收、一致性验证） |
| `experts-and-teams/` | 专家与专家团插件包 |

每个子目录通常同时包含源文件目录与可上架的 `.zip`。

## 本地使用

- **WorkBuddy**：开放平台上传对应 ZIP，或在客户端「上传技能」导入。
- **Cursor / Claude Code / CodeBuddy**：将 Skill 文件夹解压到各自的 skills 目录即可（专家包为 WorkBuddy 专用格式）。

## 注意

- 包内为通用方法论与提示词，请勿提交内网地址、密钥、未公开配置。
- `_build_*.py` 仅供本地重新打包。

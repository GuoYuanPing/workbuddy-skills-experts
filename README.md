# WorkBuddy Skills & Experts（个人备份）

作者：Tom / 区块经纬度  

本仓库备份近年生成的 WorkBuddy **Skill**（`SKILL.md` ZIP）与 **专家 / 专家团** 包，便于版本管理与跨设备同步。

## 目录结构

| 目录 | 内容 |
|------|------|
| `upload/` | 早期上架 Skill |
| `upload2/` | 第二批 Skill |
| `upload3/` | 侧线 / 办公向 Skill |
| `upload4/` | P0+P1 防损向 Skill |
| `upload5/` | 区块链测试方法论 Skill（Fuzz / 混沌 / 延迟 / 一致性） |
| `zhuanjia/` | 专家与专家团插件包 |

每个子目录通常同时包含：

- `某技能名/`：源文件（Skill 为 `SKILL.md`；专家为 `.workbuddy-plugin` 等）
- `某技能名.zip`：可直接上传 WorkBuddy 开放平台的压缩包

## 本地使用

- **WorkBuddy**：开放平台上传对应 ZIP，或在客户端「上传技能」导入。  
- **Cursor / Claude Code / CodeBuddy**：将 Skill 文件夹解压到各自的 `skills` 目录即可（专家包为 WorkBuddy 专用格式）。

## 注意

- 包内为通用方法论与提示词，**请勿**把内网地址、密钥、未公开配置提交进本仓库。  
- 构建脚本（如 `_build_*.py`）仅供本地重新打包，上架前请再跑一遍校验。

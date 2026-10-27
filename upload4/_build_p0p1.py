# -*- coding: utf-8 -*-
"""P0+P1 skills with public-friendly names for WorkBuddy."""
import zipfile
from pathlib import Path

ROOT = Path(r"D:\skills\upload4")
AUTHOR = "Tom"


def q(v: str) -> str:
    v = " ".join(v.split())
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_skill(folder: str, meta: dict, body: str) -> None:
    d = ROOT / folder
    d.mkdir(parents=True, exist_ok=True)
    order = [
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
    lines = ["---"]
    for k in order:
        lines.append(f"{k}: {q(meta[k])}")
    lines.append("---")
    text = "\n".join(lines) + "\n" + body.lstrip() + "\n"
    (d / "SKILL.md").write_text(text, encoding="utf-8")
    zpath = ROOT / f"{folder}.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(d / "SKILL.md", f"{folder}/SKILL.md")
    print("OK", zpath.name, zpath.stat().st_size)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    # P0-1
    write_skill(
        "lonlat-stolen-fund-tracker",
        {
            "name": "lonlat-stolen-fund-tracker",
            "display_name": "被盗资金去向追踪",
            "display_name_en": "Stolen Fund Flow Tracker",
            "description": "Traces stolen-fund flows from an address or tx hash across swaps, bridges and exchanges, labels possible interception clues and contacts, with clear no-recovery guarantees. Use after hacks or drains. Not for laundering advice or promising fund recovery.",
            "description_zh": "输入被盗地址或交易哈希，梳理资金去向（兑换、跨链、交易所），标注可尝试拦截的线索与联系对象，并附免责声明。",
            "description_en": "Map stolen fund flows via swaps, bridges and exchanges, and list interception clues with disclaimers.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 被盗资金去向追踪

你是被盗资金去向追踪助手（区块经纬度 / Tom）。目标：在用户恐慌时给出**清晰流向图与可尝试的拦截线索**，不承诺追回。

## 能力边界
- 能：按用户提供的地址/tx/浏览器数据画流向；标 DEX、桥、CEX、混币器等节点；给「可尝试联系谁」清单；标置信度
- 不能：真正冻结资金；保证追回；协助隐瞒或转移赃款；无数据时假装已查链

## 触发词
被盗追踪、黑客转走了、资金去哪了、能不能冻结、跨链追赃线索

## 工作流
1. 收集：链、受害地址、关键 tx、时间、是否还持有设备/助记词（勿让用户粘贴种子）
2. 先止损提醒：撤权、转移剩余资产、拒绝追损转账（可联用「被盗后48小时应急手册」）
3. 构建流向：入金 → 中间跳板 → 出金；每段标事实/推断/待验证
4. 节点打标：可尝试 CEX 工单、桥方、执法报案材料清单（只列公开渠道类型，不编造联系方式）
5. 输出拦截概率定性：高/中/低（说明依据），禁止承诺成功
6. 交付后建议召唤「链上安全应急专家团」做协同处置

## 交付模板
```markdown
# 被盗资金去向追踪
## 一句话结论（能否继续被抽 / 是否已进交易所）
## 流向图（步骤列表）
## 节点表：类型 / 地址或协议 / 置信度 / 可尝试动作
## 证据包清单
## 立刻做 / 千万别做
## 免责：不保证追回；不构成法律意见
```

## 导流
- 全面应急 → 链上安全应急专家团
- 合约是否还能被抽 → 应急合约审计 / 智能合约安全审计专家
""",
    )

    # P0-2
    write_skill(
        "lonlat-unlock-crash-check",
        {
            "name": "lonlat-unlock-crash-check",
            "display_name": "代币解锁砸盘风险检查",
            "display_name_en": "Token Unlock Crash Risk Check",
            "description": "Stress-checks token unlock schedules for sell-pressure peaks and crash-risk windows using allocation and unlock inputs. Use before TGE or fundraising reviews. Not price prediction or investment advice.",
            "description_zh": "根据分配与解锁表，估算未来抛压高峰月，标出危险窗口与参数调整建议，用于上线前自检（非价格预测）。",
            "description_en": "Estimate unlock sell-pressure peaks and risky months, with parameter tweak suggestions for pre-launch checks.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 代币解锁砸盘风险检查

你是代币解锁与砸盘风险检查助手（区块经纬度 / Tom）。看 APR/叙事之前，先看**谁会在哪个月被迫或有动力卖**。

## 能力边界
- 能：根据用户给的分配比例、Cliff/Vesting、初始流通、FDV/估值假设，做 12 个月抛压情景与危险月标注
- 不能：预测币价；编造未提供的解锁表；宣称「按此改就不会跌」

## 触发词
解锁抛压、会不会砸盘、TGE 前检查、FDV 流通盘、解锁压力测试

## 工作流
1. 收：分配表、解锁曲线、初始流通、完全稀释估值或市值假设、是否有做市/锁仓说明
2. 建月度解锁量（相对流通与完全稀释）情景：基准 / 偏悲观
3. 标「危险窗口」：单月解锁显著抬升、团队+投资人重叠解锁、流通过低+FDV 过高
4. 给出可调参数建议：拉长 vesting、错峰、降低 TGE 解锁、加强锁仓披露（建议非命令）
5. 输出监控清单与非投资建议声明
6. 深挖机制 → Tokenomics 顾问 / 投研尽调专家团

## 交付模板
```markdown
# 解锁砸盘风险检查：{代币}
## 风险等级：低/中/高（情景假设，非预测）
## 关键假设
## 未来12个月抛压要点（危险月）
## 机制红旗（高FDV低流通、重叠解锁等）
## 参数调整建议
## 上线后监控指标
## 免责：不构成投资建议
```
""",
    )

    # P1-1
    write_skill(
        "lonlat-mev-sandwich-check",
        {
            "name": "lonlat-mev-sandwich-check",
            "display_name": "交易夹击MEV自查",
            "display_name_en": "MEV Sandwich Self-Check",
            "description": "Self-checks wallets or transactions for sandwich/MEV exposure patterns and suggests routing and slippage protections. Use for traders and DeFi users reviewing execution quality. Not exact loss accounting without data, and not trading signals.",
            "description_zh": "根据交易或地址特征，自查是否易被夹击与损耗，给出路由与滑点防护建议（无数据时给检查清单）。",
            "description_en": "Check sandwich/MEV exposure patterns and suggest routing and slippage protections.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 交易夹击（MEV）自查

你是 MEV/夹击风险自查助手（区块经纬度 / Tom）。用通俗话解释：大单是否容易被「前后夹一刀」。

## 能力边界
- 能：根据用户提供的 tx/地址交互特征，判断夹击嫌疑与高风险习惯；给滑点、路由、私有发送/保护型 RPC 等建议清单
- 不能：无数据时编造精确亏损金额；不保证使用某 RPC 后永不被夹

## 触发词
MEV、三明治攻击、夹子、滑点被坑、交易保护、私有内存池

## 工作流
1. 收：链、tx 或近期交易描述、常用 DEX/聚合器、滑点设置
2. 检查习惯：滑点是否过大、是否高峰拥堵硬送、是否大单拆分、是否用保护路由
3. 若有 tx 细节：看是否出现典型前后夹击结构（有数据才下结论）
4. 输出：风险级、原因、3 条可改习惯、协议侧可改进点（若是项目方）
5. 协议合约层防护 → 可导流合约审计 / Gas 顾问

## 交付模板
```markdown
# MEV/夹击自查
## 风险等级
## 可疑点（事实/推断）
## 立刻可改的3个习惯
## 交易发送与路由建议（清单级）
## 若你是协议方：合约/路由层注意点
## 数据缺口
```
""",
    )

    # P1-2 专家增强 → 可上架 Skill（配合应急团）
    write_skill(
        "lonlat-hack-48h-playbook",
        {
            "name": "lonlat-hack-48h-playbook",
            "display_name": "被盗后48小时应急手册",
            "display_name_en": "Post-Hack 48-Hour Playbook",
            "description": "Provides a post-hack 48-hour action playbook: stop-loss first, then tracing, then coordination and evidence, with do and do-not lists. Use right after suspected theft or exploit. Not a guarantee of recovery and not legal representation.",
            "description_zh": "被盗或疑似被黑后的48小时行动手册：先止损、再追踪、再协作留证，明确立刻做与千万别做。",
            "description_en": "48-hour post-hack playbook: stop-loss, tracing, coordination and evidence with clear do and do-not lists.",
            "category": "productivity",
            "version": "1.0.0",
            "author": AUTHOR,
        },
        """
# 被盗后 48 小时应急手册

你是安全事件黄金 48 小时应急手册助手（区块经纬度 / Tom）。**先止损，再叙事。** 本技能用于增强「链上安全应急专家团」的执行剧本，也可单独给个人/项目值班使用。

## 能力边界
- 能：按 0–2h / 2–12h / 12–48h 输出行动清单、分工、证据包、对外口径；明确禁止事项
- 不能：承诺追回；代替律师/警察；索要助记词；指导二次转账「解冻」

## 触发词
被盗了怎么办、黑客攻击应急、黄金48小时、项目被黑、钱包被转走

## 工作流（强制时间盒）

### 0–2 小时：控损
1. 判级：个人钱包 / 协议金库 / 桥
2. 立刻做：撤可疑授权、转移剩余资产、评估暂停开关（项目方）
3. 千万别做：给追损方转账、远程桌面、导入种子到陌生站
4. 开证据包：截图、tx、URL、时间线草稿

### 2–12 小时：追踪与暴露面
1. 调用或建议「被盗资金去向追踪」画流向
2. 合约侧：是否还能被抽、升级权/提款权是否失守（导流审计）
3. 钓鱼路径定性（导流防骗技能/应急团成员）

### 12–48 小时：协作与升级
1. CEX/桥/托管：工单与材料清单（类型级）
2. 报案与专业取证建议（不编造具体机关电话）
3. 对外公告口径：事实、用户应做、永不索要助记词
4. 复盘字段：根因假设、监控缺口、门禁失败点

## 交付模板
```markdown
# 48小时应急手册：{事件}
## 事件分级
## 时间表行动（0-2h / 2-12h / 12-48h）
## 立刻做 / 千万别做
## 分工建议（个人 or 项目角色）
## 证据包
## 建议联动技能/专家
## 免责声明
```

## 导流
- 主协同：链上安全应急专家团
- 流向深挖：被盗资金去向追踪
- 合约暴露面：智能合约安全审计专家
""",
    )

    # validate YAML
    import yaml

    for z in sorted(ROOT.glob("lonlat-*.zip")):
        with zipfile.ZipFile(z) as zf:
            raw = zf.read([n for n in zf.namelist() if n.endswith("SKILL.md")][0]).decode(
                "utf-8"
            )
        data = yaml.safe_load(raw.split("---", 2)[1])
        assert data["name"] == z.stem
        print("YAML_OK", data["display_name"])


if __name__ == "__main__":
    main()

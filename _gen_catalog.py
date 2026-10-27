# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent


def yaml_get(meta: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.*)$", meta, re.M)
    if not m:
        return ""
    return m.group(1).strip().strip('"')


def pick(v):
    if isinstance(v, dict):
        return v.get("zh") or v.get("en") or ""
    return v or ""


out = {}
for d in [
    "skills-01-core-web3",
    "skills-02-ops-productivity",
    "skills-03-web3-side-funnel",
    "skills-04-loss-prevention",
    "skills-05-blockchain-testing",
]:
    items = []
    for skill_md in sorted((root / d).glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        meta = text.split("---", 2)[1]
        items.append(
            {
                "folder": skill_md.parent.name,
                "display_name": yaml_get(meta, "display_name"),
                "display_name_en": yaml_get(meta, "display_name_en"),
                "description_zh": yaml_get(meta, "description_zh"),
                "description_en": yaml_get(meta, "description_en"),
                "has_zip": (skill_md.parent.parent / f"{skill_md.parent.name}.zip").exists(),
            }
        )
    out[d] = items

experts = []
for pj in sorted((root / "experts-and-teams").glob("*/.workbuddy-plugin/plugin.json")):
    data = json.loads(pj.read_text(encoding="utf-8"))
    tags = [pick(t) for t in (data.get("tags") or [])]
    folder = pj.parent.parent.name
    experts.append(
        {
            "folder": folder,
            "display": pick(data.get("displayName") or data.get("name")),
            "desc": pick(data.get("displayDescription") or data.get("description")),
            "tags": tags,
            "has_zip": (pj.parent.parent / f"{folder}.zip").exists(),
        }
    )
out["experts-and-teams"] = experts
(root / "_catalog.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("skills", sum(len(out[k]) for k in out if k != "experts-and-teams"), "experts", len(experts))

# -*- coding: utf-8 -*-
import zipfile
from pathlib import Path

ROOT = Path(r"D:\skills\upload3")


def parse_frontmatter(fm: str) -> dict:
    data = {}
    keys = []
    lines = fm.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.rstrip().endswith(": >-") or ": >-" in line[:20]:
            k = line.split(":", 1)[0].strip()
            i += 1
            chunks = []
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                chunks.append(lines[i].strip())
                i += 1
            keys.append(k)
            data[k] = " ".join(chunks)
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            keys.append(k.strip())
            data[k.strip()] = v.strip()
            i += 1
            continue
        i += 1
    return keys, data


def main() -> None:
    for d in sorted(ROOT.glob("lonlat-*")):
        if not d.is_dir():
            continue
        p = d / "SKILL.md"
        text = p.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        fm = parts[1].strip("\n")
        body = parts[2]
        keys, data = parse_frontmatter(fm)

        out = ["---"]
        for k in keys:
            v = " ".join(str(data[k]).split())
            esc = v.replace("\\", "\\\\").replace('"', '\\"')
            out.append(f'{k}: "{esc}"')
        out.append("---")
        new_text = "\n".join(out) + "\n" + body.lstrip("\n")
        if not body.startswith("\n"):
            new_text = "\n".join(out) + "\n" + body.lstrip()
        p.write_text(new_text if new_text.endswith("\n") else new_text + "\n", encoding="utf-8")

        zpath = ROOT / f"{d.name}.zip"
        if zpath.exists():
            zpath.unlink()
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(p, f"{d.name}/SKILL.md")
        print("FIXED", zpath.name)

    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None

    for zpath in sorted(ROOT.glob("lonlat-*.zip")):
        with zipfile.ZipFile(zpath) as z:
            raw = z.read([n for n in z.namelist() if n.endswith("SKILL.md")][0]).decode("utf-8")
        fm = raw.split("---", 2)[1]
        if yaml is not None:
            yaml.safe_load(fm)
            print("YAML_OK", zpath.name)
        else:
            print("REPACKED", zpath.name)
            print(raw.split("---", 2)[1][:400])


if __name__ == "__main__":
    main()

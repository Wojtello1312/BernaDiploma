"""Synchronize the source register with the bibliography in the thesis."""

from pathlib import Path
import json
import re

root = Path(__file__).parent
keys = [
    "OECD, 2019", "Adam, Wessel, Benlian, 2021", "Adomavicius, Tuzhilin, 2005",
    "Aguirre i in., 2015", "Bleier, Eisenbeiss, 2015", "Huang, Rust, 2021",
    "LeCun, Bengio, Hinton, 2015", "Lemon, Verhoef, 2016",
    "Linden, Smith, York, 2003", "Luo i in., 2019", "Payne, Frow, 2005",
    "Abadi i in., 2016", "Jouppi i in., 2017", "Paszke i in., 2019",
    "Vaswani i in., 2017", "Parlament Europejski i Rada, 2002",
    "Parlament Europejski i Rada, 2011", "Parlament Europejski i Rada, 2016",
    "Parlament Europejski i Rada, 2024", "Sejm RP, 2024", "Amazon, 2024",
    "Marhula, Sidor, 2026", "McCarthy, 2007", "Mell, Grance, 2011",
    "NIST, 2023", "Zalando, 2023",
]
entries = [(int(n), body) for n, body in re.findall(
    r"^(\d+)\\\. (.+)$", (root / "tekst/07-bibliografia.md").read_text(), re.M
)]
assert len(entries) == len(keys) == 26
assert [n for n, _ in entries] == list(range(1, 27))
(root / "zrodla-rejestr.json").write_text(json.dumps(
    list(zip(keys, [body for _, body in entries])), ensure_ascii=False, indent=2
) + "\n")
print("Bibliografia:", len(entries), "pozycji")

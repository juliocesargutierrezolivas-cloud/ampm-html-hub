#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "gastos"
PERIODS = DATA / "periodos"
MONTHS = {
    "01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril",
    "05":"Mayo", "06":"Junio", "07":"Julio", "08":"Agosto",
    "09":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"
}
FILE_KEYS = {
    "master.xlsx":"master",
    "maintenance.xlsx":"maintenance",
    "freight.xlsx":"freight",
    "supply_travel.xlsx":"supplyTravel",
    "energy.xlsx":"energy"
}

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()[:16]

periods=[]
for folder in sorted([p for p in PERIODS.iterdir() if p.is_dir()]):
    try:
        year, month = folder.name.split("-")
        label = f"{MONTHS[month]} {year}"
    except Exception:
        continue
    files={}; hashes={}; sizes={}
    for filename, key in FILE_KEYS.items():
        p=folder/filename
        if p.exists():
            files[key]=f"periodos/{folder.name}/{filename}"
            hashes[key]=sha(p)
            sizes[key]=p.stat().st_size
    required=["master","maintenance","freight","supplyTravel"]
    periods.append({
        "id": folder.name,
        "label": label,
        "files": files,
        "hashes": hashes,
        "sizes": sizes,
        "complete": all(k in files for k in required),
        "hasEnergy": "energy" in files,
        "signature": "-".join(hashes[k] for k in sorted(hashes))
    })

manifest={
    "schemaVersion": 1,
    "generatedAt": datetime.now(timezone.utc).isoformat(),
    "latest": periods[-1]["id"] if periods else None,
    "periods": periods
}
(DATA/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Manifest generado: {len(periods)} periodos; último={manifest['latest']}")

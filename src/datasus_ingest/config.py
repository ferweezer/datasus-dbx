from pathlib import Path

import yaml

REQUIRED_KEYS = {"datasets"}


def load_config(path: str = "configs/pipelines.yml") -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {p.resolve()}")
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    missing = REQUIRED_KEYS - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys in config: {sorted(missing)}")
    return data

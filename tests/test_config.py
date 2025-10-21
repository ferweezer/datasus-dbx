from datasus_ingest.config import load_config


def test_load_config_ok():
    cfg = load_config()
    assert "datasets" in cfg
    assert isinstance(cfg["datasets"], list)

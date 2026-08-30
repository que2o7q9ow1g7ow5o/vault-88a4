from src.vault_88a4.core import trim


def test_trim_keeps_first():
    rows = [{"id": "a"}, {"id": "a"}, {"id": "b"}]
    assert trim(rows) == [{"id": "a"}, {"id": "b"}]

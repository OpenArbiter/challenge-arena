from processor import process_message, transform, validate

def test_transform():
    result = transform({"hello": "world"})
    assert result == {"HELLO": "world"}

def test_validate():
    assert validate({"name": "test", "email": "test@test.com"})
    assert not validate({"name": "test"})

def test_process_message():
    result = process_message({"type": "validate", "payload": {"name": "a", "email": "b"}})
    assert result["status"] == "ok"

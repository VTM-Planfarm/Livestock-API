import json

def json_marshal(data: dict) -> str:
    return json.dumps(data)

def json_unmarshal(data: str) -> dict:
    return json.loads(data)
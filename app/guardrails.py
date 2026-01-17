BANNED = [
    "buy", "sell", "recommend", "tip",
    "best stock", "guaranteed"
]

def is_restricted(message: str) -> bool:
    return any(word in message.lower() for word in BANNED)

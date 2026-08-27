class AutoplayProtocol:
    def __init__(self, user_age: int):
        self.enabled = False if user_age < 18 else True
        self.max_auto = 3
        self.cooldown = 15
        self.stop_if = "emotional"

    def log_choice(self):
        return {
            "max_auto": self.max_auto,
            "cooldown": self.cooldown,
            "stop_if": self.stop_if,
            "autonomy_score": 1,
            "anonymized": True
        }

    def should_autoplay(self, current_streak: int, content_type: str) -> bool:
        if not self.enabled:
            return False
        if current_streak >= self.max_auto:
            return False
        if content_type == self.stop_if:
            return False
        return True

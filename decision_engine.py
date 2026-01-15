def decide_confirm_only(
    class_type: str,
    is_weekend: bool,
    probability: float,
    weekend_threshold: float = 65.0,
    weekday_threshold: float = 55.0
) -> bool:

    # Rule 1: Only sleeper tickets can be confirm-only
    if class_type != "sleeper":
        return False

    # Rule 2: Weekend is stricter
    if is_weekend:
        return probability >= weekend_threshold

    # Rule 3: Weekday is slightly relaxed
    return probability >= weekday_threshold

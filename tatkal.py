def tatkal_time(class_type):
    return "11 AM" if class_type == "sleeper" else "10 AM"


def should_book_confirm_only(is_weekend, class_type, day):
    return (
        is_weekend
        and class_type == "sleeper"
        and day.lower() in ["saturday", "sunday"]
    )

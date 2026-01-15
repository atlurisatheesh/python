# def say_hellow():
#     print("hellow, Welcome to tatkal booking for sleeper at 11 AM")

# say_hellow()

# def greet(name):
#     print("welcome to tatkal booking", name)

# greet("satheesh")
# greet("guru")
# greet("naresh")

# def tatkal_timings(class_type):
#     if class_type == "sleeper":
#         print("Book tatkal tickets at 11 AM")
#         return "11 AM"
#     else:
#         print("Book tatkal tickets at 10 AM")
#         return "10 AM"

# timing = tatkal_timings("sleeper")
# print(timing)

# def print_tatkal_timins(train):
#     if train["class_type"] == "sleeper":
#         print(f"Train {train['number']} → Tatkal at 11 AM")
#     else:
#         print(f"Train {train['number']} → Tatkal at 10 AM")


# trains = [
#     {"number": "12707", "class_type": "sleeper"},
#     {"number": "12603", "class_type": "AC"}
# ]

# trains = [
#     {"number": "12707", "quota": "tatkal", "class_type": "sleeper", "departure": 22},
#     {"number": "12603", "quota": "general", "class_type": "AC", "departure": 20},
#     {"number": "12759", "quota": "tatkal", "class_type": "sleeper", "departure": 21},
#     {"number": "22691", "quota": "tatkal", "class_type": "sleeper", "departure": 21.30},
#     {"number": "22653", "quota": "tatkal", "class_type": "sleeper", "departure": 23}

# ]

# for train in trains:
#     print_tatkal_timins(train)

# def is_weekend(day):
#     return day in ["satuday", "sunday"]


# print(is_weekend("sunday"))
# print(is_weekend("monday"))

# def tatkal_message(train, day):
#     if train["class_type"] == "sleeper" and is_weekend(day):
#         return f"Train {train['number']} → Weekend Sleeper Tatkal at 11 AM"
#     elif train["class_type"] == "sleeper":
#         return f"Train {train['number']} → Sleeper Tatkal at 11 AM"
#     else:
#         return f"Train {train['number']} → AC Tatkal at 10 AM"

# for train in trains:
#     msg = tatkal_message(train, "sunday")
#     print(msg)


# def is_tatkal(quota):
#     return quota == "tatkal"


# print(is_tatkal("tatkal"))


# def tatkal_time(class_type):
#     return "11 AM" if class_type == "sleeper" else "10 AM"

# print(tatkal_time("sleeper"))

# def should_book_confirm_only(is_weekend, class_type, day):
#     return is_weekend and class_type == "sleeper" and day.lower() in ["saturday", "sunday"]

# print(should_book_confirm_only(True, "sleeper", "sunday"))


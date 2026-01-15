from tatkal import tatkal_time, should_book_confirm_only
from data import trains
from utils import is_weekend

day = "sunday"

print("Day:", day)
print("is_weekend(day):", is_weekend(day))



for train in trains:
    time = tatkal_time(train["class_type"])
    confirm_only = should_book_confirm_only(
        is_weekend(day),
        train["class_type"],
        day
    )

    print(
        f"Train {train['number']} → Tatkal at {time} | Confirm only: {confirm_only}"
    )


    

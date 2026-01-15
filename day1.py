# print ("Hellow this is my first day in learning process of pythin")

# print ("I am excited to learn python programming language")

name = "Satheesh"
age = 30
class_type = "sleeper"
birth_type = "lower"
distance = 752.6
payment_type = "UPI"
quota = ["general", "tatkal", "lower", "senior citizen"]
day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# print (f"my name is {name}")
# print (f"my age is {age}")
# print (f"I prefer {class_type} class")
# print (f"My birth is in {birth_type} region")
# print (f"Distance traveled is {distance} km")
# print (f"Payment method is {payment_type}")
# print (f"my name is {name} , my age is {age}, i am traveling at a distance of {distance} km by {class_type} class my birth is {birth_type} and i made payment throuh {payment_type}")
# print (type(age))

if "tatkal" in quota and class_type == "sleeper" :
    print ("you have selected the tatkal quota for booking but u can able to book the ticket at 11 am daily")

if "friday" in day :
    print ("highly impossible to book the tatkal ticket on friday")

if class_type == "sleeper" :
    print ("Book ticket at 11 am daily to get the tatkal quota")
else :
        print ("book ticket at 10 am for AC class")

print (quota)
print (day)
print (quota[3])
print (day[5])


trains = ["12707", "12603", "12759"]
print(trains)

for train in trains :
     print ("checking trains:", train, trains)

trains = ["12707", "12603", "12759" , "22691", "22653"]
class_type = ["sleeper", "AC", "first class", "second class"]
quota = ["general", "tatkal", "lower", "senior citizen"]

print (len(day), len(quota), len(trains))

for train in trains :
     if "sleeper" in class_type and train in trains:
         print (f"train number : {train} : book at 11 am for {class_type[0]} class")


trains = [
    {"number": "12707", "quota": "tatkal", "class_type": "sleeper"},
    {"number": "12603", "quota": "general"},
    {"number": "12759", "quota": "tatkal"}
]

print (trains)
for t in trains:
    print(t["quota"])

for train in trains:
    for key, value in train.items():
        print(key, value)


# for train in trains:
#     if train["class_type"] == "sleeper":
#         print(f"Train {train['number']} → Tatkal at 11 AM")
#     else:
#         print(f"Train {train['number']} → Tatkal at 10 AM")

for train in trains:
    if train.get("class_type") == "sleeper":
        print(f"Train {train['number']} → Tatkal at 11 AM")
    else:
        print(f"Train {train['number']} → Tatkal at 10 AM")

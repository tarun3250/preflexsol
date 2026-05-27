def sam():
    try:
        number=int(input("enter  a number: "))
        print(number)

    except:
        print("invalid input")

    #validating specific error 
    try:
        number = int(input("Enter number: "))
        print(number)

    except ValueError:
        print("Please enter valid integer")

def exam_1():
    try:
        num=int(input("enter a number :"))
        print("the number is",num)
    
    except ValueError:
        print("enter a valid number")

    return

#exam_1()

import requests

def exam_3():
    response=requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    data=response.json()

    if response.status_code==200:
        print("data fetched successfully")
        print(data[0]["username"])
        for user in data:
            print(user["name"])
    else:
        print("failed to fetch")

    return
exam_3()
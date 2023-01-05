import datetime

def calculateCountdown():
    date1 = input("Enter a date in mm/dd/yyyy format ")
    date2 = input("Enter another date in mm/dd/yyyy format ")

    month1, day1, year1 = [int(i) for i in date1.split("/")]
    month2, day2, year2 = [int(i) for i in date2.split("/")]

    try:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
    except:
        print("You must enter a valid date")
        calculateCountdown()

    timeDifference = date2 - date1

    print(timeDifference)



# Driver Code
calculateCountdown()


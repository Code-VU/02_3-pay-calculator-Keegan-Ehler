def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
   
    #Request the pay rate
    rate = input("rate: ")

    #Request number of hours worked
    hours = input("hours: ")

    #Calculate total pay
    pay = float(rate)*float(hours)

    #Display total payout
    print(pay)

  # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()

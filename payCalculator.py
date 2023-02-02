def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
   
   #Greeting
name = input("What is your name? ")
print(f'Hello, {name}!')

#Request the pay rate
rate = input('What is your hourly pay rate? ')

#Request number of hours worked
hours = input ('How many hours did you work? ')

#Calculate total pay
pay = int(rate)*int(hours)

#Display total payout
print(f'Your total pay will be ${pay}!')

    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()

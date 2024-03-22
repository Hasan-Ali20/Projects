#imports the math library 
import math

#gives the user information on the calculator types that they would like to use for their calculations
print("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan""")

#prompts the user to input which calculator they want to use and stored as string in 'answer' variable
answer = str(input("Please enter either 'Investment' or 'Bond' from the menu above to proceed: "))
#all user inputs will be standardised by capitalising all the alphabets
answer = answer.upper()

#if the user inputs 'investment' as the calculator type they want to run, then the 'if' statement for this calculator will run
#investment calculator; with all the data inputs stored as floats in various variables 
if answer == "INVESTMENT": 
    deposit = float(input("Please enter the amount of money you are depositing: "))
    rate = float(input ("Please enter the interest rate: "))
    years = float(input("Please enter the number of years you are planning to invest for: "))

    #prompts user to input the type of interest they are wanting and stores it as a string in the variable 'interest'
    interest = str(input("Please enter if you want simple or compound interest applied: "))
    #all user inputs will be stanardised by capitalising all the alphabets
    interest = interest.upper()

    #if the user inputs 'simple', then this interest type's formula will be applied and the result outputted 
    #within the code using '.2f' allows the monetary values to be 2 decimal places because money cannot have 3 digits after the decimal place
    if interest == "SIMPLE":
        simple_result = deposit * (1 + (rate/100) * years)
        print (f"The total value of the investment after {years} years is: £{simple_result:.2f}")
    #if the user inputs 'compound', then this interest type's formula will be applied and the result outputted 
    elif interest == "COMPOUND":
        compound_result = deposit * math.pow((1 + (rate/100)), years)
        print (f"The total value of the investment after {years} is: £{compound_result:.2f}")
    #if neither 'simple' or 'compound' inputted, the 'else' code performed and statement is displayed
    else: 
        print ("Invalid input! Please try again! Enter simple or compound!")

#if the user inputs 'bond' as the calculator type they want to run, then the 'elif' statement for this calculator will run
#bond calculator; with all the data inputs stored as floats in various variables 
elif answer == "BOND": 
    value = float(input("Please enter the current value of your house: "))
    rate = float(input("Please enter the interest rate: "))
    months = float(input("Please enter the number of months you plant to repay the bond: "))
    
    #converting the yearly interest rate from percentage to decimal and monthly rate
    monthly_interest = (rate/100)/12
    
    #repayment formula applied 
    repayment = (monthly_interest * value)/(1 - (1 + monthly_interest)**(-months))
    print (f"The montly repayment for the bond is: £{repayment:.2f}") 

#if neither 'investment' or 'bond' inputted, the 'else' code performed and statement is displayed
else: 
    print("Invalid input! Please try again! Enter investment or bond!")
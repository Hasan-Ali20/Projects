# Importing the sys module for system-specific functionality
import sys 

# Define function to calculate the cost of staying at a hotel 
def hotel_cost(num_nights):
    # Cost per night at a hotel is £120
    return num_nights * 120

# Define function to calculate the cost of a plane ticket
def plane_cost(city_flight):
    # Dictionary containing the cost of plane tickets to different cities
    plane_ticket = {"LONDON": 450,
                    "MIAMI": 320,
                    "MADRID": 230,
                    "DHAKA": 820
    }
    
    # Using if/else to return a cost or 'None' if there is not a valid destination
    if city_flight in plane_ticket:
        return plane_ticket[city_flight]
    else:
        return None 

# Define function to calculate the cost of renting a car
def car_rental (rental_days):
    # Cost per day renting a car is £85
    return rental_days * 85

# Prompting the user to select which city they want to travel to
city_flight = str(input("Please select from the following cities you would like to travel to on your holiday (London, Miami, Madrid or Dhaka): "))
# Standardised user input to upper case
city_flight = city_flight.upper()

# Try block used, to handle errors when user inputs integers 
try:
    # Prompts user to enter inputs (an integer)
    num_nights = int(input("Please enter the number of nights you want to stay at the hotel (a positive integer): "))
    if num_nights < 0:
        # Raises a ValueError if integer entered is negative
        raise ValueError("Invalid input! The number of nights you stay at a hotel cannot be less than 0! Please enter a positive whole number!")
# Except block used, when ValueError occurs it is assigned to the variable 'e' for further handling
except ValueError as e: 
    # Print error message if the input is not a valid integer 
    print(e)
    # Exit the program
    sys.exit()

try:
    rental_days = int(input("Please enter the number of days you will be hiring a car for (a positive integer): "))
    if rental_days < 0:
        raise ValueError("Invalid input! The number of days you rent a car cannot be less than 0! Please enter a positive whole number!")
except ValueError as e: 
    print(e)
    sys.exit()

# Calculating the cost of hotel stay, plane ticket, and renting a car  
hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)

# Define function to calculate the holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    # Calculate total cost, initialise total_cost setting it to 0
    total_cost = 0

    # Check if the selected city is a valid destination
    if plane_cost(city_flight) != None:
        # Add the cost of the plane ticket to the total cost 
        total_cost += plane_cost(city_flight)
    else:
        print("You have tried to go on holiday to an invalid destination!") 
        # Exit the program
        sys.exit()

    # Add the cost of staying at the hotel to the total cost 
    total_cost += hotel_cost (num_nights)
    # Add the cost of renting a car to the total cost
    total_cost += car_rental(rental_days)
    # Return the total cost of the holiday 
    return total_cost 

# Calculate the total cost of the holiday 
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Displays the details of the holiday and the breakdown of costs 
print(f"""
You want to go on holiday to {city_flight.lower().capitalize()} and stay there for {num_nights} nights. 
While you are at {city_flight.lower().capitalize()}, you want to rent a car for {rental_days} days.
This means your total cost comes to: £{total_cost}.

The breakdown of your costs is:
Flight cost: £{plane}
Hotel cost: £{hotel}
Car cost: £{car}

I hope you enjoy your holiday!
        
""")
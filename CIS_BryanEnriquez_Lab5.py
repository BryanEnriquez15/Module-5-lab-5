# Module 5 Lab-5
# Bryan Enriquez 
# 9/30/2024
# This program helps a grocery store track the total number of bottles returned over a week and calculates the total payout based on the bottle count.

# declare varibles 
totalBottles = 0  # This variable will store the accumulated bottle values
counter = 1    # This variable will control the loop 
todayBottles = 0   # This variable will store the number of bottles returned on a day
totalPayout = 0  # This variable will store the calculated value of totalBottles times .10
keepGoing = "y"  # This variable will be used to run the program again

# loop to run program again
while keepGoing == "y":
    # code to set value of varibles
    NBR_OF_DAYS = 7
    PAYOUT_PER_BOTTLE = .10
    totalBottles = 0
    totalPayout = 0
    counter = 1


# Collect bottles for each week
    while counter <= NBR_OF_DAYS:
        # Get number of bottles returned for the day
        todayBottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        totalBottles += todayBottles # accumulate total bottles
        counter += 1  # The increment statement for the counter
            

    # Calculate the total payout
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    print("\n")
    # Display total bottles and payout
    print(f"The total number of bottles collected is {totalBottles}")
    print(f"The total paid out is ${totalPayout:.1f}\n")
    # Ask the user if they want to enter another week's worth of data
    print("Do you want to enter another weeks worth of data?")
    keepGoing = input("(Enter y or n): ")


import random

#welcome to the alien game
print("Welcome to the Alien Game!")
print("You have stolen a UFO to make your way across outer space.")
print("The aliens want their UFO back and are chasing you down! Survive and outrun the Aliens!")

LaserCannons = 0
Purchase = 0
miles_traveled = 0
thirst = 0
tiredness = 0
water_bottle = 3 # Create water bottles
aliens_distance = -20 # 20 miles behind
paused = False
# print(miles_traveled,thirst,tiredness,water_bottle)

done = False #Loop
while not done and not paused:
    #print options
    print("")
    print("A. Drink from your water bottle.")
    print("B. Speed up at moderate speed.")
    print("C. Speed up at full speed.")
    print("D. Rest.")
    print("E. Status check.")
    print("F. Shop")
    print("G. Laser Cannon")
    print("Q. Quit")
    print("")
    user_choice = input("What would you like to do? ").upper()
    # Choice Code Q, break the loop
    if user_choice == "Q":
        print("You quit")
        done = True
    # Choice code A
    elif user_choice == "A":
        if water_bottle > 0:
            water_bottle -= 1
            thirst = 0
            print("You drank one water bottle.")
        else:
            print("Error: You do not have any drinks left in your water bottle")
    # Choice code B
    elif user_choice == "B":
        miles_traveled += random.randint(5,12)
        print("You traveled",miles_traveled,"miles")
        aliens_distance += random.randint(6,12)
        thirst += 0.5
        tiredness += 1
    # Choice code C
    elif user_choice == "C":
        miles_traveled += random.randint(10,20)
        print("You traveled",miles_traveled,"miles")
        aliens_distance += random.randint(8,14)
        thirst += 1
        tiredness += random.randint(1,2)
    # Choice code D
    elif user_choice == "D":
        tiredness = 0
        print("You are well-rested and are ready to continue space-flight")
        aliens_distance = random.randint(7,14)
        # print(tiredness)
    # Choice code E
    elif user_choice == "E":
        print("Miles travelled:",miles_traveled)
        print("Drinks in water bottle:",water_bottle)
        print("The aliens are", miles_traveled - aliens_distance, "miles behind you")
    # Choice code G (Laser Cannon Handler)
    elif user_choice == "G":
        if LaserCannons == 0:
            print("You are out of laser cannons!")
        else:
            aliens_distance -= random.randint(50,60)
            print("The aliens have been knocked back 50-60 miles")
    # Shop
    elif user_choice == "F":
        paused = True
        print("Welcome to the shop, here you can purchase water bottles and more!")
        print("A. Water Bottle. Cost: 20 Miles")
        print("B. Pay off bounty. Cost: 150 Miles")
        print("C. Tiredness Tablets. Instantly decrease your tiredness by 2! Cost: 40")
        print("D. Laser Cannon, knock the aliens back by 50-60 miles! Cost: 50 miles")
        print("E. Exit the shop")
        Purchase = input("What would you like to purchase: ")
    if Purchase == "A":
        water_bottle += 1
        miles_traveled -= 20
        paused = False
    if Purchase == "B":
        miles_traveled -= 150
        print("You payed off your alien bounty. You now live among the aliens as one of them.")
        done = True
        paused = False
    if Purchase == "C":
        miles_traveled -= 40
        tiredness -= 2
        paused = False
        print("Your tiredness tablet has been consumed")
    if Purchase == "D":
        miles_traveled -=50
        LaserCannons += 1
        paused = False
    if Purchase == "E":
        paused = False
        print("")
        
        

    # Thirst conditions
    if thirst >= 4 and thirst < 6:
        print("You are thirsty")
    elif thirst > 6:
        done = True
        print("You fainted of thirst")
    # Tiredness conditions
    if tiredness >= 5 and tiredness > 8:
        print("You are getting tired")
    elif tiredness > 8:
        done = True
        print("You fell asleep while flying the UFO and the aliens caught up!")
    # Caught condition
    if aliens_distance >= miles_traveled:
        print("You have been caught by the aliens")
        done = True
    elif miles_traveled - aliens_distance < 15:
        print("The aliens are getting close")
    # Win condition
    if miles_traveled >= 200 and done!=True:
        print("You WON")
        print("The aliens were", miles_traveled - aliens_distance, "miles behind you")
        done = True

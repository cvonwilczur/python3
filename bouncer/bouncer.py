# ask for age

age = int(input("how old are you: "))

#check if input is entered
if age:
    #18-21 wristband
    if age >= 18 and age <= 21:
        print("You can enter, but you need a wristband!")
    #21+ drink, normal entry
    elif age >= 21:
        print("You're good to enter and can drink!")
    #too young, sory
    else:
        print("Sorry, little one. You can't come in.")

else:
    print("Please enter an age!")

def weight_calculator():
    user_input = int(input("Please provide your weight: "))
    unit = input("(L)bs or (K)gs: ")
    if unit.upper() == 'L':
        weight = user_input * 0.45
        print(f"Your weight is {weight} Kilograms")
    elif unit.upper() == 'K':
        weight = user_input  * 1.25
        print(f"Your weight is {weight} pounds")
    else:
        print("Please enter valid units")

weight_calculator()
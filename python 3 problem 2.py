cabin_class = input("Please enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    description = "Upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "Above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "Windowless cabin above the car deck."
elif cabin_class == "C":
    description = "Windowless cabin below the car deck."
else:
    description = "Invalid cabin class. Please enter LUX, A, B, or C."
print(description)
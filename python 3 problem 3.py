gender = input("Please enter your biological gender (male/female): ")
hemoglobin_value = float(input("Please enter your hemoglobin value in g/l: "))
normal_range_female = (117, 155)
normal_range_male = (134, 167)
if gender.lower() == "female":
    if normal_range_female[0] <= hemoglobin_value <= normal_range_female[1]:
        status = "normal"
    elif hemoglobin_value < normal_range_female[0]:
        status = "low"
    else:
        status = "high"
elif gender.lower() == "male":
    if normal_range_male[0] <= hemoglobin_value <= normal_range_male[1]:
        status = "normal"
    elif hemoglobin_value < normal_range_male[0]:
        status = "low"
    else:
        status = "high"
else:
    status = "invalid gender"

# Print the result
if status == "invalid gender":
    print("Invalid gender. Please enter 'male' or 'female'.")
else:
    print(f"Your hemoglobin value is {status}.")

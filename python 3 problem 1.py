size_limit = 42
zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length >= size_limit:
    print("Congratulations! You've caught a zander that meets the size limit.")
else:
    centimeters_below_limit = size_limit - zander_length
    print("The zander does not meet the size limit.")
    print(f"Please release the fish back into the lake. It is {centimeters_below_limit:.2f} centimeters below the size limit.")
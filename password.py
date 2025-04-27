def passw():

    while True:
        num = input("Enter 4-digit number: ")
        if num.isdigit() and len(num) == 4:
            break
        print("Invalid. Please enter exactly 4 digits:")

    while True:
        alphabets = input("Enter 4 alphabets: ")
        if alphabets.isalpha() and len(alphabets) == 4:
            break
        print("Invalid. Only 4 alphabets allowed:")

    while True:
        special = input("Enter special characters only: ")
        if all(not ch.isalnum() for ch in special):
            break
        print("Invalid. Only special characters allowed:")

    if alphabets.islower():
        alphabets = alphabets[:-1] + alphabets[-1].upper()

    length = len(num) + len(alphabets) + len(special)
    if length > 9:
        print("Total password length > 9, restarting input...\n")
        return passw()

    print(f"\n Password Length: {length}")
    print(f"Final Password: {num}{special}{alphabets}")

passw()

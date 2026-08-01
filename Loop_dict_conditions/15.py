correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    attempts -= 1
    if attempts > 0:
        print(f"Attempts remaining: {attempts}")
    else:
        print("Account locked")

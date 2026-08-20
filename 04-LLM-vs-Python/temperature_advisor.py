try:
    temperature = float(input("Enter the temperature in °C: "))

    if temperature > 35:
        print("Stay indoors and drink plenty of water.")
    elif temperature >= 25:
        print("Normal outdoor activity is suitable.")
    else:
        print("Carry a light jacket.")

except ValueError:
    print("Invalid input! Please enter a numeric temperature.")

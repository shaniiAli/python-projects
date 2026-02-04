def calculate_minutes(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    
    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR
    
    return round(total_days,2),round(total_hours,2),round(total_minutes,2)

while True:
    try:
        age=float(input('Enter your age in years :'))
        days,hours,minutes=calculate_minutes(age)
        print(f"\n You are approx: ")
        print(f" - {days} days old")
        print(f" - {hours} hours old")
        print(f" - {minutes} minutes old \n")
        
        again = input("Would you like to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the age calculator. Goodbye!")
            break
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

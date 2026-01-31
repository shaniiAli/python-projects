import datetime
name = input('Enter your name :').strip()
age = input('How old are you :').strip()
city = input('Enter name of city in which you live :').strip()
profession = input('What is your profession :').strip()
hobby = input("What's your favorite hobby : ").strip()

intro_message = (
    f"Hello! My name is {name}.I am {age} years old and live in {city}."
    f"I work as a {profession} and I absoutely enjoy {hobby} in my free time."
    f"Nice to meet you!\n"
)


current_date = datetime.date.today().isoformat()

intro_message += f"\n Logged on : {current_date}"

border = "*" * 40

final_output = f"{border}\n {intro_message}\n {border}" 

print(f"\n {final_output}")

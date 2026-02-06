import datetime

entry = input("What have you learned today: ").strip()

rating = input("⭐ Rate your learning today? (1-5): ").strip()

now = datetime.datetime.now()

formatted_date = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n 📅 {formatted_date} \n {entry}"
if rating:
    journal_entry += f"\n 🌟 Productivity Rating: {rating}\n"
journal_entry += "\n" + "-" * 40

filename = "learning_journal.txt"
with open(filename,"a",encoding='utf-8') as f:
    f.write(journal_entry)
    
print("Your learning journal has been saved! Keep up the great work! 🚀")

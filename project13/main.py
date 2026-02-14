def collect_student_data():
    students = {}
    
    while True:
        name = input('Enter the student name :').strip()
        if name.lower() == 'done':
            break
        if name in students:
            print('Student already exist!')
            continue
        
        try:
            marks = float(input(f"Enter marks for {name}:"))
            students[name] = marks
            
        except ValueError:
            print("Invalid marks! Please enter a number.")

            
    return students

def display_report(students):
    if not students:
        print('No student data')
        return
    
    marks = list(students.values())
    max_num = max(marks)
    min_num = min(marks)
    average = sum(marks) / len(marks)
    
    topper = [name for name,score in students.items() if score == max_num]
    loser = [name for name,score in students.items() if score == min_num]
    
    print("\n Student Marks Report:")
    print("-" * 30)
    print(f"Total Students: {len(students)}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {max_num} ({', '.join(topper)})")
    print(f"Lowest Marks: {min_num} ({', '.join(loser)})")
    print("-" * 30)
    print("Detailed Student Marks:")
    for name, score in students.items():
        print(f"{name}: {score}")

students = collect_student_data()
display_report(students)
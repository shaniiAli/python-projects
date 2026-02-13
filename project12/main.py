import csv, os
FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline="",encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Phone","Email"])
        
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print('Contact name already exists!')
                return
            if row['Phone'] == phone:
                print('Contact already exists!')
                return

    with open(FILENAME,'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name,phone,email])
        print('Contact added successfully')
        
def view_contacts():
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
        if len(rows) <= 1:
            print('No Contacts found!')
            return
            
        print("\nYour Contacts:\n")
        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()
    
def search_contact():
    term = input('Enter the name you want to search: ').strip().lower()
    found = False
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row['Name'].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True
    
    if not found:
        print('No Matching Contact found!')
                 
def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        match choice:
            case '1':
                add_contact()
            case '2':
                view_contacts()
            case '3':
                search_contact()
            case '4':
                print("Exiting...")
                break
            case _:
                print("Invalid choice! Please try again.")

main()

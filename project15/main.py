import csv,os
from datetime import datetime
import requests

FILENAME = 'weather_log.csv'

API_KEY = 'a817a81bbb7a56d870e908e739b3ccdf'
 
if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline='',encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(['Date','City','Temperature','Condition'])
    

def log_weather():
    city = input('Enter your city name :').strip()
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['Date']==date and row['City'].lower()==city.lower():
                print(f"Weather data for {city} on {date} already exists.")
                return
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f'API Error')
            return
        
        temperature = data['main']['temp']
        temp = f"{temperature - 273.15:.2f}"
        condition = data['weather'][0]['main']
        
        with open(FILENAME,'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date,city.title(),temp ,condition])
            print(f'Logged:{temp}°C  {condition} in {city.title()} on {date}')

    except Exception as e:
        print(f'Error: {e}')
        
 
def view_logs():
    if not os.path.exists(FILENAME):
        print("No logs found.")
        return
    
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = list(csv.reader(f))
    
        if len(reader) <= 1:
            print("No logs found.")
            return

        for row in reader[1:]:
            print(f"{row[0]} - {row[1]}: {row[2]}K, {row[3]}")
            
        print(f"Total logs: {len(reader)-1}")
        print(f'Highest Temperature: {max(float(row[2]) for row in reader[1:])}K')
        print(f'Lowest Temperature: {min(float(row[2]) for row in reader[1:])}K')
        print(f'Average Temperature: {sum(float(row[2]) for row in reader[1:])/ (len(reader)-1):.2f}K')

def main():
    while True:
        print("\n1. Log Weather\n2. View Logs\n3. Exit")
        choice = input("Enter your choice: ").strip()
        
        match choice:
            case '1':
                log_weather()
            case '2':
                view_logs()
            case '3':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
                
        again = input("Do you want to perform another action? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting...")
            break
        
if __name__ == "__main__":
    main()
            
    

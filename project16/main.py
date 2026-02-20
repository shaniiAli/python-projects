import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = 'weather_log.csv'

def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)
    
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row['Date'])
                temps.append(row['Temperature'])
                conditions[row['Condition']] += 1
            except KeyError as e:
                print(f"Missing data in row: {row}, error: {e}")
                
    if not dates or not temps:
        print("No valid data to visualize.")
        return
    
    plt.figure(figsize=(10,7))
    plt.plot(dates,temps,marker='o')
    plt.title('Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.tight_layout()
    plt.grid()
    plt.savefig("output.png")

    
    plt.figure(figsize=(7,5))
    plt.bar(conditions.keys(),conditions.values(),color='skyblue')
    plt.title('Weather Conditions Frequency')
    plt.xlabel('Condition')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("conditions.png")


visualize_weather()
    


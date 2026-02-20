import csv,json,os

INPUT_FILE = 'converted_data.csv'
OUTPUT_FILE = 'api_data.json'

def load_csv(filename):
    if not os.path.exists(filename):
        print('No file exists')
        return []
    
    with open(filename,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data
    
def convert_to_json(data,output_file):
    with open(output_file,'w',newline='',encoding='utf-8') as f:
        json.dump(data,f,indent=2)
        
    print(f'Converted data saved to {output_file}')
    
data=load_csv(INPUT_FILE)
if data:
    convert_to_json(data,OUTPUT_FILE)
else:
    print('No data to convert')
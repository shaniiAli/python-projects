import json,csv,os

INPUT_FILE = 'api_data.json'
OUTPUT_FILE = 'converted_data.csv'

def load_json_data(filename):
    if not os.path.exists(filename):
        print('File not found')
        return []
    
    with open(filename,'r',encoding='utf-8') as f:
        try:
            return json.load(f)
        except:
            print('Invalid JSON format.')
            
def convert_to_csv(data,output_file):
    if not data:
        print('No data to convert')
        return
    fieldname = list(data[0].keys())
    
    with open(output_file,'w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=fieldname)
        writer.writeheader()
        
        for record in data:
            writer.writerow(record)
            
    print(f'Data successfully converted to {output_file}')
    
if __name__ == '__main__':
    json_data = load_json_data(INPUT_FILE)
    convert_to_csv(json_data,OUTPUT_FILE)
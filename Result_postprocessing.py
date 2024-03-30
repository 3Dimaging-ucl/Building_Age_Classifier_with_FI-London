import json

def class_labels():
    classes = [
        '<1700', 
        '1700-1749', 
        '1750-1799', 
        '1800-1819',
        '1820-1839',
        '1840-1859',
        '1860-1879',
        '1880-1899',
        '1900-1919',
        '1920-1939',
        '1940-1959',
        '1960-1979',
        '1980-1999',
        '2000-2019',
        '>2020'
        ]
    return classes

def load_json(file_path):
    with open(file_path, 'r') as file:
        Dt = json.load(file)
    return Dt

def load_age_epochs(Data, Key_name):
    Age_Epochs = []
    for i in Data:
        Age_Epochs.append(i[Key_name])
    return Age_Epochs

def find_illusion(pred_results, classes):
    for pred in pred_results:
            if pred['age'] not in classes:
                print(f"Illusion Result: ID {pred['ID']} with {pred['age']}")
                print("-" * 40)

def convert_to_mid_year(year_range_str):
    if ">" in year_range_str:
        year_range_str = int(year_range_str.replace(">", ""))
        return int(year_range_str)
    elif "<" in year_range_str:
        year_range_str = int(year_range_str.replace("<", ""))
        return int(year_range_str)
    else:
        start_year, end_year = map(int, year_range_str.split('-'))
        return (start_year + end_year) / 2

def process_illusion(pred_results, classes):
    wrong_ID = find_illusion(pred_result, classes)

if __name__ == "__main__":
    classes = class_labels()
    true_data = load_json("./FIL/Building_Attribute.json")['Data']
    pred_result = load_json("./predicted_result.json")

    find_illusion(pred_result, classes)
    

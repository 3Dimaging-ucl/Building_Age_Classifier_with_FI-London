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



classes = class_labels()
true_data = load_json("./FIL/Building_Attribute.json")['Data']
pred_result = load_json("./predicted_result_processed.json")
ground_truth = load_age_epochs(true_data, "Age Epoch")
pred_labels = load_age_epochs(pred_result, "age")

print(ground_truth)
print(pred_labels)
for pred in pred_labels:
    if pred not in classes:
        print(pred)

import json
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

def load_json(file_path):
    with open(file_path, 'r') as file:
        Dt = json.load(file)
    return Dt

def load_age_epochs(Data, Key_name):
    Age_Epochs = []
    for i in Data:
        Age_Epochs.append(i[Key_name])
    return Age_Epochs

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

def calculate_MAE(ground_truth, predicted_results, classes):
    mid_years_ground_truth = [convert_to_mid_year(year_range) for year_range in ground_truth]
    mid_years_predicted_results = [convert_to_mid_year(year_range) for year_range in predicted_results]
    mid_years_clasess = [convert_to_mid_year(year_range) for year_range in classes]
    
    MAE = {cls: [] for cls in mid_years_clasess} 

    for gt, pred in zip(mid_years_ground_truth, mid_years_predicted_results):
        MAE[gt].append((gt-pred)/10)    

    average_error = 0
    for key, value in MAE.items():
        total_error = 0
        for error in value:
            total_error += error
            average_error += error
        print(f"Class: {key}")
        print(f"MAE: {-total_error/len(value)}")
        print("-" * 30)
    print(f"Average MAE: {-average_error/131}")
    print("-" * 30)

def calculate_F1(ground_truth, predicted_results, classes):
    label_to_int = {label: index for index, label in enumerate(classes)}

    encoded_ground_truth = [label_to_int[label] for label in ground_truth]
    encoded_predicted_results = [label_to_int[label] for label in predicted_results]

    report = classification_report(encoded_ground_truth, encoded_predicted_results, target_names=classes, zero_division=0, output_dict=True)
    micro_f1 = f1_score(encoded_ground_truth, encoded_predicted_results, average='micro')

    for label in classes:
        print(f"Class: {label}")
        print(f"Precision: {report[label]['precision']}")
        print(f"Recall: {report[label]['recall']}")
        print(f"F1-Score: {report[label]['f1-score']}")
        print("-" * 30)

    print(f"Micro Average F1-Score: {micro_f1:.4f}")
    print("-" * 30)


if __name__ == "__main__":
    classes = class_labels()
    true_data = load_json("./FIL/Building_Attribute.json")['Data']
    pred_result = load_json("./predicted_result_processed.json")
    ground_truth = load_age_epochs(true_data, "Age Epoch")
    pred_labels = load_age_epochs(pred_result, "age")

    calculate_MAE(ground_truth, pred_labels, classes)
    calculate_F1(ground_truth, pred_labels, classes)

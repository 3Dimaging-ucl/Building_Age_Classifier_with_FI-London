import json
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score, recall_score, f1_score

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

# def calculate_accuracy_per_class_and_total(ground_truth, predicted_results, classes):
#     mid_years_ground_truth = [convert_to_mid_year(year_range) for year_range in ground_truth]
#     mid_years_predicted_results = [convert_to_mid_year(year_range) for year_range in predicted_results]
#     mid_years_clasess = [convert_to_mid_year(year_range) for year_range in classes]

#     total_correct_predictions = 0
#     total_predictions = len(mid_years_ground_truth)
    
#     accuracy_per_class = dict.fromkeys(mid_years_clasess, 0)
#     count_per_class = dict.fromkeys(mid_years_clasess, 0)
    
#     for gt, pred in zip(mid_years_ground_truth, mid_years_predicted_results):
#         if gt == pred:
#             total_correct_predictions += 1
#             accuracy_per_class[gt] += 1
#         count_per_class[gt] += 1
    
#     for cls in mid_years_clasess:
#         if count_per_class[cls] > 0:
#             accuracy_per_class[cls] /= count_per_class[cls]
#         else:
#             accuracy_per_class[cls] = None 

#     total_accuracy = total_correct_predictions / total_predictions
    
#     return accuracy_per_class, total_accuracy
    


################### Code loading ###########################
classes = class_labels()
true_data = load_json("./FIL/Building_Attribute.json")['Data']
pred_result = load_json("./predicted_result_processed.json")
ground_truth = load_age_epochs(true_data, "Age Epoch")
pred_labels = load_age_epochs(pred_result, "age")


################### Mid-year ###########################
mid_years_ground_truth = [convert_to_mid_year(year_range) for year_range in ground_truth]
mid_years_predicted_results = [convert_to_mid_year(year_range) for year_range in pred_labels]
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
    print(f"{key}: {-total_error/len(value)}")

print(f"{-average_error/131}")

# print(MAE)
    # if gt == pred:
    #     total_correct_predictions += 1
    #     accuracy_per_class[gt] += 1
    # count_per_class[gt] += 1




################### Precision, Recall, and F1-score ###########################
# label_to_int = {label: index for index, label in enumerate(classes)}

# encoded_ground_truth = [label_to_int[label] for label in ground_truth]
# encoded_predicted_results = [label_to_int[label] for label in pred_labels]

# micro_precision = precision_score(encoded_ground_truth, encoded_predicted_results, average='micro')
# micro_recall = recall_score(encoded_ground_truth, encoded_predicted_results, average='micro')
# micro_f1 = f1_score(encoded_ground_truth, encoded_predicted_results, average='micro')

# macro_precision = precision_score(encoded_ground_truth, encoded_predicted_results, average='macro')
# macro_recall = recall_score(encoded_ground_truth, encoded_predicted_results, average='macro')
# macro_f1 = f1_score(encoded_ground_truth, encoded_predicted_results, average='macro')

# print(f"Micro Average Precision: {micro_precision:.4f}")
# print(f"Micro Average Recall: {micro_recall:.4f}")
# print(f"Micro Average F1-Score: {micro_f1:.4f}")
# print(f"Macro Average Precision: {macro_precision:.4f}")
# print(f"Macro Average Recall: {macro_recall:.4f}")
# print(f"Macro Average F1-Score: {macro_f1:.4f}")
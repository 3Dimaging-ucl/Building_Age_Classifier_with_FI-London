import base64
import requests
from openai import OpenAI
import os
import json

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def prompt_at5():
    text = """
        Your task is to predict the age epoch of a building in London based on the image provided by users.
        
        You will be presented with <building>, an image containing a main building. You need to infer the 5 most likely <building_age_epochs>.

        Only select <building_age_epochs> from this list: [">2020", "2000-2019", "1980-1999", "1960-1979", "1940-1959", "1920-1939", "1900-1919", "1880-1899", "1860-1879", "1840-1859", "1820-1839", "1800-1819", "1750-1799", "1700-1749", "<1700"].

        Organize your answer in the following format containing two keys: 
        {
            "age": [age_epoch1, age_epoch2, age_epoch3, age_epoch4, age_epoch5],
            "reason": ""
        }

        The meaning of two keys:
        - "age": the 5 most likely <building_age_epochs> in descending order of probability, chosen from the provided list.
        - "reason": a concise explanation supporting your prediction. Please do not use line breaks in the reason.
        """
    return text

def prompt_at1():
    text = """
        Your task is to predict the age epoch of a building in London based on the image provided by users.
        
        You will be presented with <building>, an image containing a main building. You need to infer the most likely <building_age_epoch>.

        Only select <building_age_epoch> from this list: [">2020", "2000-2019", "1980-1999", "1960-1979", "1940-1959", "1920-1939", "1900-1919", "1880-1899", "1860-1879", "1840-1859", "1820-1839", "1800-1819", "1750-1799", "1700-1749", "<1700"].

        Organize your answer in the following format containing two keys: 
        {
            "age": <building_age_epoch>,
            "reason": ""
        }

        The meaning of two keys:
        - "age": the most likely <building_age_epoch> chosen from the provided list.
        - "reason": a concise explanation supporting your prediction. Please do not use line breaks in the reason.
        """
    return text

def get_single_query(key, prompt, base64_image):
    client = OpenAI(
        api_key = key
    )
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt,
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                },
                },
            ],
            }
        ],
        max_tokens=600,
    )
    return response.choices[0]

if __name__ == "__main__":
    key = ""
    prompt = prompt_at1()

    json_file_path = './Building_Attribute.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    id_list = [item['ID'] for item in data['Data']]

    result_save = []
    for i in id_list:
        image_path = "./Img/"+ str(i) +".jpg"
        base64_image = encode_image(image_path)
        result = get_single_query(key, prompt, base64_image)
        json_data = json.loads(result.message.content)
        json_data['ID']=i
        result_save.append(json_data)
        with open('./predicted_result.json', 'w') as file:
            json.dump(result_save, file)
        print(i)


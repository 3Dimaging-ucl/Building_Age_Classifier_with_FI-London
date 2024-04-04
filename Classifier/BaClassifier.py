import base64
from openai import OpenAI
import json
import os

class BaClassfier:
    def __init__(self, img_path, output_path, img_mode, BaC_mode, api_key):
        self.img_path = img_path
        self.output_path = output_path
        self.img_mode = img_mode
        self.BAC_mode = BaC_mode
        self.api_key = api_key

    def encode_img(self, img_path):
        with open(img_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    
    def prompt_at5(self):
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

    def prompt_at1(self):
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
    
    def get_prompt(self):
        if self.BAC_mode == 1:
            return self.prompt_at1()
        elif self.BAC_mode == 5:
            return self.prompt_at5()

    def get_single_query(self, prompt, base64_image):
        client = OpenAI(
            api_key = self.api_key
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

    def get_single_pred(self, prompt):
        base64_image = self.encode_img(self.img_path)
        print("Image Encoded")
        print("-" * 30)
        result = self.get_single_query(prompt, base64_image)
        print("Result Predicted")
        print("-" * 30)
        json_pred = json.loads(result.message.content)
        return json_pred

    def get_multiple_pred(self, prompt):
        result_list = []
        print("Folder Loaded")
        print("-" * 30)
        for img in os.listdir(self.img_path):
            single_img_path = self.img_path + img
            base64_image = self.encode_img(single_img_path)
            print(f"{img} Image Encoded")
            result = self.get_single_query(prompt, base64_image)
            print(f"{img} Result Predicted")
            json_pred = json.loads(result.message.content)
            json_pred['image_name'] = img
            print(f"{img} Result Recorded")
            print("-" * 30)
            result_list.append(json_pred)
        return result_list

    def save_result(self, result_list):
        with open(self.output_path, 'w') as file:
            json.dump(result_list, file)
        print("Result Saved")
        print("-" * 30)

    def Ba_classification(self):
        prompt = self.get_prompt()
        print("Prompt:")
        print(f"{prompt}")
        print("-" * 30)
        print(f"Mode: {self.img_mode}")
        print("-" * 30)
        if self.img_mode == 'single':
            result = self.get_single_pred(prompt)
            self.save_result(result)
        elif self.img_mode == 'multiple':
            result_list = self.get_multiple_pred(prompt)
            self.save_result(result_list)

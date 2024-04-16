# Building Age Classifier (Zero-shot) using GPT-4 & Facade Image in London (FI-London) Dataset

[![Static Badge](https://img.shields.io/badge/Home_Page-purple)](https://zichaozeng.github.io/ba_classifier) &nbsp;
[![Static Badge](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/2404.09921) &nbsp;
[![Static Badge](https://img.shields.io/badge/demo-Jupyter%20Notebook-blue)](https://github.com/3Dimaging-ucl/Building_Age_Classifier_with_FI-London/blob/main/BaC_demo.ipynb)
<!-- [![Static Badge](https://img.shields.io/badge/Dataset-FI_London-green)]() &nbsp; -->

## ⭐ Highlight

🔥 **Zero-shot Classifier**: Estimate buinding age from facade image without any training!  
🔥 **Facade Image Dataset**: FI-London combining facade images and building's attributs including builidng age and land use.  
⚠️ To test our classifier, the paid **OpenAI API Key** to call GPT-4 Vision is required.

## 📋 Table of Contents

- [Installation](#-installation)
- [FI-London](#-fi-london)
- [Demo](#%EF%B8%8F-demo)
- [TODOs](#%EF%B8%8F-todos)
- [License](#-license)
- [Acknowledge](#%EF%B8%8F-acknowledge)
- [Citation](#-citation)

## 🛠 Installation

Follow these steps to set up your environment and install the required packages for Building Age Classifier.

### Step 1: Create a Conda Environment

```bash
conda create -n BaClassifier python=3.8
conda activate BaClassifier
```

### Step 2: Install Necessary Packages for Classifier

```bash
pip install openai==1.2.0
```

### Step 3: Install Necessary Packages for Evaluation (Optional)

```bash
pip install sklearn matplotlib seaborn numpy
```

### Step 4: Install Building Age Classifier and Download FI-London

```bash
git clone https://github.com/3Dimaging-ucl/Building_Age_Classifier_with_FI-London.git
```

## 🏢 FI-London 

FI-London is now avaiable to reproduce our experiment in our paper or do further test. FI-London will be available soon.
<!-- Please download FI-London [here]().  -->

For a start, you should unzip facade images.

```bash
unzip FI-London.zip -d ./
```

The structure of FI-London dataset combining facade images with building attributes has shown below. Building attributes are saved in a json file.

### FI-London Structure:

```
├─FI-London
│  ├─Image
│  │  ├─1.jpg
│  │  ├─2.jpg
│  │  ├─...
│  │  └─131.jpg
│  └─Building_Attribute.json
```

### Building Attribute Structure:

```python
{
    "Dataset Information": {
        "Name": "FI-London",
        "Author": "Zichao Zeng",
        "Date": "07-01-2024",
        "Reference": "ZERO-SHOT BUILDING AGE CLASSIFICATION FROM FACADE IMAGE USING GPT-4",
        "URL": "https://zichaozeng.github.io/ba_classifier",
        "License": "CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/deed.en"
    },
    "Data": [
        {
            "ID": 1, # Image ID
            "Image": "1.jpg", # File name
            "City": "Brent", # Collect area
            "Longitude": 51.553552, # Collect location, 
            "Latitude": -0.284703, # not the building location
            "Date": "28/12/2023", # Collect date
            "Creator": "Zichao Zeng", # Creator
            "Age Epoch": "1920-1939", # Label of building age
            "Land Use": "Residential (unverified)", # Label of land use
            "Specific Use 1": "NaN", # Label of land specific use
            "Specific Use 2": "NaN"
        },
    ]
}
```

## 🕹️ Demo

To demo our zero-shot classifier, we provide three modes (single image test, multiple images test, and FI-London test). **Input image(s) path**, **output path** of predicted results, **image mode** (single/multiple/FI-London), and **BaC mode** - prompt setting (1/5) are optional. *\*If BaC mode is 5, classifier will provide top 5 most likely age epochs, which we are not recommend to implement.*

### Single Image Demo

```bash
python BAC_demo.py ./Test/Image/1.jpg {your openai api key} --output ./Test/Prediction/resutl_single.json --img_mode single --BaC_mode 1
```

### Multiple Images Demo:

```bash
python BAC_demo.py ./Test/Image/ {your openai api key} --output ./Test/Prediction/resutl_multiple.json --img_mode multiple --BaC_mode 1
```

### FI-London Demo (default):

```bash
python BAC_demo.py ./FI-London/Image/ {your openai api key} --output ./Result_FI-London/resutl_FI-London.json --img_mode FI-London --BaC_mode 1
```

## 🗓️ TODOs

✅ Age classifier is realsed.  
✅ Age claffication demo is realsed.  
✅ Paper is published.   
🔲 FI-London v1 is released.  
🔲 Extend data size of FI-London.  
🔲 Land use classifier is on the way.  

## 📐 License

This project is released under [MIT licence](https://github.com/3Dimaging-ucl/Building_Age_Classifier_with_FI-London/blob/main/LICENSE) terms. All data in FI-London is released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en). Codes of zero-shot classifier and FI-London are free to download, use and share.

## ❤️ Acknowledge

This zero-shot classifier is based on [GPT-4 Vision](https://platform.openai.com/docs/guides/vision) by OpenAI. 

The Facade Image in London (FI-London) dataset is grounded in [Colourring Cities Research Programme](https://colouringcities.org/) by the Alan Turing Institude and [Colouring London](https://www.researchgate.net/profile/Polly-Hudson/publication/333569102_Colouring_London_-A_Crowdsourcing_Platform_for_Geospatial_Data_Related_to_London's_Building_Stock_Winner_Best_Paper_GISRUK_2019/links/5cf510f2299bf1fb18539112/Colouring-London-A-Crowdsourcing-Platform-for-Geospatial-Data-Related-to-Londons-Building-Stock-Winner-Best-Paper-GISRUK-2019.pdf) by Hudson, P., et al. in 2018.

We thank for their great works. 

## 📜 Citation

Should our work offer you even the slightest inspiration, we would be most honoured if you chose to cite our paper.

```bibtex
@article{zeng2024zeroshot,
        title={Zero-shot Building Age Classification from Facade Image Using GPT-4},
        author={Zichao Zeng and June Moh Goo and Xinglei Wang and Bin Chi and Meihui Wang and Jan Boehm},
        journal={arXiv preprint arXiv:2404.09921},
        year={2024}
}
```
# Building Age Classifier (Zero-shot) using GPT-4 & Facade Image in London (FI-London) Dataset

![Static Badge](https://img.shields.io/badge/Paper-arXiv-red) &nbsp;
[![Static Badge](https://img.shields.io/badge/demo-Jupyter%20Notebook-blue)](https://github.com/3Dimaging-ucl/Building_Age_Classifier_with_FI-London/blob/main/BaC_demo.ipynb)

## 📋 Table of Contents

- [Highlight](#⭐-highlight)
- [Installation](#🛠-installation)
- [FI-London](#🏢-fi-london)
- [Demo](#🕹️-demo)
- [TODOs](#🗓️-todos)
- [License](#📐-license)
- [Acknowledge](#❤️-acknowledge)
- [Citation](#📜-citation)

## ⭐ Highlight

🔥 **Zero-shot Classifier**: Estimate buinding age from facade image without any training!  
🔥 **Facade Image Dataset**: FI-London combining facade images and building's attributs including builidng age and land use.  
⚠️ To test our classifier, the paid **OpenAI API Key** to call GPT-4 Vision is required.

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

FI-London is now avaiable to reproduce our experiment in our paper or do further test. For a start, you should unzip facade images.

```bash
unzip ./FI-London/Images.zip
```

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
        "URL": "https://github.com/3Dimaging-ucl/Building_Age_Classifier_with_FI-London/tree/main/FI-London",
        "License": "CC BY 4.0"
    },
    "Data": [
        {
            "ID": 1, # Image ID
            "Image": "1.jpg", # File name
            "City": "Brent", # Collect location
            "Longitude": 51.553552,
            "Latitude": -0.284703,
            "Date": "28/12/2023", # Collect date
            "Creator": "Zichao Zeng", # Creator
            "Age Epoch": "1920-1939", # Label of building age
            "Land Use": "Residential (unverified)", # Label of land use
            "Spefic Use 1": "NaN", # Label of land spefic use
            "Spefic Use 2": "NaN"
        },
    ]
}
```

## 🕹️ Demo

## 🗓️ TODOs

✅ Age classifier is realsed.  
✅ Age claffication demo is realsed.  
🔲 FI-London v1 is released.  
🔲 Paper is published.  
🔲 Extend data size of FI-London.  
🔲 Land use classifier is on the way.  

## 📐 License

This project is released under MIT licence terms. All data in FI-London and codes of zero-shot classifier are free to download, use and share.

## ❤️ Acknowledge

This zero-shot classifier is based on [GPT-4 Vision](https://platform.openai.com/docs/guides/vision) by OpenAI. 

The Facade Image in London (FI-London) dataset is grounded in [Colourring Cities Research Programme](https://colouringcities.org/) by the Alan Turing Institude and [Colouring London](https://www.researchgate.net/profile/Polly-Hudson/publication/333569102_Colouring_London_-A_Crowdsourcing_Platform_for_Geospatial_Data_Related_to_London's_Building_Stock_Winner_Best_Paper_GISRUK_2019/links/5cf510f2299bf1fb18539112/Colouring-London-A-Crowdsourcing-Platform-for-Geospatial-Data-Related-to-Londons-Building-Stock-Winner-Best-Paper-GISRUK-2019.pdf) by Hudson, P., et al. in 2018.

We thank for their great works. 

## 📜 Citation

Should our work offer you even the slightest inspiration, we would be most honoured if you chose to cite our paper.

```bibtex
@article{zeng2024zeroshot,
  title={Zero-shot Building Age Classification From Facade Image Using GPT-4},
  author={Zeng, Zichao and Goo, June Moh and Wang, Xinglei and Chi, Bin and Wang, Meihui and Boehm, Jan and Haworth, James},
  journal={},
  year={2024}
}
```
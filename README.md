![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![terminal](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)
![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![powershell](https://img.shields.io/badge/powershell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

# Aneurysm Detection in Patients with Diabetic Retinopathy

This repository contains a deep learning project aimed at detecting aneurysms in patients with diabetic retinopathy. The project utilizes 1200 eye fundus images in .tif file format and employs a deep learning algorithm implemented using PyTorch. The model achieves an accuracy of 80% using a Convolutional Neural Network (CNN) with a ResNet18 architecture.

## Project Structure

The main folder structure of the repository is as follows:

```
- Notebooks
    -- 02_data_wrangling.ipynb
    -- 03_EDA.ipynb
    -- 04_preprocessing_modeling.ipynb
    -- helper_functions.py
```

## Notebooks

### 02_data_wrangling.ipynb

This notebook focuses on the initial data wrangling tasks, including data loading, cleaning, and preprocessing. It covers tasks such as handling missing values, data normalization, and data augmentation if applicable. 

### 03_EDA.ipynb

In this notebook, Exploratory Data Analysis (EDA) is performed on the dataset. It includes statistical analysis, visualizations, and insights into the distribution of classes and features within the dataset. EDA helps in understanding the underlying patterns and characteristics of the data.

### 04_preprocessing_modeling.ipynb

This notebook combines preprocessing tasks with the model building process. It includes steps such as feature extraction, data transformation, model training, evaluation, and hyperparameter tuning. The implementation of the deep learning algorithm using PyTorch with a ResNet18 architecture is detailed in this notebook.

### helper_functions.py

This Python script contains helper functions used throughout the project. These functions may include data preprocessing functions, model evaluation metrics, image processing utilities, or any other reusable code snippets.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the `Notebooks` directory.
3. Open and execute the notebooks in sequential order (`02_data_wrangling.ipynb`, `03_EDA.ipynb`, `04_preprocessing_modeling.ipynb`).
4. Ensure you have the necessary dependencies installed. You can install them using the provided `requirements.txt` file or by manually installing the required packages using `pip` or `conda`.

## Requirements

- Python 3.8
- PyTorch
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- Other dependencies as mentioned in the notebooks.

## References

[TODO]

## Contributors

Happy to contribute!

## License

MIT

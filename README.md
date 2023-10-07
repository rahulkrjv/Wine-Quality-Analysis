# README.md

**Wine Quality Analysis**

**Overview**
This repository contains Python code for the analysis of the Wine Quality dataset, which includes physicochemical properties and wine quality ratings for both red and white wine variants of Portuguese "Vinho Verde" wine.
The analysis covers data cleaning, exploration, and visualization, as well as the identification of factors that influence wine quality using a Random Forest Regressor model.

**Dataset Information**
  **Source:** Created by Paulo Cortez, Antonio Cerdeira, Fernando Almeida, Telmo Matos, and Jose Reis in 2009.
  **Number of Instances:** Red wine - 1599; White wine - 4898.
  **Number of Attributes:** 11 input attributes + 1 output attribute.

**Attributes:**

  Fixed acidity
  Volatile acidity
  Citric acid
  Residual sugar
  Chlorides
  Free sulfur dioxide
  Total sulfur dioxide
  Density
  pH
  Sulphates
  Alcohol
  Quality (output)
  
**Code Structure**
  **data:** Contains the CSV files for the red and white wine datasets.

  **wine_quality_analysis.ipynb:** Jupyter Notebook containing the Python code for data cleaning, exploration, and analysis.

**Instructions**
1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed, along with the required libraries (pandas, matplotlib, seaborn, scikit-learn).
3. Open and run the wine_quality_analysis.ipynb notebook to perform the analysis.
4. Review the findings and visualizations in the notebook to gain insights into the Wine Quality dataset.

**Analysis Highlights**
  Summary statistics for red and white wine datasets.
  Pair plots to visualize feature relationships and wine quality.
  Histogram of wine quality scores.
  Heatmap of feature correlations with wine quality.
  Identification of important factors using a Random Forest Regressor model.
  
**License**
This project is licensed under the MIT License. Feel free to use the code and findings as needed.

**Author**
Rahul Kumar

**Acknowledgments**
The Wine Quality dataset was originally created by Paulo Cortez, Antonio Cerdeira, Fernando Almeida, Telmo Matos, and Jose Reis in 2009. Please consider citing their work if you use this dataset in your research or analysis.

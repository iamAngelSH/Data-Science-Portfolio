![Data Science Portfolio](/Extras/DataScience.gif)


Projects using Exploratory Data Analysis, Predictive Data Analysis, and Machine Learning techniques.

### Contents
  - [Projects](#projects)
    - [Boston House Data Analysis](#exploratory-data-analysis-and-predictive-analysis-using-r-boston-house-data)
    - [Amazon Stock Price Prediction](#predictive-analysis-using-python-amazon-stock-price-prediction)
    - [Loan Status Prediction](#predictive-analysis-using-linear-regression-loan-status)
     
<br/>



**Languages used**: 

<a href="https://github.com/search?q=user%3ADenverCoder1+language%3Apython"><img alt="Python" src="https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white"></a>
    <a href="https://github.com/search?q=user%3ADenverCoder1+language%3Ar"><img alt="R" src="https://img.shields.io/badge/R-276DC3.svg?logo=r&logoColor=white"></a>
    
**🧰 Frameworks and libraries**

<p>
    <a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-013243.svg?logo=numpy&logoColor=white"></a>
    <a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
    <a href="#"><img alt="Keras" src="https://img.shields.io/badge/Keras-D00000.svg?logo=Keras&logoColor=white"></a>
    <a href="#"><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?logo=TensorFlow&logoColor=white"></a>
   <a href="#"><img alt="TensorFlow" src="https://img.shields.io/badge/scikit_learn-F7931E.svg?logo=scikit-learn&logoColor=white"></a>
  
</p>

**💻 Software and tools**

<p>
  <a href="#"><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white"></a>
    <a href="#"><img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white"></a>
    <a href="#"><img alt="Git" src="https://img.shields.io/badge/Git-F05033.svg?logo=git&logoColor=white"></a>
    <a href="#"><img alt="Google Sheets" src="https://img.shields.io/badge/Google%20Sheets-34A853.svg?logo=google%20sheets&logoColor=white"></a>
</p>


<br/>



<hr>
<br/>


# Projects
<br/>



## Exploratory Data Analysis and Predictive Analysis using R: Boston House Data 
**Overview**
- A simple [EDA](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15) on the Boston House Data
- The goal was to prepare data as best as we can for predictive analysis.
  - This included checking dataset structure
  - Remove any NA values in our columns
  - Statistical summary
    - Min, Mean, Median, Max, Quartiles
  - Visuals
    - Boxplot
      - Helped in visualizing our statistics and seeing where the outliers stood
    - Correlation plot
      - See the level of linear dependence between two variables 


- Predictive Analysis using Linear Regression
  - Used 3 different Linear Models
    - Linear Model: Y = lm(Y ~ A, ...)
        - This model is a straight-line with an implicit y-interecept
    - Linear Model: Y = lm(Y ~ A + I(A^2), ...)
         - Polynomial model to find a relationship between independent variable and dependent variable
    - Linear Model: Y = lm(Y ~ A + B, ...)
         - First-order model in A, with no interaction terms

Let me know if you have an questions via [email](mailto:angelash303@gmail.com).

View full project [here](https://github.com/iamAngelSH/Data-Science-Portfolio/blob/main/EDA_BostonHousing_Data/EDA_Boston_House_Data.ipynb)

❗IMPORTANT❗


If you are going to download the file make sure the following libraries are installed.


**Libraries used in this Project:**


For Visualization:
```R
library(corrplot)
library(lattice)
library(ggplot2)
library(plotly)
```
For Data Splitting
```R
library(dplyr)
```


## Predictive Analysis using Python: Amazon Stock Price Prediction
**Overview**
- A **Predictive Analysis** project involving Stock Market data
- Goal was to prepare data to use for stock price prediction using a Machine Learning Algorithm
  - This inlcuded using *Yahoo Finance API* 
  - Reviewing our data
  - Visuals
    - Line plot to show Adj Close vs. Stock Prediction
- Predictive Analysis using Support Vector Machine 
  -  Setup for the model:
    - kernel = 'rbf'
    - For our C value and gamma, I did a couple things:
      - created different classifiers that ranged in values
      - C Value range:
        ```Python 
        c_value = [0.1, 1.0, 10.0, 100.0, 1000.0]
        ```  
      - gamma value range:
        ```Python
        gamma_Values = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
        ```
    - From here, I then got the best R^2 score from the best combination of values and used to create the SVm Regression model 

    - The results are based from October 25, 2021 through 15 days out.
    - Here are the final results:
    ```Python
    | Stock Price: $3116.55 |
	  --------------------
	| Stock Price: $3097.92 |
	  --------------------
	| Stock Price: $3031.01 |
	  --------------------
	| Stock Price: $3021.73 |
	  --------------------
	| Stock Price: $3024.18 |
	  --------------------
	| Stock Price: $3160.62 |
	  --------------------
	| Stock Price: $3168.1 |
	  --------------------
	| Stock Price: $3172.84 |
	  --------------------
	| Stock Price: $3166.63 |
	  --------------------
	| Stock Price: $3166.21 |
	  --------------------
	| Stock Price: $3179.58 |
	  --------------------
	| Stock Price: $3183.07 |
	  --------------------
	| Stock Price: $3189.64 |
	  --------------------
	| Stock Price: $3185.4 |
	  --------------------
	| Stock Price: $3182.98 |
	  --------------------
    ```


I encourage you to try this out with different values and see what you get! 

Let me know if you have an questions via [email](mailto:angelash303@gmail.com).

View the full project [here](https://github.com/iamAngelSH/Data-Science-Portfolio/blob/main/Stock_Price_Prediction/Stock_Price_Prediction.ipynb).


❗IMPORTANT❗


If you are going to download the file make sure the following libraries are installed.


**Libraries used in this Project:**

Data Preprocessing/Manipulation
```Python
import pandas as pd
import numpy as np
```

Visualization
```Python
import matplotlib.pyplot as plt
import seaborn as sns
```


Stock Market Data from Yahoo Finance API
```Python
import yfinance as yf
```

Support Vector Machine Model
```Python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
```


## Predictive Analysis using Linear Regression: [Loan Status](https://github.com/iamAngelSH/Data-Science-Portfolio/blob/main/Loan_Prediction/Loan_Prediction.ipynb)
**Overview**
- A **Predictive Analysis** project involving loan data to predict whether or not someone can recieve a loan.
- Goal was to prepare data to use for stock price prediction using a Machine Learning Algorithm
  - This inlcuded using a dataset from [Kaggle](https://www.kaggle.com/) 
  	- We used 2 different datasets: Training/Testing
 - This process included:
 	- Preliminary Data Analysis
 	- Data Cleaning
 	- Exploratory Data Analysis
 	- Data Preprocessing for Modeling
 	- Machine Learning Implementation
 
 - Machine Learning Implementation: Logistic Regression
 	- Using logistic regression we looked at the followin to decided the best parameters:
```python
parameters_log_reg = {
    'penalty' :['l2'],
    'C' : [0.01, 0.1, 1, 2, 10, 100]
} 
```  
- Our results:
	- Yes on a Loan
		- Applicant Income: 52k
		- Loan Amount 14k
		- Has Credit History
	- no on a Loan
		- Applicant Income: 34k
		- Loan Amount: 13k
		- No credit history   	


❗IMPORTANT❗


If you are going to download the file make sure the following libraries are installed.
```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV


from sklearn.linear_model import LogisticRegression

```
Let me know if you have an questions via [email](mailto:angelash303@gmail.com).

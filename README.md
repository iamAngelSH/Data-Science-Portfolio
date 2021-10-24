# Data Science Portfolio
Projects and Course work using Exploratory Data Analysis, Predictive Data Analysis, and Machine Learning techniques.

**Languages used**: 

<a href="https://github.com/search?q=user%3ADenverCoder1+language%3Apython"><img alt="Python" src="https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white"></a>
    <a href="https://github.com/search?q=user%3ADenverCoder1+language%3Ar"><img alt="R" src="https://img.shields.io/badge/R-276DC3.svg?logo=r&logoColor=white"></a>
    
**🧰 Frameworks and libraries**

<p>
    <a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-013243.svg?logo=numpy&logoColor=white"></a>
    <a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
    <a href="#"><img alt="Keras" src="https://img.shields.io/badge/Keras-D00000.svg?logo=Keras&logoColor=white"></a>
    <a href="#"><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?logo=TensorFlow&logoColor=white"></a>
</p>

**💻 Software and tools**

<p>
  <a href="#"><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white"></a>
    <a href="#"><img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white"></a>
    <a href="#"><img alt="Git" src="https://img.shields.io/badge/Git-F05033.svg?logo=git&logoColor=white"></a>
    <a href="#"><img alt="Google Sheets" src="https://img.shields.io/badge/Google%20Sheets-34A853.svg?logo=google%20sheets&logoColor=white"></a>
</p>


<br/>


### Contents
  - [Projects](#projects)
    - [Boston House Data Analysis](#exploratory-data-analysis-and-predictive-analysis-using-r-boston-house-data)
     
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

❗IMPORTANT❗


If you are going to download the file make sure the following libraries are installed.
### Libraries used in this Project:
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

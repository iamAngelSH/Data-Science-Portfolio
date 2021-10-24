# Advanced Data Analytics
Projects and Course work using Exploratory Data Analysis, Predictive Data Analysis, and Machine Learning techniques.

**Languages used**: 

<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/r/r.png"></code>
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

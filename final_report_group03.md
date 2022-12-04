# COSC 301 - Final Project Group 3 - Milestone 5 
###### *Note: Analysis was to be done for 3 questions but project was reduced to two members*
---
## Introduction

This project focuses on the importance of group-think in affecting the behavioral outcomes of fans within NFL stadiums. To understand this metric, we utilize NFL arrest data from (2011-2015) collected by authors of the Washington Post. The psychological insight into such a metric may allow data to be utilized in anticipation for rowdy crowds and susceptible environments.

--- 

## Exploratory Data Analysis (EDA)

All exploratory data analysis and overall analysis within this project was constructed, reformatted, and coded within notebooks found [within this repository folder.](https://github.com/ubco-W2022T1-cosc301/project-group03/tree/main/notebooks) The project was constructed based upon metrics asking:
1. How likely is it for a certain matchday (gameweek) or time to be a predictor of a rowdy crowd? 

AND

2. Is committing crimes correlated with specific stadiums and/or teams? (Geographical/team-cultural influence)

Our EDA presented intriguing measures and details regarding the dataset. One such metric looked at sorting pertaining to the dataset by observing the average number of arrests for the first 100 datapoints. 
![Figure 1. Average number of arrests during the week for first 100 datapoints](images\\EDA1analysis3.png) 

Since there was no saturday games listed as seen in the figure, we were aware that sorting was done by days of the week and required reformatting to account for Saturday games. This meant reformatting of the dataset sorting was necessary (in our case, by season and THEN day of week). We also sorted data to remove all NaN values by converting them to 0.

![Figure 2. Total number of arrests during  gameweeks for first 50 datapoints](images\\EDA2analysis3.png)

There also was lots of variation within the the first 50 points in the database for total arrests when observed histographically above. We could already see some trends arising before with lower arrests during weeks 4-5, 8, and 10-12.

![Figure 3. Total number of arrests during  gameweeks for first 50 datapoints](images\\EDA3analysis3.png)

Lastly, when looking at the dataset for overall histographical data of for all categorical datapoints, we notice that arrests predictably have the most common value of 0 (no arrests! 👍)

Overall arrests also interestingly remain very consistent across the years/seasons.

---

## Question 2 + Results

##### Author: Sarim Faheem 

##### Question: How likely is it for a certain matchday (game-week) or time to be a predictor of a rowdy crowd?

For this research question, once the dataset was sorted and reformatted (accounting arrests for only day, time, week, and season), I theorized that crowds are emotionally influenced by time and place which leads to emotionally charged individuals behaving with conduct that ultimately leads to other erratic individuals joining in. 

To start with
![Figure 4. Total number of arrests during  gameweeks for first 50 datapoints](images\\fig1_analysis3.png)
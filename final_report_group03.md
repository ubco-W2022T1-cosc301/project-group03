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
![Figure 1. Average number of arrests during the week for first 100 datapoints](./images/EDA1analysis3.png) 

Since there was no saturday games listed as seen in the figure, we were aware that sorting was done by days of the week and required reformatting to account for Saturday games. This meant reformatting of the dataset sorting was necessary (in our case, by season and THEN day of week). We also sorted data to remove all NaN values by converting them to 0.

![Figure 2. Total number of arrests during  gameweeks for first 50 datapoints](./images/EDA2analysis3.png)

There also was lots of variation within the the first 50 points in the database for total arrests when observed histographically above. We could already see some trends arising before with lower arrests during weeks 4-5, 8, and 10-12.

![Figure 3. Total number of arrests corresponding to all categorical data](./images/EDA3analysis3.png)

Lastly, when looking at the dataset for overall histographical data of for all categorical datapoints, we notice that arrests predictably have the most common value of 0 (no arrests! 👍)

Overall arrests also interestingly remain very consistent across the years/seasons.

---

## Question 1 + Results

##### Author: Omar Kandeel

##### Question: Is committing crimes correlated with specific stadiums and/or teams? (Geographical/team-cultural influence)

One of the research questions asked which team had the "rowdiest" crowds leading to higher arrests rates. Looking at both home teams and away teams.

Firstly let's take a look at the average arrests made for each team as a home team.

![alt text for screen readers](./images/HomeArrests.png)

As we can see, San Diego is the team with the rowdiest fans when they are playing at their home stadium, sitting at a total of 80 arrests made through out the 2011-2015 NFL seasons.

Let's give them the benefit of the doubt since they might have more games than other stadiums? So where does San Diego stand at the number of games played at their stadium?

![alt text for screen readers](./images/NumberofGames.png "Games per Stadium")

Surprisingly enough, San Diego did not have the highest number of games played at home. But rather they tied for 4th place compared to the other teams.
**San Diego** has half the amount of games as Arizona (the tied leader in the amount of home games), and yet Arizona has almost a 1/4 the arrests that San Diego has seen.

Now let's take a look at the away teams and see if San Diego is also the rowdiest team when they are on the road.

![alt text for screen readers](./images/AwayArrests.png "Away arrests")

As we can see, it's no longer the San Diego fans being the rowdiest, but instead the **New England** fans!

Again, we're going to do the same analysis and give them the benefit of the doubt since they might have had more games than others as the away team.

![alt text for screen readers](./images/NumAwayGs.png "Number of away games per team")

Now this gives some interesting insight. Because for away teams, the team with the most arrests is New England (Patriots). They are leading in the number or arrests during their away games, even though they are not leading in the number of away games (count wise). The team with the most away games is Baltimore and yet they have a total of 40 arrests during their away games while New England has closer to 65.

Lastly, let's take a look at whether or not there has been a trend (upwards or downwards) between later seasons and earlier seasons for arrests.

![alt text for screen readers](./images/SeasonalArrests.png "Number of arrests per season")

Now this gives us an insight as to which seasons had the highest arrests between all the seasons in our dataset. However, we still need to see how many games were played in each season as that would change the overall result.

![alt text for screen readers](./images/GamesPerSeason.png "Games per Season")

After looking at the data, we can see that during the 2012 season, there were more games played, thus creating a higher possibility of conflicts resulting in arrests. Nonetheless, the **2015 season** (that had the secondmost arrests during the season) had 2 more arrests during the season even though there were 7 fewer games during then.

*What do these higher arrests within a season, even though there were fewer games than other seasons, tell us?*

After doing some digging, it turns out that the 2015 season was the 50th anniversary of the [Super Bowl.](https://en.wikipedia.org/wiki/2015_NFL_season)
With the opening game being the **New England** Patriots and the Pittsburgh Steelers.

---

## Question 2 + Results

##### Author: Sarim Faheem 

##### Question: How likely is it for a certain matchday (game-week) or time to be a predictor of a rowdy crowd?

For this research question, once the dataset was sorted and reformatted (accounting arrests for only day, time, week, and season), I theorized that crowds are emotionally influenced by time and place which leads to emotionally charged individuals behaving with conduct that ultimately leads to other erratic individuals joining in. 
![Figure 4. Total number of games during  gameweeks for corresponding gametime](./images/fig3_analysis3.png)
Notice that most games occur at noon which must be accounted for in our remaining results.
![Figure 5. Total number of arrests during  gameweeks for corresponding gametime](./images/fig1_analysis3.png)
**To start with I observed how many arrests take place during specific times and found that most arrests happen at noon (12:00-1:00pm) which makes sense since that is when most games are played** 
![Figure 6. Average number of arrests during  gameweeks for corresponding gametime](./images/fig2_analysis3.png)
However, the average number of arrests was higher during late-night games with expected rowdier crowds.

![Figure 7. Total number of arrests during  gameday](./images/fig4_analysis3.png)
![Figure 8. Average number of arrests during  gameday](./images/fig5_analysis3.png)
![Figure 9. Total number of games during  gameday](./images/fig6_analysis3.png)


Similar results applied for gamedays where predictably significant amount of games being played on Sunday and therefore, a high amount of total arrests.

Average number of arrests per day is significantly higher on Wednesday as it accounts for only 1 variable within the dataset. (An intense rivalry game on opening day within the 2012 season).

Most notably, Monday night football brings in rowdier crowds on average. Perhaps an indicator of crowd fatigue at the start of of a week.

![Figure 10. Total number of arrests during  gameweek](./images/fig7_analysis3.png)
![Figure 11. Average number of arrests during  gameweek](./images/fig8_analysis3.png)
![Figure 12. Total number of games during  gameweek](./images/fig9_analysis3.png)

For gameweeks, beyond the early week excitement, week number does not seem to have any correlation with arrest rates during NFL games.

- Week 8-9 is scheduled for around November 1 which is the official trade deadline for the NFL. An important variable in sportsfans' perception of the state of their aligned team.
- Week 14-16 is during the late December holidays season.
---

## Conclusion

Arrests during the NFL season do tend to have a correlation with the influence of groupthink. The team with the highest arrests rate when they are playing on their home field is the San Diego (LA Chargers). Meanwhile the team with the highest arrests during the games where they are playing on the opponents field is the New England (Patriots).

Similarly, arrests during NFL in-season games do tend to have correlation with factors pertaining to time A. There seems to be a distinct correlation of higher arrests per game for late night games compared to the more popularly schedule mid-day early games. Similarly, arrest rates are higher for Sunday-Monday scheduled NFL games compared to remaining game days. 

**Crowds are impacted by multiple factors that influence their psyche and cause their emotional response to be charged or unpredictable. Environment factors such as *time and locale* influence these emotional responses and lead to a desire for some method of discharge. When one individual entices the crowd, the overall crowd seems to jump in to release their emotions. Rowdier crowds for teams with merits, reputations, or high expectations, have higher fan arrests on average similar to  games with rowdier crowds produced from influences of time and season. These factors highlight potential red-flags to predict disorderly fan behavior**



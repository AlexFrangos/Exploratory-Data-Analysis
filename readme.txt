
I selected to do the Exploratory Data Analysis project (Data Science)

The dataset used is from kaggle.com: https://www.kaggle.com/mohansacharya/graduate-admissions

This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.

The project must demonstrate the following skills:

Ability to formulate relevant questions for investigation
Identifying trends
Identifying covariation between variables
Communicating results effectively using visualisations



Relevant questions for investigation:


1) Which are the top 10 GRE Scores, TOEFL Scores, SOP, LOR, CGPA and what was the 'Chance of Admit' for those?

2) Find the correlation between all columns.

3) Which column matters the most for a better chance of admit (highest correlation with 'Chance of Admit')?

4) Find people that did better in hard skills and lesser in soft skills and the effect of this on both the 'Chance of Admit' and 'University Rating'. 
   Note: Hard skills are considered to be the 'GRE Score', 'TOEFL Score' and 'CGPA'. Soft skills are considered to be 'SOP' and 'LOR'

5) Find people that did better in soft skills and lesser in hard skills and the effect of this on both the 'Chance of Admit' and 'University rating.
   Note: Hard skills are considered to be the 'GRE Score', 'TOEFL Score' and 'CGPA'. Soft skills are considered to be 'SOP' and 'LOR'

6) Find the average of the columns that is required to have a 'Chance of Admit' higher than the average 'Chance of Admit'
   Find the average of columns that is required to have a 'Chance of Admit' in the 75% percentile.

7) Do people with higher hard skills than normal go to a university with a better 'University Rating'?
   Note: Hard skills are considered to be the 'GRE Score', 'TOEFL Score' and 'CGPA'. 




I developed a number of functions for which you will have to uncomment the code to run them one by one (preferably). Below I outlined how I think its most appropriate to run the code.

1) Run the descriptiveStatistics function. (Uncomment line 25)

2) Run the outlierAnalysis function. (Uncomment line 41)

3) Run the showDifferenceAfterRemovingOutliers (Uncomment line 58)

4) Run the distributionGraphs function. (Uncomment line 79)

5) Run the topScoresWithChanceOfAdmit function. You can call the function with any column from the dataset. (Uncomment line 88)

6) Run the correlationPlot function. (Uncomment line 99)

7) Run the correlationPlotWithChanceofAdmit function. (Uncomment line 112)

8) Run the betterHardSkillsThanSoftSkills function. (Uncomment first line 130 and then uncomment line 131)

9) Run the betterSoftSkillsThanHardSkills function. (Uncomment first line 152 and then uncomment line 153)

10) Run the admissionHigherThanMeanAnd75Percentile function. (Uncomment line 174)

11) Run the hardSkillsBetterUniversity function. (Uncomment line 188)


Conclussion:
Some interesting facts came out after this Exploratory Data Analysis.

I found that CGPA has the highest correlation with Chance of Admit (after running the correlationPlotWithChanceOfAdmit function)

I found that the mean of 'Chance of Admit' on people that have better hard skills and lesser soft skills is 0.75, whereas mean of 'Chance of Admit' on people that have better soft skills and lesser hard skills is 0.669. From this we can see that hard skills produce higher chances of admission.

I found the average of all columns that is needed to have a 'Chance of Admit' higher than the average one is:

Average of all columns when 'Chance of Admit' is larger than mean
GRE Score            324.544118
TOEFL Score          111.235294
University Rating      3.784314
SOP                    3.995098
LOR                    3.936275
CGPA                   9.015147
Research               0.818627

I found that the average of all columns that is needed to have a 'Chance of Admit' that is in the 75% percentile is:
Average of all columns when 'Chance of Admit' is in the 75% percentile
GRE Score            329.928571
TOEFL Score          114.510204
University Rating      4.377551
SOP                    4.423469
LOR                    4.295918
CGPA                   9.342347
Research               0.959184



Notes: 
Sometimes you have to run the program again to see all the displayed data on the terminal. 
Sometimes you have to adjust the settings of the python launcher to see all the graphs clearly. I have attached all the images of the visualisations produced by the program incase something isn't clear.

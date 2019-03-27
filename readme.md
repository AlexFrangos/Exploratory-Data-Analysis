---


---

<h1 id="exploratory-data-analysis-project-data-science">Exploratory Data Analysis project (Data Science)</h1>
<p>The dataset used is from <a href="http://kaggle.com">kaggle.com</a>: <a href="https://www.kaggle.com/mohansacharya/graduate-admissions">https://www.kaggle.com/mohansacharya/graduate-admissions</a></p>
<p>This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.</p>
<p>The project must demonstrate the following skills:</p>
<p>Ability to formulate relevant questions for investigation<br>
Identifying trends<br>
Identifying covariation between variables<br>
Communicating results effectively using visualisations</p>
<h2 id="relevant-questions-for-investigation">Relevant questions for investigation:</h2>
<ol>
<li>
<p>Which are the top 10 GRE Scores, TOEFL Scores, SOP, LOR, CGPA and what was the ‘Chance of Admit’ for those?</p>
</li>
<li>
<p>Find the correlation between all columns.</p>
</li>
<li>
<p>Which column matters the most for a better chance of admit (highest correlation with ‘Chance of Admit’)?</p>
</li>
<li>
<p>Find people that did better in hard skills (skills that require pure knowledge of the subject) and lesser in soft skills (skills that may require communication and inter-personal relations)  and the effect of this on both the ‘Chance of Admit’ and ‘University Rating’.<br>
Note: Hard skills are considered to be the ‘GRE Score’, ‘TOEFL Score’ and ‘CGPA’. Soft skills are considered to be ‘SOP’ and ‘LOR’.</p>
</li>
<li>
<p>Find people that did better in soft skills (skills that may require communication and inter-personal relations) and lesser in hard skills (skills that require pure knowledge of the subject) and the effect of this on both the ‘Chance of Admit’ and 'University rating.<br>
Note: Hard skills are considered to be the ‘GRE Score’, ‘TOEFL Score’ and ‘CGPA’. Soft skills are considered to be ‘SOP’ and ‘LOR’</p>
</li>
<li>
<p>Find the average of the columns that is required to have a ‘Chance of Admit’ higher than the average ‘Chance of Admit’<br>
Find the average of columns that is required to have a ‘Chance of Admit’ in the 75% percentile.</p>
</li>
<li>
<p>Do people with higher hard skills than normal go to a university with a better ‘University Rating’?<br>
Note: Hard skills are considered to be the ‘GRE Score’, ‘TOEFL Score’ and ‘CGPA’.</p>
</li>
</ol>
<h2 id="how-to-run-the-code">How to run the code:</h2>
<p>I developed a simple command-line menu for which you can select any of the options listed to run any function.</p>
<p>Note: For the first four selections (A, B , C , D), I am using the data set that contains outliers to show you my way of thinking and how I approached this problem. For the rest of the selections I am using the data set that does not contain outliers to continue the Exploratory Data Analysis.</p>
<h2 id="conclussion">Conclussion:</h2>
<p>Some interesting facts came out after this Exploratory Data Analysis.</p>
<p>I found that CGPA has the highest correlation with Chance of Admit (after running the correlationPlotWithChanceOfAdmit function)</p>
<p>I found that the mean of ‘Chance of Admit’ on people that have better hard skills and lesser soft skills is 0.75, whereas mean of ‘Chance of Admit’ on people that have better soft skills and lesser hard skills is 0.669. From this we can see that hard skills produce higher chances of admission.</p>
<p>I found the average of all columns that is needed to have a ‘Chance of Admit’ higher than the average one is:</p>
<p>Average of all columns when ‘Chance of Admit’ is larger than mean<br>
GRE Score            324.544118<br>
TOEFL Score          111.235294<br>
University Rating      3.784314<br>
SOP                    3.995098<br>
LOR                    3.936275<br>
CGPA                   9.015147<br>
Research               0.818627</p>
<p>I found that the average of all columns that is needed to have a ‘Chance of Admit’ that is in the 75% percentile is:<br>
Average of all columns when ‘Chance of Admit’ is in the 75% percentile<br>
GRE Score            329.928571<br>
TOEFL Score          114.510204<br>
University Rating      4.377551<br>
SOP                    4.423469<br>
LOR                    4.295918<br>
CGPA                   9.342347<br>
Research               0.959184</p>
<h2 id="notes">Notes</h2>
<p>Sometimes you have to run the program again to see all the displayed data on the terminal.<br>
Sometimes you have to adjust the settings of the python launcher to see all the graphs clearly. I have attached all the images of the visualisations produced by the program incase something isn’t clear.</p>


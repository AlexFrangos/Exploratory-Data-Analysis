#This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.




import pip._internal as pip


package_names=['seaborn', 'pandas', 'matplotlib' ,'scipy'] #packages to install
pip.main(['install'] + package_names + ['--upgrade'])

import sys
import time
import pandas as pd
import seaborn as sns

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

admissions_data = pd.read_csv("admission_statistics.csv",sep='\s*,\s*',header=0, encoding='ascii', engine='python')

# We drop the 'Serial No.' column from our data set as it doesnt help us in our exploratory data analysis
admissions_data = admissions_data.drop("Serial No.", axis=1)


def leaveEmptyLines():
	print()
	print()

# Describe data so we can get an insight of what we are handling and maybe detect any outliers
def descriptiveStatistics(admissions_data_old):
	print("Descriptive data: ")
	leaveEmptyLines()
	print(admissions_data_old.describe(include='all'))



# Print a boxplot to detect any outliers
def outlierAnalysis(admissions_data_old):
	col_names = ['TOEFL Score','GRE Score', 'University Rating','LOR','SOP', 'CGPA', 'Chance of Admit']

	fig, ax = plt.subplots(len(col_names), figsize=(8,40))

	for i, col_val in enumerate(col_names):
		sns.boxplot(y=admissions_data_old[col_val], ax=ax[i])
		ax[i].set_title('Box plot - {}'.format(col_val), fontsize=10)
		ax[i].set_xlabel(col_val, fontsize=8)

	plt.show()


# After we saw that there are some outliers (From calling the above function ('outlierAnalysis') we remove the outliers and continue our EDA with our new data set.
def outlierAnalysisAndRemoval(admissions_data):
	Q1 = admissions_data.quantile(0.25)
	Q3 = admissions_data.quantile(0.75)	
	IQR = Q3-Q1

	admissions_data_out = admissions_data[~((admissions_data < (Q1 - 1.5 * IQR)) |(admissions_data > (Q3 + 1.5 * IQR))).any(axis=1)]
	return admissions_data_out

# Show the difference in the number of columns and rows after removing the outliers.
def showDifferenceAfterRemovingOutliers(admissions_data,admissions_data_old):
	admissions_data_out = outlierAnalysisAndRemoval(admissions_data)

	print("Number of rows and columns of the original dataset: ", admissions_data_old.shape)
	print("Number of rows and columns after removing outliers: ", admissions_data_out.shape)


#This set contains the outliers
admissions_data_old = admissions_data 

# Our data set now after callin the 'outlierAnalysisandRemoval' function  doesnt contain any outliers. 
admissions_data=outlierAnalysisAndRemoval(admissions_data) 


def distributionGraphs(admissions_data_old):
	col_names = ['TOEFL Score','GRE Score','University Rating','SOP','CGPA', 'Research', 'Chance of Admit']
	fig, ax = plt.subplots(len(col_names), figsize=(16,12))

	for i, col_val in enumerate(col_names):
		sns.distplot(admissions_data_old[col_val], hist=True, ax=ax[i])
		ax[i].set_title('Freq dist '+col_val, fontsize=10)
		ax[i].set_xlabel(col_val, fontsize=8)
		ax[i].set_ylabel('Count', fontsize=8)

	
	plt.show()


# Find top 10 gre,toefl,sop,lor,cgpa scores and what was the chance of admit for those. This is the answer to question 1
def topScoresWithChanceOfAdmit(admissions_data,column):
	criteria = admissions_data.sort_values(by = column, ascending=False)
	print(criteria[[column,'Chance of Admit']].head(10))


# Shows correlation between data in a heatmap. This is the answer to question 2
def correlationPlot(admissions_data):
	print(admissions_data.apply(lambda s: admissions_data.corrwith(s)))

	f, ax = plt.subplots(figsize=(10, 8))
	corr = admissions_data.corr()
	sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
	plt.show()


# Display collumns that have the highest correlation with 'Chance of Admit'. This is the answer to question 3
def correlationPlotWithChanceOfAdmit(admissions_data):
	admissions_data_corr = admissions_data.corr()['Chance of Admit'][:-1] # -1 because the latest row is 'Chance of Admit'
	golden_features_list = admissions_data_corr[abs(admissions_data_corr) > 0.5].sort_values(ascending=False)
	print("There is {} strongly correlated values with Chance of Admit:\n{}".format(len(golden_features_list), golden_features_list))

	for i in range(0, len(admissions_data.columns), 5):
		sns.pairplot(data=admissions_data, x_vars=admissions_data.columns[i:i+5], y_vars=['Chance of Admit'])

	plt.show()	


# Find people that did better in hard skills than soft skills and the effect of this on both the chance of admit and the university rating. This is the answer to question 4
def betterHardSkillsThanSoftSkills(admissions_data,column):
	criteria = ((admissions_data['GRE Score'] >= admissions_data['GRE Score'].mean()) & (admissions_data['TOEFL Score'] >= admissions_data['TOEFL Score'].mean()) & (admissions_data['CGPA'] >= admissions_data['CGPA'].mean()) & (admissions_data['SOP'] <= admissions_data['SOP'].mean()) & (admissions_data['LOR'] <= admissions_data['LOR'].mean()))
	hard_skills_more = admissions_data[criteria]
	
	print (hard_skills_more[['GRE Score','TOEFL Score','CGPA','SOP', 'LOR', column]])
	leaveEmptyLines()

	if column == 'Chance of Admit':
		print("Mean of 'Chance of Admit' on criteria list: ", hard_skills_more[column].mean())
		print("Mean of 'Chance of Admit' on all the admissios_data list is: ", admissions_data[column].mean())
	elif column == 'University Rating':
		print("Mean of 'University Rating' on criteria list: ", hard_skills_more[column].mean())
		print("Mean of 'University Rating' on all the admissios_data list is: ", admissions_data[column].mean())



# Find people that did better in soft skills and lesser in hard skills and the effect on  both the chance of admit and the university rating. This is the answer to question 5
def betterSoftSkillsThanHardSkills(admissions_data,column):
	criteria = ((admissions_data['GRE Score'] <= admissions_data['GRE Score'].mean()) & (admissions_data['TOEFL Score'] <= admissions_data['TOEFL Score'].mean()) & (admissions_data['CGPA'] <= admissions_data['CGPA'].mean()) & (admissions_data['SOP'] >= admissions_data['SOP'].mean()) & (admissions_data['LOR'] >= admissions_data['LOR'].mean()))
	soft_skills_more = admissions_data[criteria]
	
	print (soft_skills_more[['GRE Score','TOEFL Score','CGPA','SOP', 'LOR', column]])
	leaveEmptyLines()

	if column == 'Chance of Admit':
		print("Mean of 'Chance of Admit' on criteria list: ", soft_skills_more[column].mean())
		print("Mean of 'Chance of Admit' on all the admissios_data list is: ", admissions_data[column].mean())
	elif column == 'University Rating':
		print("Mean of 'University Rating' on criteria list: ", soft_skills_more[column].mean())
		print("Mean of 'University Rating' on all the admissios_data list is: ", admissions_data[column].mean())


# Find the average of all the collumns for the chance of admission to be higher than the mean.  This is the answer to question 6
def admissionHigherThanMeanAnd75Percentile(admissions_data):
	 criteria = admissions_data['Chance of Admit'] > admissions_data['Chance of Admit'].mean()
	 more_than_mean = admissions_data[criteria]
	 more_than_mean= more_than_mean.drop("Chance of Admit", axis=1)
	
	 print("Average of all columns when 'Chance of Admit' is larger than mean")
	 print(more_than_mean.mean())
	 leaveEmptyLines()

	 criteria2= admissions_data['Chance of Admit'] > admissions_data['Chance of Admit'].quantile(0.75)
	 more_than_75_percentile = admissions_data[criteria2]
	 more_than_75_percentile = more_than_75_percentile.drop('Chance of Admit', axis=1)

	 print("Average of all columns when 'Chance of Admit' is in the 75% percentile")
	 print(more_than_75_percentile.mean())



# See if people with higher than average hard skills go to a university with a better rating. This is the answer to question 7
def hardSkillsBetterUniversity(admissions_data):
	criteria = ((admissions_data['GRE Score'] >= admissions_data['GRE Score'].mean()) & (admissions_data['TOEFL Score'] >= admissions_data['TOEFL Score'].mean()) & (admissions_data['CGPA'] >= admissions_data['CGPA'].mean()))
	hard_skills_better_uni = admissions_data[criteria]
	
	print (hard_skills_better_uni[['GRE Score','TOEFL Score','CGPA','University Rating']])
	leaveEmptyLines()

	print("Mean of University Rating on criteria list: ", hard_skills_better_uni['University Rating'].mean())
	print("Mean of University Rating on all the admissions list is: ", admissions_data['University Rating'].mean())


def menu(admissions_data,admissions_data_old):
	choice =  ''
	while True:

		choice = input("""
                      A: Run the descriptiveStatistics function. 
                      B: Run the outlierAnalysis function
                      C: Run the showDifferenceAfterRemovingOutliers
                      D: Run the distributionGraphs function.
                      E: Run the topScorersWithChanceOfAdmit function.
                      F: Run the correlationPlot function.
                      G: Run the correlationPlotWithChanceOfAdmit function.
                      H: Run the betterHardSkillsThanSoftSkills function.
                      I: Run the betterSoftSkillsThanHardSkills function.
                      J: Run the admissionHigherThanMeanAnd75Percentile function.
                      K: Run the hardSkillsBetterUniversity function.
                      Q: Quit
                      
                      Please enter your choice:   """)
		leaveEmptyLines()


		if choice == "A" or choice == "a":
			descriptiveStatistics(admissions_data_old)

		elif choice == "B" or choice == "b":
			outlierAnalysis(admissions_data_old)

		elif choice == "C" or choice == "c":
			showDifferenceAfterRemovingOutliers(admissions_data,admissions_data_old)

		elif choice == "D" or choice == "d":
			distributionGraphs(admissions_data_old)

		elif choice == "E" or choice == "e":
			valid_columns  = {
				"A" : "GRE Score",
				"B" : "TOEFL Score",
				"C" : "University Rating",
				"D" : "SOP",
				"E" : "LOR",
				"F" : "CGPA",
				"G" : "Research"

			}

			column = ''
			while column.upper() not in valid_columns:
				column = input("""
			Valid column choices:
                      A: GRE Score
                      B: TOEFL Score
                      C: University Rating
                      D: SOP
                      E: LOR
                      F: CGPA
                      G: Research
                    

                      Please enter your choice: """)
				print('selected', column)
			actual = valid_columns[column.upper()]
			print(actual)


			topScoresWithChanceOfAdmit(admissions_data,actual)


		elif choice == "F" or choice == "f":
			correlationPlot(admissions_data)

		elif choice == "G" or choice == "g":
			correlationPlotWithChanceOfAdmit(admissions_data)

		elif choice == "H" or choice == "h":
			betterHardSkillsThanSoftSkills(admissions_data,'Chance of Admit')
			leaveEmptyLines()
			betterHardSkillsThanSoftSkills(admissions_data,'University Rating')

		elif choice == "I" or choice == "i":
			betterSoftSkillsThanHardSkills(admissions_data,'Chance of Admit')
			leaveEmptyLines()
			betterSoftSkillsThanHardSkills(admissions_data,'University Rating')

		elif choice == "J" or choice == "j":
			admissionHigherThanMeanAnd75Percentile(admissions_data)

		elif choice == "K" or choice == "k":
			hardSkillsBetterUniversity(admissions_data)


		elif choice == "q" or choice == "Q":
			sys.exit()
		if choice.upper() not in ('A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Q'):
			leaveEmptyLines()
			print("                      You must only select one of the options in the menu")
			print("                      Please try again")
			leaveEmptyLines()
		else:
			leaveEmptyLines()
			sefes = input('To go back to start, press ENTER:'  )
			leaveEmptyLines()










menu(admissions_data,admissions_data_old)














	   





















	




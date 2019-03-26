#This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.
import pandas as pd
import numpy as np
import seaborn as sns
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
def descriptiveStatistics(admissions_data):
	print("Descriptive data: ")
	leaveEmptyLines()
	print(admissions_data.describe(include='all'))

#descriptiveStatistics(admissions_data)


# Print a boxplot to detect any outliers
def outlierAnalysis(admissions_data):
	col_names = ['TOEFL Score','GRE Score', 'University Rating','LOR','SOP', 'CGPA', 'Chance of Admit']

	fig, ax = plt.subplots(len(col_names), figsize=(8,40))

	for i, col_val in enumerate(col_names):
		sns.boxplot(y=admissions_data[col_val], ax=ax[i])
		ax[i].set_title('Box plot - {}'.format(col_val), fontsize=10)
		ax[i].set_xlabel(col_val, fontsize=8)

	plt.show()

#outlierAnalysis(admissions_data)

# After we saw that there are some outliers (From calling the above function ('outlierAnalysis') we remove the outliers and continue our EDA with our new data set.
def outlierAnalysisAndRemoval(admissions_data):
	Q1 = admissions_data.quantile(0.25)
	Q3 = admissions_data.quantile(0.75)	
	IQR = Q3-Q1

	admissions_data_out = admissions_data[~((admissions_data < (Q1 - 1.5 * IQR)) |(admissions_data > (Q3 + 1.5 * IQR))).any(axis=1)]
	return admissions_data_out

# Show the difference in the number of columns and rows after removing the outliers.
def showDifferenceAfterRemovingOutliers(admissions_data):
	admissions_data_out = outlierAnalysisAndRemoval(admissions_data)
	print("Number of rows and columns of the original dataset: ", admissions_data.shape)
	print("Number of rows and columns after removing outliers: ", admissions_data_out.shape)

#showDifferenceAfterRemovingOutliers(admissions_data)



# Our data set now after callin the 'outlierAnalysisandRemoval' function  doesnt contain any outliers. 
admissions_data=outlierAnalysisAndRemoval(admissions_data) 


def distributionGraphs(admissions_data):
	col_names = ['TOEFL Score','GRE Score','University Rating','SOP','CGPA', 'Research', 'Chance of Admit']
	fig, ax = plt.subplots(len(col_names), figsize=(16,12))

	for i, col_val in enumerate(col_names):
		sns.distplot(admissions_data[col_val], hist=True, ax=ax[i])
		ax[i].set_title('Freq dist '+col_val, fontsize=10)
		ax[i].set_xlabel(col_val, fontsize=8)
		ax[i].set_ylabel('Count', fontsize=8)

	
	plt.show()

#distributionGraphs(admissions_data)



# Find top 10 gre,toefl,sop,lor,cgpa scores and what was the chance of admit for those. This is the answer to question 1
def topScoresWithChanceOfAdmit(admissions_data,column):
	criteria = admissions_data.sort_values(by = column, ascending=False)
	print(criteria[[column,'Chance of Admit']].head(10))

#topScoresWithChanceOfAdmit(admissions_data,column)    Use any column you want from the dataset.

# Shows correlation between data in a heatmap. This is the answer to question 2
def correlationPlot(admissions_data):
	print(admissions_data.apply(lambda s: admissions_data.corrwith(s)))

	f, ax = plt.subplots(figsize=(10, 8))
	corr = admissions_data.corr()
	sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
	plt.show()

#correlationPlot(admissions_data)

# Display collumns that have the highest correlation with 'Chance of Admit'. This is the answer to question 3
def correlationPlotWithChanceOfAdmit(admissions_data):
	admissions_data_corr = admissions_data.corr()['Chance of Admit'][:-1] # -1 because the latest row is 'Chance of Admit'
	golden_features_list = admissions_data_corr[abs(admissions_data_corr) > 0.5].sort_values(ascending=False)
	print("There is {} strongly correlated values with Chance of Admit:\n{}".format(len(golden_features_list), golden_features_list))

	for i in range(0, len(admissions_data.columns), 5):
		sns.pairplot(data=admissions_data, x_vars=admissions_data.columns[i:i+5], y_vars=['Chance of Admit'])

	plt.show()	

correlationPlotWithChanceOfAdmit(admissions_data)

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


#betterHardSkillsThanSoftSkills(admissions_data,'Chance of Admit')
#betterHardSkillsThanSoftSkills(admissions_data,'University Rating')



	
	
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

#betterSoftSkillsThanHardSkills(admissions_data,'Chance of Admit')
#betterSoftSkillsThanHardSkills(admissions_data,'University Rating')


	
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

#admissionHigherThanMeanAnd75Percentile(admissions_data)


# See if people with higher than average hard skills go to a university with a better rating. This is the answer to question 7
def hardSkillsBetterUniversity(admissions_data):
	criteria = ((admissions_data['GRE Score'] >= admissions_data['GRE Score'].mean()) & (admissions_data['TOEFL Score'] >= admissions_data['TOEFL Score'].mean()) & (admissions_data['CGPA'] >= admissions_data['CGPA'].mean()))
	hard_skills_better_uni = admissions_data[criteria]
	
	print (hard_skills_better_uni[['GRE Score','TOEFL Score','CGPA','University Rating']])
	leaveEmptyLines()

	print("Mean of University Rating on criteria list: ", hard_skills_better_uni['University Rating'].mean())
	print("Mean of University Rating on all the admissions list is: ", admissions_data['University Rating'].mean())

#hardSkillsBetterUniversity(admissions_data)
















	   





















	




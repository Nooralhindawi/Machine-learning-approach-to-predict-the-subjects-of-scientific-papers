# Machine-learning-approach-to-predict-the-subjects-of-scientific-papers
Assignment
This code is made to develop a machine learning approach to predict the subjects of scientific papers:
Each section has a specific header in the code.
-The code has been acheived through GoogleColab platform.
-After uploading the dataset to my personal drive, the data has been read by the first lines of code (after importing all the needed libraries)
-The dataset has been organized and defined to features and label.
-Splitting the data has been accomplished using 10-fold cross validation and LogisticRegression ML approach has been utilized.
-In order to refer to the correct paper_id, the index of each output has been acquired and stacjed with the testing labels.
-Results have been stores in a TSV file (by adding sep = '\t')
-The approach has been evaluated via distinct metrics  
-The disadvantage of *subset accuracy* (also known as exact match ratio) measure is that multi-class classification problems have a chance of being partially correct, but here we ignore those partially correct matches.There is a function in scikit-learn which implements subset accuracy, called as accuracy_score that has been imported earlier and used here.

Anonther solution can be acheived using ATOM library and by alternting the ML approaches.

#This directory contains the a selection of the Cora dataset (www.research.whizbang.com/data).

The Cora dataset consists of Machine Learning papers. These papers are classified into one of the following seven classes:
		Case_Based
		Genetic_Algorithms
		Neural_Networks
		Probabilistic_Methods
		Reinforcement_Learning
		Rule_Learning
		Theory

The papers were selected in a way such that in the final corpus every paper cites or is cited by atleast one other paper. 
There are 2708 papers in the whole corpus. 

After stemming and removing stopwords we were left with a vocabulary of size 1433 unique words. 
All words with document frequency less than 10 were removed.


THE DIRECTORY CONTAINS TWO FILES:

The .content file contains descriptions of the papers in the following format:

		<paper_id> <word_attributes>+ <class_label>

The first entry in each line contains the unique string ID of the paper followed by binary values indicating whether each word in the vocabulary is present (indicated by 1) or absent (indicated by 0) in the paper. Finally, the last entry in the line contains the class label of the paper.

The .cites file contains the citation graph of the corpus. Each line describes a link in the following format:

		<ID of cited paper> <ID of citing paper>

Each line contains two paper IDs. The first entry is the ID of the paper being cited and the second ID stands for the paper 
which contains the citation. 
The direction of the link is from right to left. 
If a line is represented by "paper1 paper2" then the link is "paper2->paper1".

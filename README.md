# Example Data of Change Analysis and for Bug Detection for Cyber-Physical Systems (CPS)

The following GitHub repository contains several methods to extract commit changes and issues from any GitHub repository. These methods only require the URL of the corresponding GitHub repository(ies).

## Goal of Repository
We created this repository as part of a university project. The project's aim was to analyse a set of GitHub repositories of CPS projects to classify a set of commits according to their changes. This set of classified changes can then be used to train ML based bug prediction algorithms for the correct interpretation of commit changes. The result of classified commit changes provides a high and low level change classification as well as the significance of such a change. In the following you can see an extract of the results:
![ClassificationExample](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/ClassificationExample.png)
In order to classify commit changes we used an already existing taxonomy of MCR changes from the paper "An empirical investigation of relevant changes and automation needs in modern code review" by Sebastiano Panichella and Nik Zaugg (2020, Empirical Software Engineering (2020) 25:4833–4872, https://doi.org/10.1007/s10664-020-09870-3). The taxonomy was further enhanced with a significance level as described in detail below. The significance level was based on the paper "Change Analysis with Evolizer and ChangeDistiller" by Harald C. Gall, Beat Fluri, and Martin Pinzger (IEEE Software 2009, 26(1):26-33., http://www.zora.uzh.ch). An overview of the entire taxonomy used within out project can be seen within the tab "Taxonomy" of the excel file "Results of example classification" linked at the bottom.

## Motivation of Project
As mentioned above for each analysed commit change, we provided a significance level. Understanding the significance of a certain commit change is particularly important for CPS projects, because of the various effects such a code change may impose on the CPS. There are various examples of catastrophic consequences of unmonitored or unintentional code changes such as the Boeing 747 Max crashes in 2019 or Tesla's autopilot crash. Detecting bugs early, for instance as part of continuous integration, contributes significantly to the quality of code as well as to the efficiency of software and hardware. Also, analysing the code history of projects does not only improve aforementioned points, but also reduces development and maintenance costs. 

## Study Definition & Planning
The main focus of the project is to specify a taxonomy specifically for CPS code changes & bugs. Our research questions are 
a) to understand how bugs/code changes affect CPS 
b) to specify and categorize significant and behavioral CPS code changes and
c) to recognize critical changes affecting the behavior of functionality.
We formulated the following hypothesis:
a) Categorization of CPS code changes & bugs is feasible
b) CPS code changes & bugs have a specific taxonomy, which should be useful to design models for CPS and eventually feed it into ML to predict types of behavioral changes & failures.

The approach to create the taxonomy is the following: first, several GitHub repositories of CPS are collected. The repositories should be actively maintained (or at some point) and should have between 100 and 3000 commits. This lead us to a total of 12 repositories. Then, two scripts are created commit_gatherer.py and Issue_gatherer.ipynb to collect issues and commits from our selected GitHub repos and store them in .csv format. Afterwards, the taxonomy is defined and a random sample from the commits of the repositories is created. The commits in the sample are then classified according to our taxonomy using the revers_commit_search.py script to compare the changes.

## Usage
In order to use our mining and sampling methods perform the following steps.
1. First you have to define a list of public GitHub repositories you want to mine. Save all those repositories in an CSV file in the same as this example: [repositories.csv](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/repositories.csv).
2. Then execute the commit_gatherer.py replacing the path ot the "Additional Resources/repositories.csv" with the path to you repositories-csv-file. This will give you a set of csv files, one listing commits for each of your repositories.
3. In the next step you will sample a number of commits from the previously extracted commit changes list with the Sample.ipynb code.
4. Then execute the reverse_commit_search.py script in order to extract the code before and after of each sampled commit. The code will create a folder for each commit and saves theses before and after files in there.
5. The next step is to manually analyse the extracted code snippets and classify them based on the taxonomy provided in the "Taxonomy" tap of the [Results of example classification](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/HCIRevivalGroup%20Classification%20of%20Commit%20Changes.xlsx).

## Use Projects' Results in Bug Prediction
The future goal of the project is that bugs in commits for CPS can be predicted. In order to do so a ML pipeline will be set up, that uses the result of the bug classification that was described before. With the data that is already available one can try to build a model wheter a change is a particular change type. But the model gets far more useful when it can predict what change type a given change is. Therefore we aim to have a multiclass classification model instead of a binary classification model. In order to build such a model the following improvements of the data is recommended:
1. More data: Currently there are 100 classified datapoints and 49 different change types the future system should be able to predict. In order to build a good model there should be at least some dozens of examples for every change type.
2. Higher quality: In order to classify such an amount of data, there should be clear guidelines how to label them. Different people might classify the same example differently. In order to avoid this it is proposed to establish clear guidlines with criteria on how to derive a certain label.
3. More features: The current dataset contains information about the commit, such as the commit message. The model to be build will probably perform better if this data is further preprocessed or additional data can be used. We recommend to either do some NLP and sentiment analysis on the commit messages or build use some tool like change distllier to provide the model with information about the actual code change.

### Additonal Resources
- [Midterm Presentation](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/SoftMain_HCIRevivalGroup_Change%20Analysis%20%26%20Bug%20Detection%20for%20CPS%20Dev_MidtermPresentation.pdf)
- [Final Presentation](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/SoftMain_HCIRevivalGroup_Change%20Analysis%20%26%20Bug%20Detection%20for%20CPS%20Dev_Final.pdf)
- [GitHub repositories used for example classification](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/HCI%20Revival%20Group%20Notes.pdf)
- [Results of example classification](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/HCIRevivalGroup%20Classification%20of%20Commit%20Changes.xlsx)

# Example Data for Change Analysis and Bug Detection for Cyber-Physical Systems (CPS)

The following GitHub repository contains several methods to extract commit changes and issues from any GitHub repository. These methods only require the URL of the corresponding GitHub repository(ies).

## Goal of Repository
We created this repository as part of a university project. The project's aim was to analyse a set of GitHub repositories of CPS projects to classify a set of commits based on their changes. This set of classified changes can then be used to train ML based bug prediction algorithms for the correct interpretation of commit changes. The result of classified commit changes provides a high and low level change classification as well as the significance of such a change. In the following you can see an extract of the results:
![ClassificationExample](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/ClassificationExample.png)

## Motivation of Project
As mentioned above for each analysed commit change, we provided a significance level. Understanding the significance of a certain commit change is particularly important for CPS projects, because of the various effects such a code change may impose on the CPS. There are various examples of catastrophic consequences of unmonitored or unintentional code changes such as the Boeing 747 Max crashes in 2019 or Tesla's autopilot crash. Detecting bugs early, for instance as part of continuous integration, contributes significantly to the quality of code as well as to the efficiency of software and hardware. Also, analysing the code history of projects does not only improve aforementioned points, but also reduces development and maintenance costs. 

## Study Definition & Planning
The main focus of the project is to specify a taxonomy specifically for CPS code changes & bugs. Our research questions are 
a) to understand how bugs/code changes affect CPS 
b) to specify and categorize significant and behavioral CPS code changes and
c) to recognize critical changes affecting the behavior of functionality.
The approach to create the taxonomy is the following: first, several GitHub repositories of CPS are collected. Then, two scripts are created MENTION SCRIPTS to collect issues and commits from our selected GitHub repos and store them in .csv format. Finally, the issues and commits are combined with the timestamp and commitID

```bash
scripts
```

## Usage
run the scripts like so:
```python
import foobar

foobar.pluralize('word') # returns 'words'
```

### Additonal Resources
- [Midterm Presentation](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/SoftMain_HCIRevivalGroup_Change%20Analysis%20%26%20Bug%20Detection%20for%20CPS%20Dev_MidtermPresentation.pdf)
- Final Presentation: LINK
- [GitHub repositories used for example classification](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/HCI%20Revival%20Group%20Notes.pdf)
- [Results of example classification](https://github.com/mboeke/hcirevivalgroup/blob/main/Additional%20Resources/HCIRevivalGroup%20Classification%20of%20Commit%20Changes.xlsx)

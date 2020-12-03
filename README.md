# Example Data for Change Analysis and Bug Detection for Cyber-Physical Systems (CPS)

The following GitHub repository contains several methods to extract commit changes and issues from any GitHub repository. These methods only require the URL of the corresponding GitHub repository(ies).

## Goal of Repository
We created this repository as part of a university project. The project's aim was to analyse a set of GitHub repositories of CPS projects to classify a set of commits based on their changes. This set of classified changes can then be used to train ML based bug prediction algorithms for the correct interpretation of commit changes. The result of classified commit changes provides a high and low level change classification as well as the significance of such a change.
***INSERT EXAMPLE***

## Motivation of Project
As mentioned above for each analysed commit change, we provided a significance level. Understanding the significance of a certain commit change is particular important for CPS projects, because of the various effects such a code change may impose on the CPS.

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
- [Midterm Presentation](./SoftMain_HCIRevivalGroup_Change Analysis & Bug Detection for CPS Dev_MidtermPresentation)
- Final Presentation: LINK
- GitHub repositories used for example classification: LINK
- Results of example classification: LINK

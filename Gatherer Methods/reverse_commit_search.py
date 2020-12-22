## pip install pydriller

## The method reverse_commit_search goes through all sampled commit changes "Sample_Commits.csv" and extracts the code of each file of each commit
## before and after the actual commit, so that the code of each file can be compared before and after the commit.

from pydriller import RepositoryMining
import pandas as pd
import os
import csv

repositories = pd.read_csv("Additional Resources/repositories.csv")
commits = pd.read_csv("Commit_CSVs/Sample_Commits.csv")

current_directory = os.getcwd()


for c in range(0, commits.shape[0]):
    try:
        os.mkdir(current_directory + '/changes/{0}'.format(c))
        print('Created folder {}'.format(c))
    except:
        print('Overwritten folder {}'.format(c))

counter = 0

for key, commit in commits.iterrows():
    repo = commit['Repository']
    for commit_obj in RepositoryMining(path_to_repo = repositories[repositories.Name == repo].URL.values[0], only_commits = [commit['Commit_ID']]).traverse_commits():
        for m in commit_obj.modifications:
            with open("changes/{}/{}_before.txt".format(counter, m.filename), "w+") as text_file:
                text_before = m.source_code_before if m.source_code_before is not None else 'file did not exist'
                text_file.write(text_before)
            with open("changes/{}/{}_after.txt".format(counter, m.filename), "w+") as text_file:
                text_after = m.source_code if m.source_code is not None else 'file removed'
                text_file.write(text_after)

    counter += 1

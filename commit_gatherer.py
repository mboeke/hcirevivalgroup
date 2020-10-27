## pip install pydriller

from pydriller import RepositoryMining
import pandas as pd
import csv
import time

repositories = pd.read_csv("repositories.csv")

files = []
for key, repository in repositories.iterrows():
    print('Gathering commits for {}'.format(repository['Name']))
    with open('Commit_CSVs/Commit_CSVs_{}.csv'.format(repository['Name']), 'w+', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['Contributor', 'Date', 'Message', 'Files']  # without 'Id' for now
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for commit in RepositoryMining(repository['URL']).traverse_commits():
            curr = []
            for modified_file in commit.modifications:
                if modified_file.filename != '__init__.py':
                    curr.append(modified_file.filename)
            writer.writerow({
                'Contributor': commit.author.name,
                'Date': (str(commit.committer_date)[:10]),
                'Message': commit.msg,
                'Files': [','.join(curr)]})
    time.sleep(10)
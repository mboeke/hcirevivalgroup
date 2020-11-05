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
        fieldnames = ['Commit_ID','Contributor', 'Date', 'Message', 'Files']  # without 'Id' for now
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        bug_commits = []
        for commit in RepositoryMining(repository['URL']).traverse_commits():
            curr = []
            for modified_file in commit.modifications:
                if modified_file.filename != '__init__.py':
                    curr.append(modified_file.filename)
            commit_mess = commit.msg.replace('\n','')
            commit_mess.replace('\t', '')
            writer.writerow({
                'Commit_ID': commit.hash,
                'Contributor': commit.author.name,
                'Date': (str(commit.committer_date)[:10]),
                'Message': commit_mess,
                'Files': [','.join(curr)]})
            if any(word in commit.msg.lower() for word in ['bug', 'error', 'problem']):
                bug_commits.append([commit.hash, commit.author.name, (str(commit.committer_date)[:10]), commit_mess, [','.join(curr)]])

    with open('Commit_CSVs/Bug_Commit_CSVs_{}.csv'.format(repository['Name']), 'w+', newline='',encoding="utf-8") as csvfile:
        fieldnames = ['Commit_ID', 'Contributor', 'Date', 'Message', 'Files']  # without 'Id' for now
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(bug_commits)
    time.sleep(10)
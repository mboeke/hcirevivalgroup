## pip install pydriller

from pydriller import RepositoryMining
import pandas as pd
import csv

repositories = pd.read_csv("repositories.csv")

files = []
ignore_filenames = ['__init__.py', 'readme.md', '.gitignore', '', '__main__.py']
for key, repository in repositories.iterrows():
    print('Gathering commits for {}'.format(repository['Name']))
    with open('Commit_CSVs/Commit_CSVs_{}.csv'.format(repository['Name']), 'w+', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['Commit_ID','Contributor', 'Date', 'Message', 'Files', 'Branch','Repository']  # without 'Id' for now
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        bug_commits = []
        # print(RepositoryMining(repository['URL']).branches())
        for commit in RepositoryMining(repository['URL']).traverse_commits():
            curr = []
            for modified_file in commit.modifications:
                # ignore certain files common on each git repo, but unnecessary
                if modified_file.filename.lower() not in ignore_filenames:
                    curr.append(modified_file.filename)
            commit_mess = commit.msg.replace('\n','')
            commit_mess.replace('\t', '')
            if len(curr) in range(1, 11):
                writer.writerow({
                    'Commit_ID': commit.hash,
                    'Contributor': commit.author.name,
                    'Date': (str(commit.committer_date)[:10]),
                    'Message': commit_mess,
                    'Files': [','.join(curr)],
                    'Branch': str(commit.branches),
                    'Repository': repository['Name'],
                })
            if any(word in commit.msg.lower() for word in ['bug', 'error', 'problem']):
                bug_commits.append([commit.hash, commit.author.name, (str(commit.committer_date)[:10]), commit_mess, [','.join(curr)]])

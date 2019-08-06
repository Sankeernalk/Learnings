from git import Repo

repo_dir = '/Users/sankeernalk/Desktop/git/GitFirstRepository'
repo = Repo(repo_dir)
file_list = [
    '/Users/sankeernalk/Desktop/git/GitFirstRepository/summary_momeric.txt'
]
commit_message = 'Add simple regression analysis1'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
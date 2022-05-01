GIT WORKFLOW
============
Step 1) git clone (repositry name) | This is to bring a repo from remote github repo onto local laptop directory
example: git clone <python-basic-programs http link from github>

Step 2) modify or add files to the repo and then use `git add`
  example: git add <file name>

Step 3) check the status and commit all added files to local repo by using git commit
example : git commit -m "commit message. what is is for"
example : git commit;  this will pop up an editor to type the commit message

Step 4) Verify the committed files using git log
example: git log

Step 5) Create a new branch out of master for pushing
example: git branch;  check which branch you are in , it should be master
         git branch <new branch name>

Step 6) Now switch to the new branch you created above
    example: git checkout <branch name>

Step 7) All committed files needs to be pushed to remote repo using git push;
git push <remote_URL/remote_name> <branch> | This is to push any changes made in the local branch to remote repo
example : git push origin HEAD:<branch_name>

Step 8) go to github UI from web and you will have to add reviwers and merge the branch to master in the web UI itself

Step 9) delete branch in UI. switch to master branch and delete pushed branch. Then use git pull on master branch to keep it up to date
example : git checkout master
	  git branch -D <branch_name>
	  git pull  

Additional commands
===================

Step 1) git pull <branch_name> <remote_URL/remote_name> | This is to recive any changes made in the remote branch that you do not have in your local
example: >>> git pull origin master

Step 2) git status | This is to check if you are up to date with the branch you are in. If you are not, then it will tell you what files are not updated.


Step 3) git branch ; shows in which branch you are currently in. Or can be used to create a new branch
example : git branch
example : git branch <branch_name>


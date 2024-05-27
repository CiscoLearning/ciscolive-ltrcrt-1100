# !!!!!!
# NEEDS IMAGES - CHECK LAB GUIDE. NOT READY - COMPARE STEPS ALSO
# !!!!!!





In the previous task, the merging went through successfully without a need to resolve any conflicts   because you had made changes to the file only in one of the branches. At some point you will have a merge conflict, where you may have made overlapping changes to a file and Git cannot automatically merge the changes. 
Activity
1.	Create a new branch and switch to it. 
$ git branch test
$ git checkout test 
Switched to branch 'test'
2.	Open my_file.txt in Visual Studio Code and change the word boss to novice. Then save the file.
$ code my_file.txt
 
3.	Stage and commit your changes in your new branch.
$ git add my_file.txt
$ git commit -m "Modified from boss to novice"
[test 06cc0c2] Modified from boss to novice
 1 file changed, 1 insertion(+), 1 deletion(-)
Note: If you want to add and commit your changes using a single command, you can use the option -a with the git commit command. 
$ git commit -am “my message”
Git then automatically stages files that have been modified or deleted.
4.	Switch to the main branch and modify the file my_file.txt by changing the word boss to beginner.
$ git checkout main
Switched to branch 'main'
 
5.	Stage and commit your changes in the main branch.
$ git add my_file.txt 
$ git commit -m "Modified from boss to beginner"
[main bedec8d] Modified from boss to beginner
 1 file changed, 1 insertion(+), 1 deletion(-)
6.	Review the difference between the two branches with the git diff command. You can see that we have been editing the same word on separate branches with different results.
$ git diff test
diff --git a/my_file.txt b/my_file.txt
index 7199b6b..2d236d0 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1,2 +1,2 @@
 I am learning Git!
-I am a Git novice!
+I am a Git beginner! 
7.	Try to merge the branches with the git merge command as you did in the previous task.
$ git merge test
Auto-merging my_file.txt
CONFLICT (content): Merge conflict in my_file.txt
Automatic merge failed; fix conflicts and then commit the result.
8.	Because there is a conflict, Git cannot merge the two branches together automatically. Therefore, you need to fix the conflict manually. Use Visual Studio Code to select the change you would like to keep.
 
Note: To solve the conflict, you could also use a tool other than Visual Studio Code, even a command line-based text editor.
9.	After choosing one of the options (Accept Current Change, Accept Incoming Change, or Accept both Changes), save the file.
10.	Check the Git state with the git status command.
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
11.	Now that you have fixed the conflicts, follow the Git instructions provided in the git status output: Mark the conflicts   for resolution with git add and then run git commit.
$ git add my_file.txt
$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)
$ git commit -m "Resolving the merge conflict"
[main 597756b] Resolving the merge conflict
12.	When the merge is successful, remove your feature branch.
$ git branch -d test
Deleted branch test (was e255ebe).

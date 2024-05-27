So far in the tasks, you have worked on the main branch. In practice, you would usually use branches and merge them into your default branch when your changes are ready. 
Suppose you are working on a new feature. You might need to improve the structure of some of your code (refactor), and you want to be able to check in your changes as you make progress. However, you don’t want to limit yourself and prevent easy changes to your production code. To manage this situation, you need to isolate your changes, and you can do that with Git branching. 
Activity

1.	Create a new branch, using the git branch command with the name of the new branch.
$ git branch practice

2.	Use git branch to see all the branches that have been created.
$ git branch
* main
  practice

3.	You have two branches, and your current branch is marked with an asterisk. Change to the newly created branch by using the command git checkout.
$ git checkout practice
Switched to branch 'practice'

Note: You can use the option -b with git checkout to simultaneously create and check out the new branch: git checkout -b practice

4.	Add some more text to your my_file.txt file.
$ echo "I am a Git boss!" >> my_file.txt

5.	Add and commit your changes. You can also use git status to verify the Git state. It should show that your changes are occurring in your new branch instead of in the main branch.
$ git add my_file.txt
$ git status
On branch practice
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   my_file.txt

$ git commit -m "Added a comment in the practice branch"
[practice 8130876] Added a comment in the practice branch
 1 file changed, 1 insertion(+)

6.	Switch back to the main branch by using the git checkout command.  
Step help [for Harness]
$ git checkout main
Switched to branch 'main'

7.	Check the differences between the two branches by using git diff. You can use the command to compare the branches in the same way that you used it earlier to compare files and commits in the main branch. Refer to git diff --help if necessary.
Step help [for Harness]
$ git diff main practice 
diff --git a/my_file.txt b/my_file.txt
index 97555a7..a544d86 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1 +1,2 @@
 I am learning Git!
+I am a Git boss!

8.	Merge the content from the practice branch to the main branch. Use the command git merge with the name of the branch that you would like to merge with the current branch.
$ git merge practice
Updating a18f65e..8130876
Fast-forward
 my_file.txt | 1 +
 1 file changed, 1 insertion(+)

9.	Delete the practice branch by using the option -d with the git branch command.
$ git branch -d practice
Deleted branch practice (was 8130876).

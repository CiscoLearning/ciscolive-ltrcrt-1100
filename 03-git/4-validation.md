Git includes built-in tools for you to verify what has been changed in your files. Because Git has stored the full history of the changes, you can revert to an earlier version if necessary. 
Activity

1.	You may want to review the commit history for a repository. Display the most recent commits with git log.
$ git log
commit aacd4699fba564fcaae0df8ed26ea482e06de13b (HEAD -> main)
Author: Your Name <you@yourdomain.example.com>
Date:   Thu Dec 9 10:26:19 2021 +0000

    initializing my_file.txt

Note: In the previous task, you looked at the commit hash that Git presented: aacd469. Notice that aacd469 is the first 7 characters of the preceding full commit hash: aacd4699fba564fcaae0df8ed26ea482e06de13b. You can use the option --oneline with git log to see the commits’ short hashes.

2.	Make a change to the Git tracked file my_file.txt. Add a line that says, “At this rate I will be a Git expert in no time”. 
$ echo "At this rate I will be a Git expert in no time." >> my_file.txt

3.	Now when you perform a git status, you see changes in your file. 
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")

4.	What are those changes that you did in the file? Git has a useful command, git diff, that you can use to see the changes. Learn from the documentation how to use this command.
$ git diff --help
GIT-DIFF(1)                         Git Manual                        GIT-DIFF(1)

NAME
       git-diff - Show changes between commits, commit and working tree, etc

SYNOPSIS
       git diff [<options>] [<commit>] [--] [<path>...]
       git diff [<options>] --cached [<commit>] [--] [<path>...]
       git diff [<options>] <commit> <commit> [--] [<path>...]
       git diff [<options>] <blob> <blob>
       git diff [<options>] --no-index [--] <path> <path>

DESCRIPTION
       Show changes between the working tree and the index or a tree, changes
       between the index and a tree, changes between two trees, changes between
       two blob objects, or changes between two files on disk.

       git diff [<options>] [--] [<path>...]
           This form is to view the changes you made relative to the index
           (staging area for the next commit). In other words, the differences
           are what you could tell Git to further add to the index but you still
           haven’t. You can stage these changes by using git-add(1).

<output omitted>

5.	Based on what you learned in the previous step, use git diff to find out what was changed in my_file.txt since the last commit.
$ git diff my_file.txt
diff --git a/my_file.txt b/my_file.txt
index 97555a7..a63eba2 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1 +1,2 @@
 I am learning Git!
+At this rate I will be a Git expert in no time.

6.	You have now verified that the changes are fine. Proceed to stage your changes   with git add and use git commit to commit these new changes.   

Step help:
$ git add my_file.txt
$ git commit -m "Adding observation"

7.	Use git log to see the changes in the commit history. Test   the option --oneline to get output with reduced information.
$ git log --oneline
5693486 (HEAD -> main) Adding observation
aacd469 initializing my_file.txt

8.	You can use git diff in multiple ways, as you saw in the documentation. Using the information from the documentation, compare the changes between the two latest commits.
$ git diff aacd469 5693486
diff --git a/my_file.txt b/my_file.txt
index 97555a7..a63eba2 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1 +1,2 @@
 I am learning Git!
+At this rate I will be a Git expert in no time.

9.	What if you made a mistake and would like to go back to the previous commit? Use the command git revert to   go back. Start by checking the documentation for how to use this command, and then revert to the previous commit. Note that with the revert command you need to specify the commit which you want to cancel, not the one to which you want to return. This means that to revert to the previous commit, you need to use the hash of the current commit.
$ git revert --help
<output omitted>
$ git revert 5693486  
[main a18f65e] Revert "Adding observation"
 1 file changed, 1 deletion(-)

10.	If you accidentally use a wrong commit hash and the revert fails, you can use the git revert --abort to cancel the operation and try again with the correct commit hash. If you did not get this error, continue to the next step.
$ git revert aacd469
error: could not revert aacd469... initializing my_file.txt
hint: after resolving the conflicts, mark the corrected paths
hint: with 'git add <paths>' or 'git rm <paths>'
hint: and commit the result with 'git commit'
$ git status
On branch main
You are currently reverting commit aacd469.
  (fix conflicts and run "git revert --continue")
  (use "git revert --abort" to cancel the revert operation)

Unmerged paths:
  (use "git reset HEAD <file>..." to unstage)
  (use "git add/rm <file>..." as appropriate to mark resolution)

        deleted by them: my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
$ git revert --abort

11. Close the file that opens in the upper Visual Studio Code window, there is no need to change the commit message.

12. Verify that the reverting worked by using git log. You can also check the content of the file, which should no longer include the line “At this rate I will be a Git expert in no time.”
$ git log --oneline
a18f65e (HEAD -> main) Revert "Adding observation"
5693486 Adding observation
aacd469 initializing my_file.txt
$ cat my_file.txt 
I am learning Git!

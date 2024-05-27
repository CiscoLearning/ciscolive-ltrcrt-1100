Initializing a Git repository doesn’t yet mean that your changes are tracked. You will need to identify   the files that you want to track, and stage and commit them every time you want to save a new snapshot of the files’ current state. 
When you work with Git, it is useful to use git status to often verify the state of Git. Another good habit is to use the --help option of a command whenever you are unsure about what syntax to use for your task. After learning in this task how to use these commands, you can use them also in the upcoming tasks even if they were not explicitly mentioned.
Activity

1. Git, as with many other command-line tools, includes a help option for your reference. Check the common Git commands by using the help option.

```
``$ git --help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

<output omitted>
```

2. git status is a useful command for examining the current Git state. Use the command to show the initial working tree status of your local Git repository.
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)

The response tells you which branch you are on (main) and the status of the paths in your working tree.

3.	You have an initialized but empty repository. Create a new file called my_file.txt in your working directory, ~/git_exercises, with the text “I am learning Git!”
$ echo "I am learning Git!" > my_file.txt

4.	List the files in the directory to verify that the my_file.txt file was successfully created.
$ ls -la
total 8
drwxrwxr-x   3 student student   37 Dec  9 10:21 .
drwx------. 24 student student   4096 Dec  9 09:59 ..
drwxrwxr-x   7 student student   119 Dec  9 10:20 .git
-rw-rw-r--   1 student student   19 Dec  9 10:21 my_file.txt

5.	Use git status to examine the changed Git state. You should see a message like the following:
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        my_file.txt

nothing added to commit but untracked files present (use "git add" to track)

Note: Notice that Git found the new file in the directory and determines that it is not a tracked activity.
To track the file, you will need to add my_file.txt to stage your work, and then commit your work to record changes to the repository.

6.	Stage my_file.txt for the next commit by using git add.
$ git add my_file.txt

7.	How did the Git state change? Verify it with git status.
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   my_file.txt

8.	Before committing your change, add a message with your commit to explain your changes. Use git commit --help to find the option to include your message.
$ git commit --help
GIT-COMMIT(1)                                                                                         
NAME
       git-commit - Record changes to the repository

SYNOPSIS
       git commit [-a | --interactive | --patch] [-s] [-v] [-u<mode>] [--amend]
                  [--dry-run] [(-c | -C | --fixup | --squash) <commit>]
                  [-F <file> | -m <msg>] [--reset-author] [--allow-empty]
                  [--allow-empty-message] [--no-verify] [-e] [--author=<author>]
                  [--date=<date>] [--cleanup=<mode>] [--[no-]status]
                  [-i | -o] [--pathspec-from-file=<file> [--pathspec-file-nul]]
                  [-S[<keyid>]] [--] [<pathspec>...]

DESCRIPTION
<output omitted>

OPTIONS
<output omitted>
       -m <msg>, --message=<msg>
           Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.

Note: When you are not sure about how to use a certain Git command, you can check the documentation by using the --help option.

9.	Based on what you learned in the previous step, commit your changes with a simple, descriptive message.
$ git commit -m "initializing my_file.txt"
[main (root-commit) aacd469] initializing my_file.txt
 1 file changed, 1 insertion(+)
 create mode 100644 my_file.txt
Note: aacd469 contained in [main (root-commit) aacd469] is your commit’s unique hash. Every commit is identified by a unique SHA1 hash, so your commit ID will be different from what you see here.

10.	Verify the Git state with git status to verify that there are currently no more changes to be committed.
On branch main
nothing to commit, working tree clean

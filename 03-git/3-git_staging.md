# Hands on - Add, Remove, and Commit files with Git

![line](../assets/banner.png)

## What are we doing?

- Add files to your local Git staging area.
- Remove files from the Git repository.
- Commit changes to your local Git repository.


## Task 4: Track a file locally

1. In the Visual Studio Code terminal, change directory to the cloned git repository if you have not already done so:

```shell
cd ~/learning-git
```

2. In the terminal, create a new file named **new_file.txt** that contains the text "I am learning Git!":

```shell
echo "I am learning Git!" > new_file.txt
```

3. Verify the file was created by using the **ls** command:

```shell
ls
```

Your output should match the following:

```text
new_file.txt  README.md
```

4. Use the **git status** command to see that the new file exists but is not being tracked by Git:

```shell
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

*Notice that Git has identified the presence of **new_file.txt**, but the output from **git status** tells you that the file is not being tracked.*

5. Use the **git add** command to add the new file to the staging area. This command instructs Git to begin tracking the file. Remember that adding a file to the staging area does NOT add the file to the repository - you will do that in a later task.

```shell
git add new_file.txt
```

6. Verify that the file has been added to the staging area by using the **git status** command:

```shell
git status
```

Your output should match the following:

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   new_file.txt
```

*Note that **new_file.txt** is now listed as a "change to be committed"

**Now that you had added a new file to the staging area, proceed to the next task to remove an existing file from the repository**

## Task 5: Remove files from the local Git working area

1. Use the **ls** command to identify the files in your local working directory:

```shell
ls
```

```text
new_file.txt  README.md
```

2. You have decided that the README.md file is no longer needed. Use the **git rm** command to remove the file from the working directory:

```shell
git rm README.md
```

3. Use the **ls** command once more and note that the file is no longer present:

```shell
ls 
```

```text
new_file.txt
```

*NOTE: If you are working in a production environment and only wish to remove the file from the working area **without** actually deleting the file, you can use the `--cached` option to **git rm**: `git rm --cached README.md`*

4. Use the **git status** command to verify that the file will be deleted from the repository when you commit the changes:

```shell
git status
```

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    README.md
        new file:   new_file.txt
```

5. Notice that two changes are pending and will be applied when you perform a commit:

- Delete the README.md file from the repository
- Add the **new_file.txt** file to the repository

**Proceed to the next task to commit your changes to the local repository**


## Task 6: Commit changes to the local Git repository

1. You ended the previous task with two changes pending to be committed. Use the **git commit** command to commit those changes to your local repository. Note that, by default, a **commit** requires a *message* to be added. The message should note the changes being made, and will appear in the git log:

```shell
git commit -m "Remove README and add a new file"
```

Your output should be similar to the following:

```text
[main db0d07a] Remove README and add a new file
 2 files changed, 1 insertion(+), 92 deletions(-)
 delete mode 100644 README.md
 create mode 100644 new_file.txt
```

2. Use the **git status** command to verify that no changes are pending:

```shell
git status
```

Your output should match the following:

```text
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

3. Use the **ls** command to verify the README file is not present:

```shell
ls
```

```text
new_file.txt
```

![line](../assets/banner.png)

Before continuing to the next task, you should have completed the following:

* [x] **Created a new file named `new_file.txt` and added it to the local staging area**
* [x] **Removed the `README.md` file from the local working tree**
* [x] **Committed changes to your local repository**
* [x] **Verified the changes at each step using the `git status` command**

**Congratulations! You have added a new file to your staging area, committed it to the repository, and deleted a file from the local repository. Continue to the next page to learn how to reflect these changes in the remote repository**

![line](../assets/banner.png)

<p align="center">
<a href="2-gitlab_repo.md"><img src="../assets/previous.png" width="150px"></a>
<a href="4-git_remotes.md"><img src="../assets/next.png" width="150px"></a>
</p>
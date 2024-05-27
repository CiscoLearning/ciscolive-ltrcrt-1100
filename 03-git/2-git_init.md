When you start using the Git distributed version control on your local system, there are a couple of things you need to start with. First, the first time you work with Git on your local system, you need to set your name and email address. This information will be visible in the history of changes that you have made.
Second, you will want to initialize a Git repository for your project. Then you can start tracking your changes in the later tasks of this Lab.
Activity
	
1. Start using the Git version control by setting the name and email address that other collaborators will see. Define your name and email address with git config.  
$ git config --global user.name "Your Name"
$ git config --global user.email you@yourdomain.example.com

2. Verify your current configuration by listing the variables that are set in your Git config file with git config -l. The information that you provided in the previous step is displayed.
$ git config -l
user.name=Your Name
user.email=you@yourdomain.example.com

3. Initialize an empty Git repository with git init.
$ git init
Initialized empty Git repository in /home/student/git_exercises/.git/

4. You have created a local repository within your project that is contained in the hidden directory .git. This directory is where your change history is located. You can verify the existence of the new directory by listing all the directory contents with option -a, which will also include the hidden entries.
$ ls -a
.  ..  .git

5. Define the name of your initial Git branch as main. Branching is discussed in more detail in a later part of this Lab  . Until then, all the version control will occur in this single main branch. 
$ git checkout -b main
Switched to a new branch 'main'


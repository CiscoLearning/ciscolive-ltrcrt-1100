# 0. Connect to the lab environment
![line](../assets/banner.png)

In this lab, each participant receives their own Pod. Each pod includes a Linux development host and a GitLab instance.

![line](../assets/banner.png)

## Connect to your environment using Visual Studio Code remote SSH extension

> **Note**: You should have a physical token at your workstation engraved with your Pod number. If you do not have a token, please let your instructors know and you will be issued one.

**STEPS:**

<table>

<tr><th>Step</th><th width=50%>Description</th><th>Screenshot / code snippet</th></tr>

<tr><td>1.</td><td>

Open the Microsoft Visual Studio Code application from your desktop.

</td><td>

![Visual Studio Code logo](./images/01-vscode-icon.png)
</td></tr>

<tr><td>2.</td><td>

To connect to your Linux Developer VM, click the green icon on the left bottom of Visual Studio Code application.

</td><td>

![Connect](./images/02-vscode-remotessh.png)

</td></tr>

<tr><td>3.</td><td>

Select `Connect to Host...`.

</td><td>

![Connect](./images/03-vscode-connect.png)

</td></tr>
<tr><td>4.</td><td>
    
Fill in the connection details to your Pod's Developer VM: `auto@pod<xx>-xelab.cisco.com` where `<xx>` should be replaced with the number of your pod. For example Pod 50 would be `auto@pod50-xelab.cisco.com`.

> **Note**: If you are prompted to select the platform of the remote host, click `Linux`.

</td><td>

![connect](./images/04-vscode-ssh.png)

</td></tr>
<tr><td>5.</td><td>

If prompted to verify the Fingerprint, click `Continue`.

</td></tr>
<tr><td>6.</td><td>

Fill in the password that the instructor has provided you.


</td></tr>
<tr><td>7.</td><td>

After Visual Studio Code has copied necessary files for the remote session, the window will update to match the settings on the developer VM. You can verify that you are connected the correct pod in the lower-left corner of the Visual Studio Code window.

> **Note**: If the terminal view does not show up automatically, you can open it from the top menu of Visual Studio Code application: `Terminal` > `New terminal`
</td><td>

![Overview](./images/05-vscode-terminal.png)

</td></tr>
</table>


## Visual Studio Code tips

Throughout this lab, you will work in the Visual Studio Code terminal using the SSH extension that you set up in this preparation task.

- You can open a file from Visual Studio Code's terminal with the command `code`.
    ```bash
    code filename.py
    ```

You can open multiple Visual Studio code terminals. This might be useful when you need to leave something running such as a Python application or a Docker container, but want to run other scripts at the same time.

![visual studio code terminals](./images/06-vscode-multiple-terminals.png)

## Checklist before continuing

Before continuing to the next task, you should have completed the following:

* [x] **Connected to your pod using Visual Studio Code remote SSH extension**


![line](../assets/banner.png)
<p align="center">
<a href="../README.md"><img src="../assets/previous.png" width="150px"></a>
<a href="../01-intro-apis/1.md"><img src="../assets/next.png" width="150px"></a>
</p>

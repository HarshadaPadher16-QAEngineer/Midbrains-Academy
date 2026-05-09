       Step 1: Generate a GitHub Token (PAT)
  - GitHub no longer accepts your regular password for pushing code. You must use a Token.
  - Log in to GitHub and go to Settings (click your profile photo).
  - On the left sidebar, click Developer settings (at the very bottom).
  - Click Personal access tokens > Tokens (classic).
  - Click Generate new token > Generate new token (classic).
  - Note: Enter a name like "Eclipse_Selenium_Push".
  - Scopes: Check the box for repo (this allows pushing code).
  - Click Generate token at the bottom.
  - Copy the Token immediately! You won't see it again.

       Step 2: Configure Author Identity in Eclipse
  - Eclipse needs to know who is committing the code.
  - In Eclipse, go to Window > Preferences.
  - Navigate to Version Control > Git > Configuration.
  - Click Add Entry... and add these two:
  - Key: user.name  | Value: Harshada Padher
  - Key: user.email | Value: [Your GitHub Email]
  - Click Apply and Close.

        Step 3: Prepare the Project for Git
  - Right-click your project in Eclipse.
  - Select Team > Share Project...
  - Select Git and click Next.
  - Click Create Repository and then click Finish.
  - Your files will now show a [?] icon, meaning they are ready to be tracked.

        Step 4: Commit and Push to GitHub
  - Right-click your project > Team > Commit.
  - The Git Staging tab will open at the bottom.
  - Stage Files: Drag all files from Unstaged Changes down to Staged Changes (or click the ++ icon).
  - Message: Type a commit message (e.g., "Initial push for Midbrain Academy project").
  - Commit & Push: Click the Commit and Push button.

        Step 5: Authentication (The Token Part)
  - A window will pop up asking for the destination:
  - URI: Paste your GitHub Repository URL (e.g., https://github.com/HarshadaPadher16-QAEngineer/Midbrains-Academy.git).
  - User: Type your GitHub Username.
  - Password: DO NOT enter your account password. Paste the Token (PAT) you copied in Step 1.
  - Check the box Store in Secure Store (so you don't have to type it again).
  - Click Next > Next > Finish.
  - Summary of the Workflow
  - Token: Acts as your secure password for Eclipse.
  - Add/Stage: Picks the files you want to upload.
  - Commit: Saves the version on your computer.
  - Push: Sends the version to the GitHub website.

         Note: Since your Midbrains-Academy repository already exists, Eclipse might ask you to "Pull" or "Rebase" first if there are files online that are not on your computer. Always click Preview and then Push to complete the process!

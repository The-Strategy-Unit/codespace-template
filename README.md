# R & Python Codespaces Template
 
This repository is a starting point for working in either **R** or **Python**, using [GitHub Codespaces](https://github.com/features/codespaces) — a way to code in your browser (or VS Code) without installing anything on your own computer.

 
You don't need to have R, Python, RStudio, or any package managers installed on your machine. Everything runs in the cloud, inside a ready-made environment.
 
You get to choose which language you want to work in each time you start a new codespace.
 
---
 
## What is a Codespace?
 
A **codespace** is a temporary, cloud-based computer that GitHub creates for you, pre-installed with everything needed for a project. Think of it as a fresh laptop that already has all the right software on it, accessible through your web browser.
 
This repository is set up so that when you create a codespace, GitHub will ask you **which environment you want**: R or Python.
 
---
 
## Step 1: Copy this repository to your own account

1. Click the green **Use this template** button near the top of the page.
2. Select **Create a new repository** from the dropdown.
3. Follow the instructions on the **Create a new repository** page. Keep the repository name the same (`codespace-template`). Select if you want a "Public" or "Private" repo. Click the "Create repository" button.

You should now have a copy of this repository at https://github.com/YOUR-GITHUB-USERNAME/codespace-template

## Step 2: Create your codespace

The easiest way to start is to use one of the two links below. ⚠️ It is important that you replace the value in YOUR-GITHUB-USERNAME with your actual GitHub username!

- 🅁 **Open an R codespace**: https://codespaces.new/YOUR-GITHUB-USERNAME/codespace-template?devcontainer_path=.devcontainer/r-rstudio/devcontainer.json
- 🐍 **Open a Python codespace**: https://codespaces.new/YOUR-GITHUB-USERNAME/codespace-template?devcontainer_path=.devcontainer/python-uv/devcontainer.json
 
Clicking a link will take you to a "Create codespace" page with the correct configuration already selected. Click **Create codespace** to continue. GitHub will now build your environment — this can take a few minutes the first time, so feel free to make a cup of tea. Later codespaces will start faster.
 
### Alternative: creating a codespace manually
 
If you'd rather use the repository's **`<> Code`** button instead of the links above:
 
1. Click the green **`<> Code`** button, then select the **Codespaces** tab.
2. **Do not click "Create codespace on main"** — this quick option skips the language choice and may create the wrong environment.
3. Instead, click the **`...`** (three dots) in the top corner of the panel, and choose **"New with options..."**.
4. Under **Dev container configuration**, choose either:
   - **R (rocker/r-ver + RStudio)**
   - **Python (uv)**
5. Click **Create codespace**.
 
## Step 3a: Using the R environment
 
If you chose **R (rocker/r-ver + RStudio)**:
 
- Once the codespace has finished building, look for a notification or a **"Ports"** tab in VS Code, and find the port labeled **RStudio IDE** (port `8787`).
- Click the little globe/browser icon next to it, or open the forwarded address, to open **RStudio** in a new browser tab.
- You'll now have a full RStudio interface, with the following R packages already installed and ready to use:
  - `tidyverse`
  - `lubridate`
  - `here`
  - `languageserver`
- You can write and run R code directly in RStudio's console, or create `.R` script files.
**No installation needed** — R, RStudio, and these packages are already set up for you.
 
---
 
## Step 3b: Using the Python environment
 
If you chose **Python (uv)**:
 
- Once the codespace has finished building, open a terminal in VS Code (menu: **Terminal → New Terminal**, or press `` Ctrl+` ``).
- This environment uses a tool called **[uv](https://docs.astral.sh/uv/)** to manage Python and its packages. You don't need to install Python yourself — uv takes care of it.
- To check everything is working, type:
```
  uv --version
```
- To run a Python project in this repository, type:
```
  uv sync
```
  This installs the exact Python version and packages the project needs.
- To run a Python script, use:
```
  uv run python your_script.py
```
 
You'll write and edit your Python files directly in the VS Code editor in your browser, and run them using the terminal.
 
---
 
## Which one should I pick?
 
- Choose **R** if you're doing statistics, data analysis with the tidyverse, or want an RStudio-style interface.
- Choose **Python** if you're writing Python scripts, doing general programming, or want a lightweight, fast-to-set-up environment.
You can always delete your codespace and start a new one with the other language — nothing you do in one codespace affects your ability to create the other.
 
---
 
## Stopping and deleting your codespace
 
Codespaces don't run forever, and they use up free monthly quota, so it's good practice to stop them when you're done:
 
1. Go to [github.com/codespaces](https://github.com/codespaces) to see all your active codespaces.
2. Click the **`...`** next to your codespace and choose **Stop codespace** (pauses it — you can resume later) or **Delete** (removes it completely).
A codespace will also stop automatically after a period of inactivity.
 
---
 
## Troubleshooting
 
- **Nothing happens when I click Create codespace** — try refreshing the page, or check you're signed in to GitHub.
- **I don't see a choice between R and Python** — use "Configure and create codespace" instead of the default quick-create button (see Step 1).
- **RStudio tab won't open** — check the **Ports** panel in VS Code and make sure port `8787` shows as forwarded; click it again to reopen the tab.
- **`uv: command not found`** — close and reopen the terminal, as the codespace may still be finishing setup.
If you're stuck, it's worth pasting the exact error message into a search engine — most Codespaces issues are common and well documented.
 
 ## Acknowledgements

 The R codespace container and the layout of this repository was based on https://github.com/wykhuh/r-rstudio-codespace. Claude Code was used to advise on the creation of the Python codespace container and write the README.

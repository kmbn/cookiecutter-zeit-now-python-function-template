# Zeit Now Python Function Template
This Cookiecutter template generates a basic Now serverless Python function project. The resulting project can be deployed immediately to Zeit Now.

## Requirements
Before using this template you will need to:
1. Install Cookiecutter
2. Install the Now desktop app, which also installs the Now CLI
3. Create a (free) Zeit Now account

## How to Use
Run this command to get the template. Cookiecutter will download it and then run it.

```bash
cookiecutter https://github.com/kmbn/cookiecutter-zeit-now-python-template
```
(After you've run this command once, the template will be cached locally and you can run it again with just the template name: `cookiecutter cookiecutter-zeit-now-python-template`. You can also create an alias for the name so you don't have to type it out each time.)

Enter a name for your app at the prompt.

Cookiecutter will create a directory with the same name as the app. Change to it:
```bash
cd <name-of-app>
```

Run Now:
```bash
now
```
(If you are not logged in, you will be prompted to log in first.)

Now will deploy your app and copy the URL to your clipboard. Copy/paste it into your browser's address bar and you'll see `Hello world!`.

## Developing Your Function
The template also includes `pre-commit` hooks and configuration files for linting your code as well as a starter test to run with `pytest` (included in `dev-requirements.txt)`. All of this is optional—the pre-commit hooks and tests are not required for deploying to Now and none of the additional files are uploaded to Now. The additional files are all excluded by the `.nowignore` file included in the template. The `.nowignore` file works like a `.gitignore` file (except for Now rather than Git). The template also includes a `.gitignore` file as well.

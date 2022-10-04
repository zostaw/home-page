# home-page
This is source code for my personal home page.

It does not keep track of venv, so requirements.txt must be updated accordingly.

## PREREQUISITES
- python 3.10.5

## INSTALLATION

1. go to parent directory for your project. In example, home directory is used (new directory "home-page" will be created inside).
```
cd ~/
```

2. initiate local repo and load this project
```
git clone git@github.com:zostaw/home-page.git
```

3. prepare python virtualenv
3.1 install
There are multiple options, I present below 2 most common.

a) simpliest to install, but more difficult to update:
```
python3 -m venv venv
```
b) suggested option - download pyenv - it is a little bit longer for the first time, but once it is installed, managing multiple python versions and virtualenvs comes with much more comfort - see installation guide under https://www.linuxtut.com/en/c8b82ab42564256df884/
Once pyenv is installed, execute:
```
# install python version in pyenv
pyenv install 3.10.5
# create venv for your project
pyenv virtualenv 3.10.5 home-page
# list all pyenv virtualenvs
pyenv activate home-page
# activate for your python project
pyenv local home-page
```
That prepared virtualenv will stick with the directory and it is simple to change versions.

3.2. install python requirements

a) simple option - one must execute this command everytime he enters

activate venv:
```
. venv/bin/activate
```

install required pip packages:
```
pip install --no-cache-dir -r ./requirements.txt
```

b) suggested option - with pyenv:

install required pip packages (activation is not required at this point, as long as you entered the home-page directory)
```
pip install --no-cache-dir -r ./requirements.txt
```

## UPGRADE

1. pull new version of home-page
```
git pull
```

2. update python venv (if changed)
Here you can find suggestions for version change with pyenv: https://www.linuxtut.com/en/c8b82ab42564256df884/

3. update packages in your venv
```
pip install --no-cache-dir -r ./requirements.txt
```

4. restart server - see START section

## START

The server is implemented to run in two modes:

1. development mode
It will use dummy flask server, it is not recommended for production.
```
./start dev
```

2. production mode
It will use WSGI server (gunicorn), this is recommended option for production.
```
./start prod
```

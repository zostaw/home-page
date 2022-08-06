# home-page
This is my home page.

It does not keep track of venv, so requirements.txt should be updated accordingly.

## INSTALLATION
You must have installed at least python 3.6

1. go to parent directory for your project. In example, home directory is used (new directory "home-page" will be created inside).
```
cd ~/
```

2. initiate local repo and load this project
```
git clone git@github.com:zostaw/home-page.git
```
3. install venv
```
python3 -m venv venv
```
4. activate venv
```
. venv/bin/activate
```
5. install required pip packages
```
pip install --no-cache-dir -r ./requirements.txt
```

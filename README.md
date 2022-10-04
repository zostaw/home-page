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

### `npm Global install:`
npm install npm -g

#### `Python virtual environment setup:`
##### `Windows 10:`
###### `check if pip is already installed`
py -m pip --version
###### `if pip is already installed upgrade pip, if not install`
py -m pip install --upgrade pip
###### `install virtual environment using pip`
py -m pip install virtualenv

###### `create virtual environment`
py -m venv [virtual env name]
Or \
mkvirtualenv [virtual env name]

###### `to activate virtual env:`
.\env\Scripts\activate

###### `to deactivate virtual env`
deactivate

###### `to reactivate virtual env`
workon [virtual env name]

##### Ubuntu:
###### `check if pip is already installed`
python3 -m pip --version
###### `if pip is already installed upgrade pip, if not install`
python3 -m pip install --upgrade pip
###### `install virtual environment using pip`
python3 -m pip install virtualenv

###### `create virtual environment`
python3 -m venv [virtual env name] \
Or \
mkvirtualenv [virtual env name]\

###### `to activate virtual env:`
source env/bin/activate

###### `to deactivate virtual env`
deactivate

###### `to reactivate virtual env`
workon [virtual env name]


#### `Installing required libraries in virtualenv`
pip install python-dotenv\
pip install virtualenvwrapper\
pip install flask\
pip install numpy\
pip install datetime\
pip install pickle-mixin\
pip install sklearn\
pip install pandas\
pip install tensorflow\
pip install xgboost\
pip install -q git+https://github.com/tensorflow/docs\
pip install matplotlib\

#### `To start flask server`
##### `Windows 10`
set FLASK_APP=bike_share.py
flask init
flask run

##### `Ubuntu`
export FLASK_APP=bike_share.py
flask init
flask run

#### `To start react app`
yarn start



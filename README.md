### `npm Global install:`
npm install npm -g

#### __`Python virtual environment setup:`__
##### __`Windows 10:`__
###### __`check if pip is already installed`__
py -m pip --version
###### __`if pip is already installed upgrade pip, if not install`__
py -m pip install --upgrade pip
###### __`install virtual environment using pip`__
py -m pip install virtualenv

###### __`create virtual environment`__
py -m venv ``virtual env name``\
Or \
mkvirtualenv ``virtual env name``

###### __`to activate virtual env:`__
.\env\Scripts\activate

###### __`to deactivate virtual env`__
deactivate

###### __`to reactivate virtual env`__
workon ``virtual env name``

##### Ubuntu:
###### __`check if pip is already installed`__
python3 -m pip --version
###### `if pip is already installed upgrade pip, if not install`
python3 -m pip install --upgrade pip
###### `install virtual environment using pip`
python3 -m pip install virtualenv

###### `create virtual environment`
python3 -m venv ``virtual env name``\
Or \
mkvirtualenv ``virtual env name``

###### `to activate virtual env:`
source env/bin/activate

###### `to deactivate virtual env`
deactivate

###### `to reactivate virtual env`
workon ``virtual env name``


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



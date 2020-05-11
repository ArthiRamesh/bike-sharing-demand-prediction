## npm Global install:
npm install npm -g

Python virtual environment setup:
Windows 10:
## check if pip is already installed
py -m pip --version
## if pip is already installed upgrade pip, if not install
py -m pip install --upgrade pip
## install virtual environment using pip
py -m pip install virtualenv

## create virtual environment
py -m venv <virtual env name>
Or 
mkvirtualenv <virtual env name>

## to activate virtual env:
.\env\Scripts\activate

## to deactivate virtual env
deactivate

## to reactivate virtual env
workon <virtual env name>

Ubuntu:
## check if pip is already installed
python3 -m pip --version
## if pip is already installed upgrade pip, if not install
python3 -m pip install --upgrade pip
## install virtual environment using pip
python3 -m pip install virtualenv

## create virtual environment
python3 -m venv <virtual env name>
Or 
mkvirtualenv <virtual env name>

## to activate virtual env:
source env/bin/activate

## to deactivate virtual env
deactivate

## to reactivate virtual env
workon <virtual env name>


## Installing required libraries in virtualenv
pip install python-dotenv
pip install virtualenvwrapper
pip install flask
pip install numpy
pip install datetime
pip install pickle-mixin
pip install sklearn
pip install pandas
pip install tensorflow
pip install xgboost
pip install -q git+https://github.com/tensorflow/docs
pip install matplotlib

## To start flask server
Windows 10
set FLASK_APP=bike_share.py
flask init
flask run

Ubuntu
export FLASK_APP=bike_share.py
flask init
flask run

## To start react app
yarn start


### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.


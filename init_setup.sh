##These file will help to store terminal command Shell Script
# only for linux terminal (bash)
#touch README.md (create readme.md file)
#echo will used for showing message on cmd promt
#bash init_setup.sh

echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
source python -m venv env  
echo [$(date)]: "activating the environment" 
source activate env
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt
echo [$(date)]: "END" 
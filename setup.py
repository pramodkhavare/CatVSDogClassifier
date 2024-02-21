#setup.py file will help to create local package 
# few year ago pyproject.toml file was used to provide configuration to setup.py
# but nowdays mostly setup.config is used
import setuptools 

with open('README.md' ,'r' ,encoding= 'utf-8') as f:
          LONG_DESCRIPTION = f.read()
          

PROJECT_NAME = "CNN_Classifier"
VERSION = '0.0.1'
SRC_REPO = "CNNClassfier"
DESCRIPTION = "This is our deep learning classification package"
AUTHOR_NAME = "Pramod Khavare"
AUTHOR_EMIL = "pramodkhavare2000@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


setuptools.setup(
    name = SRC_REPO,
    version=VERSION ,
    description=DESCRIPTION , 
    author= AUTHOR_NAME ,
    author_email= AUTHOR_EMIL ,
    long_description= LONG_DESCRIPTION ,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{PROJECT_NAME}",

    project_urls = {
            "Bug Tracker ": f"ttps://github.com/{AUTHOR_NAME}/{PROJECT_NAME}"
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")
)


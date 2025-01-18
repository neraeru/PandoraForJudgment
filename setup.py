from setuptools import setup

APP = ['damage_calculator.py'] 
DATA_FILES = [] 
OPTIONS = {
    'argv_emulation': True,  
    'packages': ['packaging', 'altgraph', 'pyinstaller', 'pefile'], 
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
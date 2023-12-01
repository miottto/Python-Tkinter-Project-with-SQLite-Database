from setuptools import setup, find_packages

setup(
    name='Library App',
    author='Luiz Gustavo Miotto',
    description='This package contains a Tkinter GUI + SQLite3 software code for a book library.',
    author_email='lg.miotto@gmail.com',
    url='',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['tkinter', 'hashlib', 'sqlite3', 'os'  
       
    ],
    classifiers=[
        "Programming Language :: Python :: 3", 
        "Operating System :: Microsoft :: Windows",    
    ]
    
)

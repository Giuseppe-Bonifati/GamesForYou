# GamesForYou :video_game: :bar_chart: 

<a href="https://www.linkedin.com/in/giuseppe-bonifati-738640261/"><img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue"></a> 



#### Description:
   

GamesForYou is a simple project made for CS50 final project.
GamesForYou will choose a random PS5 or Xbox Series X games, based on the type of game that the user will choose, also at the end the program will show you all statistics of all the users choices (type of games).
GamesForYou take the information of the games form Wikipedia ( Web scraping )

#### Video Demo:  <a href="https://youtu.be/EucxYjQYdQg"> <img src="https://img.shields.io/badge/-Play-f00?logo=youtube"></a> 


## Installation

<a href=https://www.python.org/ ><img src="https://img.shields.io/badge/-Python-white?logo=python"></a> <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/-Pandas-130654?logo=pandas"></a>  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/-Matplotlib-blue"></a>
<a href="https://www.wikipedia.org/"><img src="https://img.shields.io/badge/-Wikipedia-grey?logo=wikipedia"></a>    <a href="https://www.xbox.com/en-US/"><img src="https://img.shields.io/badge/-Xbox-107c10?logo=xbox"></a> <a href="https://www.playstation.com/en-us/"><img src="https://img.shields.io/badge/-Playstation%205-black?logo=Playstation5"></a>

<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/-Visual%20Studio%20Code-0098ff?logo=visualstudiocode" ></a>

In the file <a href="https://github.com/Giuseppe-Bonifati/GamesForYou/blob/main/requirements.txt"><img src="https://img.shields.io/badge/-requirements.txt-white?"></a> there are all the packages to be installed 

Then we import on project.py all the following:

```python
import random
import sys
from csv import DictWriter

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore # library for data analysis
import requests  # type: ignore # library to handle requests
from bs4 import BeautifulSoup  # type: ignore # library to parse HTML documents
```
### List of the games

https://en.wikipedia.org/wiki/List_of_PlayStation_5_games

https://en.wikipedia.org/wiki/List_of_Xbox_Series_X_and_Series_S_games

## Directory

In the directory project there are the following directories:

▪️ project.py

▪️ test_project.py

▪️ user.csv

▪️ requirements.txt

▪️ README.md

▪️ .gitignore

▪️ LICENSE.md



## Design

All the project (code) is on the file project.py.

The program take the users informations and each time check if the informations are valid , then with the help of request and Beautiful Soup and pandas the program extract content and data from Wikipedia and return a random game.

Once we display the result , the program will save all the informations in a file csv, in this case in the file user.csv.

At the pandas with help to calculated all the statistics and it will be displayed to the users with Matplotlib    



## Visuals

<p align="center">
<img width="539" alt="image" src="https://user-images.githubusercontent.com/110894389/220594613-7b663c51-04a2-4b2d-977a-6128e9418569.png">
</p>

<p align="center">
<img width="953" alt="image" src="https://user-images.githubusercontent.com/110894389/220594960-b7e72bf6-52e7-4707-9650-4a3ad258809b.png">
</p>


## License

<a href="https://github.com/Giuseppe-Bonifati/GamesForYou/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue"></a>

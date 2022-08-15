# Biological Records of Puma concolor


## Description
A simple Flask application that accesses data of cougar specimens and observations from the [iDigBio API](https://www.idigbio.org/portal/search), uses SQLAlchemy to store data in a SQLite database, queries database and returns information on five specimens


![](https://live.staticflickr.com/65535/47752782922_93b7d3141a_b.jpg)

## Introduction
Puma, cougar, and mountain lion are all names for the same animal: *Puma concolor*. Historically, their habitat ranged from the Yukon in Canada to the southern Andes in South America. The most dramatic reduction of habitat has occurred in eastern North America, where the once-prevalent Eastern Puma (*Puma concolor couguar*) has recently been declared [extinct](https://www.biologicaldiversity.org/news/press_releases/2018/eastern-puma-01-22-2018.php#:~:text=WASHINGTON%E2%80%94%20The%20U.S.%20Fish%20and,and%20from%20Manitoba%20to%20Illinois.).


![](https://csvcoll.org/imglib/verte/UWSP_Mammals/M-010/M_10389skull_Puma_concolor_1615930283_lg.jpg)

## Installation
- Navigate to the parent directory `Puma`
- Depending on what packages you already have installed on your machine, you may be able to skip some of the following steps:
    - install pip 
    - pip install Python 3
    - pipenv install
- Navigate to inner directory `Puma_app`
    - flask run FLASK_APP = app.py

## Next Steps
- Deploy application using cloud platform such as Heroku
- Adjust query to pull information on more specimens
- Create data visualizations, including a map
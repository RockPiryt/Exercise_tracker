# Exercises Tracker
Create exercises tracker using Pixela. User can add exercise's minutes at particular day and see progress at visual graph

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Previews](#Previews)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
* [License](#license)

## General Information

I created this app to analyze system of exercises everyday. Pixela graph is easy way to understand my overall progress. I use API requests to GET, POST, PUT and DELETE  information about exercises. Moreover I use strftime() to format date to correct format, which is required on Pixela page. 


## Technologies Used
- Python - version 3.11 
- Requests - library to made API request
- Dotenv - to hide passwords and token



## Features
List the ready features here:
- User can answer question about 'how many exercises do at particular day?'
- This answer is posted via POST request to Pixela graph
- User can analyze graph to see progress in exercises


## Previews
### Pixela Graph
![Pixela Graph Preview](https://github.com/RockPiryt/Exercise_tracker/blob/main/exercises_tracker_pixela_preview.jpeg?raw=true)


## Setup
- Clone This Project git clone
- Enter Project Directory cd Exercise_tracker
- Create a Virtual Environment (for Windows) py -m venv (name your virtual enviroment :) venv

'EXAMPLE: py -m venv venv'

- Activate Virtual Environment source: venv/Scripts/activate
- Install Requirements Package pip install -r requirements.txt
- Finally Run The Project: python app.py


## Project Status
Project is: _in progress_ 

## Room for Improvement

Room for improvement:
- Ask user about particular date


## Contac
- Created by [@RockPiryt Github](https://github.com/RockPiryt)

- My Resume [@RockPiryt Resume](https://rockpiryt.github.io/Resume/)

Feel free to contact me!

## License
This project is open source and available under the [MIT License]
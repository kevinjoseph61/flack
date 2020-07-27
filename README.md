# Flack!

## A Flask driven application that uses sockets to implement a real time clone of slack 

- Flask+Slack=Flack!
- This project was done in accordance with the specifications laid out in https://docs.cs50.net/web/2020/x/projects/2/project2.html for project 2 of CS50w (2018 version)
- Application demo can be found at https://drive.google.com/file/d/1QcxpSVXf9I9cfgtYGzqeeDaHZFTeQC3W/view?usp=sharing
- application.py contains the main code that requires flask to run. Be sure to set the environment variable of FLASK_APP to application.py
- Use pip to install the required libraries in requirements.txt using "pip install -r requirements.txt"
- Run flask using "flask run"
- index.js in the static folder contains all the necessary interactions with the server using sockets.io
- style.css in staic contains all the styling that has been used for the index.html file
- index.html in the templates folder contains the main format for the single page interface that is used for rendering the flack application
- Application allows adding and changing of username
- Application allows to create and join channel as required
- Application allows side by side chatting on different browsers
- Application allows to send files less than 10mb as optional feature
- Application remembers name and channel by using local storage of the browser even after closing of window
- index.js and application.py interact with each other to update messages in server side and client side as necessary

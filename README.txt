Movie Application -- version 1.0

This program generates a web page that displays a person's favorite movies. 
The web page displays the movies title, poster and plot summary, as well as 
a trailer of the movies. 

-- Dependencies -- 

   webbrowser, re, os, jinja2

-- Program Structure -- 

movie_app/
|-- movies.py
|-- entertainment_center.py
|-- page_generator.py
|-- README.txt
|-- templates/
    |-- index.html
    |-- main.css
    |-- main.js

The movie objects are built using the Movie class, which is located in 
the movies.py. The movies.py file instantiates movie objects with a 
title (string), poster (img url as string), storyline (string) and movie 
trailer (youtube url string). 

Movie objects are generated in the entertainment_center.py file, which
imports the Movie class from movies.py. Movie objects are stored in a 
list. To create movie objects, simply add the movie object to the 
entertainment_center.py file and then append it to the list variable 
my_movies. The entertainment_center.py file also imports the functionality
from the page_generator.py file and calls the open_movies_page() function,
which takes the list of movies as an argument. When this function is called
the movie objects are handled in page_generator.py. 

The page_generator.py file uses jinja2 to handle the template files. The 
function open_movies_page() gets a template object using jinja which is then
formatted using the movie objects passed to the function. After the template 
is formatted, webbrowser is used to update the file. Finally, the updated
page is opened in your favorite browser.  

- Bootstrap and Googlefonts are used for the css and js - 
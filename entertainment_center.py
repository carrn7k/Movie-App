import movies
import page_generator

rocky = movies.Movie(
    'Rocky',
    'https://www.youtube.com/watch?v=3VUblDwa648',
    'The story of boxer making his way to the top',
    'https://www.movieposter.com/posters/archive/main/90/MPW-45270')

be_blood = movies.Movie(
    'There Will Be Blood',
    'https://www.youtube.com/watch?v=FeSLPELpMeM',
    'A story exploring a man\'s quest for power',
    'http://cdn.collider.com/wp-content/uploads/there_will_be_blood_movie_poster_rolling_roadshow_2010_olly_moss.jpg')

old_men = movies.Movie(
    'No Country for Old Men',
    'https://www.youtube.com/watch?v=38A__WT3-o0',
    'A story about a man caught up in crime and violence',
    'https://aswedetalksmovies.files.wordpress.com/2012/04/no-country-for-old-men.jpg')

the_future = movies.Movie(
    'Back to the Future',
    'https://www.youtube.com/watch?v=yosuvf7Unmg',
    'A boy travels in time using a delorean',
    'http://www.movieposter.com/posters/archive/main/50/MPW-25074')

space_jam = movies.Movie(
    'Space Jam',
    'https://www.youtube.com/watch?v=IzU0x1tlfSQ',
    'Michael Jordan plays basketball with the Loony Toons and some Aliens',
    'https://www.movieposter.com/posters/archive/main/93/MPW-46645')

my_movies = [
    rocky, be_blood,
    old_men, the_future,
    space_jam
]

page_generator.open_movies_page(my_movies)

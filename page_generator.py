import jinja2
import os
import webbrowser
import re

# Create a template environment using jinja2
PATH = os.path.dirname(os.path.abspath(__file__))
loader = jinja2.FileSystemLoader(os.path.join(PATH, 'templates'))
ENVIRONMENT = jinja2.Environment(loader=loader)


movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" 
data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h3 id="titles">{movie_title}</h3>
    <img src="{poster_image_url}" width="220" height="342">
<h4><a href="#" id="plot" data-toggle="popover" title="{movie_title}"
data-content="{storyline}" data-placement="top">plot</a></h4>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline = movie.storyline
        )
    return content

def open_movies_page(movies):
    # Fetch the template using jinja and then format it
    update = ENVIRONMENT.get_template('index.html').render()
    update = update.format(movie_tiles = create_movie_tiles_content(movies))
    # Open the formatted template in a browser
    with open('templates/index.html', 'w') as edit:
        edit.write(update)
        webbrowser.open(PATH + '\\templates\\index.html')



# Movie Database App

This is a simple movie database application built using Python, WebApp2 framework, Jinja2 templates, Google App Engine, and Google Cloud ndb Datastore. The application allows users to store and manage movie information, including titles, directors, cast members, genres, and posters.

## Features

- View a list of movies stored in the database.
- Add new movies to the database.
- Search movies by directors, cast members, and genres.
- Edit existing movie information in the database.

## Installation and Deployment

1. Clone the repository through [https link](https://github.com/implicitdefcncdragneel/webapp2-omdb-openAPI.git).
2. Install the required dependencies specified in the `requirements.txt` file.
3. Set up the Google Cloud Platform project and enable the App Engine service.
4. Modify the necessary configurations in the `app.yaml` file.
5. Deploy the application to the Google App Engine using the provided deployment instructions.

## Usage

1. The home page displays a list of movies with their thumbnails and links to their IMDB pages.
2. Use the navigation menu to access different features:
   - **List Movies:** View all movies stored in the database.
   - **Add Movie:** Add a new movie by providing its details.
   - **Search Movies:** Search movies by directors, cast members, or genres.
   - **Edit Movie:** Edit existing movie information.
3. To add movies easily, you can fetch data from an open-source movie database such as [OMDb API](https://www.omdbapi.com/).
4. Enjoy managing and exploring your movie collection!

## Code Structure

The codebase is structured as follows:

- `app.yaml`: Configuration file for Google App Engine.
- `main.py`: Main script request handlers for different views, actions and routing logic.
- `models.py`: Defines the ndb models for movie entities.
- `templates/`: Directory containing Jinja2 HTML templates.

## Contact

For any questions or inquiries, please contact [chandranandan.chandrakar@gmail.com](mailto:chandranandan.chandrakar@gmail.com).

**Note:** 
1. To deploy the application, please refer to the instructions provided in the link  (https://cloud.google.com/eclipse/docs/creating-new-webapp).
Note :
2. https://stackoverflow.com/questions/15639475/webapp2-with-python3 .
3. Use Your Own API Key For OMDB that will be inserted in "AddMovieHandler" .

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api_key = os.environ["movie_api"]

# create new table
class Movie(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(250), unique=True, nullable=False)
   year = db.Column(db.Integer, nullable=False)
   description = db.Column(db.String(500), nullable=False)
   rating = db.Column(db.Float, nullable=True)
   ranking = db.Column(db.Integer, nullable=True)
   review = db.Column(db.String(250), nullable=True)
   img_url = db.Column(db.String(250), nullable=False)
db.create_all()

# # add new entry
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

class RateMovieForm(FlaskForm):
   new_rating = FloatField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
   new_review = StringField(label='Your Review', validators=[DataRequired()])
   submit = SubmitField(label="Done")

class AddMovieForm(FlaskForm):
   new_movie = StringField(label='Movie Title', validators=[DataRequired()])
   submit = SubmitField(label="Add Movie")

@app.route("/")
def home():
   ordered_movie = Movie.query.order_by(Movie.rating)
   ranking = ordered_movie.count()
   # ranking = 1
   for item in ordered_movie:
      item.ranking = ranking
      db.session.commit()
      ranking -= 1
   return render_template("index.html", movies=ordered_movie)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
   rating_form = RateMovieForm()
   movie_id = request.args.get('id')
   movie = Movie.query.get(movie_id)
   if rating_form.validate_on_submit():
      movie.rating = float(rating_form.new_rating.data)
      movie.review = rating_form.new_review.data
      db.session.commit()
      return redirect(url_for('home'))
   return render_template("edit.html", form=rating_form, movie=movie)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
   add_form = AddMovieForm()
   if add_form.validate_on_submit():
      movie_endpoint = "https://api.themoviedb.org/3/search/movie"
      search_movie = add_form.new_movie.data
      movie_parameters = {
         "api_key": api_key,
         "query": search_movie,
      }

      movie_response = requests.get(url=movie_endpoint, params=movie_parameters)
      movie_data = movie_response.json()["results"]
      return render_template("select.html", all_movies=movie_data)
   return render_template("add.html", form=add_form)

@app.route('/movie', methods=['GET', 'POST'])
def movie():
   mov_id = request.args.get('id')
   if mov_id:
      info_endpoint = f"https://api.themoviedb.org/3/movie/{mov_id}"
      info_parameters = {
         "api_key": api_key,
      }

      info_response = requests.get(url=info_endpoint, params=info_parameters)
      data = info_response.json()
      new_movie = Movie(
         title=data["title"],
         year=data["release_date"].split("-")[0],
         description=data["overview"],
         img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
      )
      db.session.add(new_movie)
      db.session.commit()

      return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)

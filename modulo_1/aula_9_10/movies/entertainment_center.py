import fresh_tomatoes
import media


toy_story = media.Movie(
	"Toy Story", 
	"A story of a boy and hist toys that come to life", 
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=vwyZH85NQC4"
	)
# print(toy_story.storyline)

avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SL1000_.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"
	)
# print(avatar.storyline)

avengers = media.Movie(
	"Avender Infinity War",
	"The history of a crazy Titan that plans to exterminate half the population of the Universe.",
	"https://http2.mlstatic.com/poster-cartaz-filme-a3-marvel-vingadores-guerra-infinita-09-D_NQ_NP_684076-MLB27154811623_042018-F.jpg",
	"https://www.youtube.com/watch?v=6ZfuNTqbHE8"
	)

# avengers.show_trailer()

# movies = [toy_story, avatar, avengers]
# fresh_tomatoes.open_movies_page(movies)


# print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print("Clas: " + media.Movie.__name__)
print("Module: " + media.Movie.__module__)
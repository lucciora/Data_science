from matplotlib import pyplot

# bar 만들기

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

pyplot.bar(xs, num_oscars)
pyplot.title("My Favorite Movies")
# label x-axis with movie names at bar centers
pyplot.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
pyplot.show()


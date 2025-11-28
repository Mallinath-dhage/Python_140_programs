# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
for i in range(3):
    movie = input(f"Enter the name of favorite movie {i+1}: ")
    movies.append(movie)
print("Your favorite movies are:", movies)

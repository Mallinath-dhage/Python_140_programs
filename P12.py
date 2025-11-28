# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
for i in range(3):
    movie = input(f"Enter the name of favorite movie {i+1}: ")
    movies.append(movie)
print("Your favorite movies are:", movies)

# Here in this program, we are using a for loop to prompt the user to enter the names of their 3 favorite movies.
# Each movie name is appended to the 'movies' list. Finally, we print the list of favorite movies entered by the user.
# This program demonstrates the use of lists and loops in Python.
# In the line 4 we are using f-string to format the input prompt dynamically based on the iteration count.
# This makes the prompt more user-friendly by indicating which movie number the user is entering.
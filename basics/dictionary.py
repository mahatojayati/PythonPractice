Novels = {1: "The Great Gatsby",
          2: "To Kill a Mockingbird",
          3: "1984",
          4: "Pride and Prejudice",
          5: "The Catcher in the Rye",}
Movies = {1: "The Shawshank Redemption",
            2: "The Godfather",
            3: "The Dark Knight",
            4: "Pulp Fiction",
            5: "Forrest Gump",}

for i in Novels:
    print(i, ":", Novels[i])
for i in Movies:
    print(i, ":", Movies[i])
# Adding a new novel
Novels[6] = "Brave New World"
# Adding a new movie
Movies[6] = "Inception"
# Printing the updated dictionaries
print("\nUpdated Novels:")
for i in Novels:
    print(i, ":", Novels[i])
print("\nUpdated Movies:")
for i in Movies:
    print(i, ":", Movies[i])
# Removing a novel
del Novels[2]
# Removing a movie
del Movies[3]
# Printing the dictionaries after deletion
print("\nNovels after deletion:")
for i in Novels:
    print(i, ":", Novels[i])
print("\nMovies after deletion:")
for i in Movies:
    print(i, ":", Movies[i])
# Checking if a novel exists
novel_to_check = "1984"
if novel_to_check in Novels.values():
    print(f"\n'{novel_to_check}' exists in the Novels dictionary.")
else:
    print(f"\n'{novel_to_check}' does not exist in the Novels dictionary.")
# Checking if a movie exists
movie_to_check = "The Matrix"
if movie_to_check in Movies.values():
    print(f"'{movie_to_check}' exists in the Movies dictionary.")
else:
    print(f"'{movie_to_check}' does not exist in the Movies dictionary.")
    
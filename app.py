"""
- Enter 'a' to add a movie, 'l' to see your movie, 'f' fo find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running the program

Tasks:
[]: decide where to store movies
[]: What is the format of a movie?
[]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'


"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' fo find a movie, and 'q' to quit: ")
    print()

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Sorry, you entered an invalid command. Please try again.")

        print()
        user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' fo find a movie, and 'q' to quit: ")


def show_movies():
    for movie in movie_list:
        title = movie['title']
        director = movie['director']

        print(f"{title} : by {director}")



movie_list = [

    {
        'title': 'The Matrix',
        'director': 'Sam',
        'year': '1995',
        'category': 'Action'
    },
    {
        'title': 'Pulp Fiction',
        'director': 'Quintin Tarantino',
        'year': '1995',
        'category': 'Action'
    },
    {
        'title': "The world's fastest indian",
        'director': '??',
        'year': '2007',
        'category': 'Action'
    }

    ]
menu()

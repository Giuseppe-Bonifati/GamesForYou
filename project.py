import random
import sys
from csv import DictWriter
import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore # library for data analysis
import requests  # type: ignore # library to handle requests
from bs4 import BeautifulSoup  # type: ignore # library to parse HTML documents


def main():
    file_csv = "user.csv"
    # assign to the user the function users() that return a dictionary with all the information about the user
    user = users() 
    print(
        f"\n*******************{user['name']} Welcome to GamesForYou ********************************"
    )
    print(
        "********We will help you to find the best games for your console**********\n"
    )
    # assign to the var console the value that return the fuction consols().
    consol = consols()
    # return the genres game on the var genre
    genre = genres().capitalize()
    if consol == "serie x":
        # web return in the var info a random game
        info = web("List_of_Xbox_Series_X_and_Series_S_games", genre)
    elif consol == "ps5":
        # web return in the var info a random game
        info = web("List_of_PlayStation_5_games", genre)

    print("\nGamesForYou choose:\n")
    print(f"****************{info['Title']}****************")
    write_file(file_csv, info, user, consol)
    confirmation = input("\nIf you want to see all statistics enter y and press enter , all other different input will close the program: ")
    if confirmation in ["yes","y","Y","YES","Yes"]:
        print("\n\n**********************************Bye!! Hope to see you soon :)**************************************")
        #stat() return a dictionary with all avarage statistics
        average_dict = stat()
        #print on the console all the statistics and also (the function statistics_and_graf call another function graf() to show the graphs)
        statistics_and_graf(average_dict)
    else:
        sys.exit("\n\n**********************************Bye!! Hope to see you soon :)**************************************")    



def statistics_and_graf(average_dict):
    '''this function print all statistics and call the function graf() to show the graphs'''
    print("\nFavorite consol: PS5 {:.2f}%  SERIE X {:.2f}%".format(average_dict['play_stations'],average_dict['serie_x']))
    print("Average ages of our users: {:.2f}".format(average_dict['age']))
    print("\n\nUsers favorite types of game , divided by genres:\n")
    print("Sports: {:.2f}%".format(average_dict['sports']))
    print("Racing: {:.2f}%".format(average_dict['racing']))
    print("Survival: {:.2f}%".format(average_dict['survival']))
    print("Shooters: {:.2f}%".format(average_dict['shooters']))
    print("Action-adventure: {:.2f}%".format(average_dict['action']))
    print("Adventure: {:.2f}%".format(average_dict['adventure']))
    print("Stealth: {:.2f}%".format(average_dict['stealth']))
    print("Horror: {:.2f}%".format(average_dict['horror']))
    graf(average_dict)


def graf(average_dict):
    '''function made to show the graphs'''
    fig, ax = plt.subplots()
    fig.set_size_inches(16.5, 8.5)

    x = [
        "Survival",
        "Racing",
        "Sports",
        "Fighting",
        "Shooters",
        "Action-adventure",
        "Adventure",
        "Stealth",
        "Horror",
    ]

    y = [average_dict["survival"],average_dict["racing"],average_dict["sports"],average_dict["fight"],average_dict["shooters"],average_dict["action"],average_dict["adventure"],average_dict["stealth"],average_dict["horror"]]

    bar_colors = [
        "tab:red",
        "tab:orange",
        "tab:olive",
        "tab:gray",
        "tab:brown",
        "tab:green",
        "tab:cyan",
        "tab:pink",
        "tab:blue",
    ]

    ax.bar(x, y, color=bar_colors)

    ax.set_ylabel("Percentage usage")
    ax.set_title("USER CHOICE PS5:{:.2f}% SERIE X:{:.2f}% AVERAGE AGE {:.2f}".format(average_dict['play_stations'],average_dict['serie_x'],average_dict["age"]))
    
    

    plt.show()


def write_file(file_csv, info, user, consol):
    '''the fuction get 4 arguments the file to be written, the dictionary info with all the values from wikipedia,
       the user name and the consol
       this function will update and write info in file csv'''
    field = [
        "UserName",
        "UserFamilyName",
        "Age",
        "Consol",
        "Title",
        "Genre(s)",
        "Developer(s)",
        "Publisher(s)",
    ]
    info["Consol"] = consol
    info["UserName"] = user["name"]
    info["UserFamilyName"] = user["surname"]
    info["Age"] = user["age"]

    with open(file_csv, "a") as f:
        dictwriter_object = DictWriter(f, fieldnames=field)
        dictwriter_object.writerow(info)
        f.close()


def web(link, genre):
    """get the information from an url and return a random game with the
    genres, the developers and the publisher (info form wikipedia)"""
    # get the response in the form of html
    wiki_url = "https://en.wikipedia.org/wiki/" + link
    response = requests.get(wiki_url)
    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, "html.parser")
    list_of_games = soup.find("table", {"id": "softwarelist"})
    # pandas read_html
    df = pd.read_html(str(list_of_games))

    # convert list to data frame
    df = pd.DataFrame(df[0])

    # drop level columns
    df.columns = df.columns.droplevel(-1)

    # find all games with the types
    types = df.loc[df["Genre(s)"] == genre]["Title"]
    # get a random games form the list
    game = random.choice(list(types))

    # using the game (title) find all the rest of the data frame (row)
    base = df.loc[df["Title"] == game]

    # get the genre developers the publisher of the random games
    genres = base["Genre(s)"].values[0]
    dev = base["Developer(s)"].values[0]
    pub = base["Publisher(s)"].values[0]

    # return a dictionary containing the game names genres developers and the publisher
    return {"Title": game, "Genre(s)": genres, "Developer(s)": dev, "Publisher(s)": pub}


def users():
    """Return a dictionary containing  users dates name , surname and age that will be an int"""

    print("\n***Let us know more about you***")

    while True:
        try:
            name = input("Name: ").strip().capitalize()
            if not name.isalpha():
                raise ValueError
            surname = input("Surname: ").strip().capitalize()
            if not surname.isalpha():
                raise ValueError
            age = int(input("Age: "))
            if not age or not name or not surname:
                raise ValueError
            elif age < 18:
                sys.exit(
                    f"\nSorry {name} website not allowed for user under 18 years old\n"
                )
            break
        except ValueError:
            print(f"\n{name} Please enter your data again somethings went wrong\n")

    return {"name": name, "surname": surname, "age": age}


def consols():
    """check if the user answers the question correctly and check if the answers is on the list"""
    consol = input("Type the name of your console:\nPS5 , Serie X: ").strip().lower()
    while consol not in ["ps5", "serie x"]:
        consol = input("\nType as in the description PS5 , Serie X: ").strip().lower()
    return consol


def genres():
    """check if the user answers the question correctly and check if the answers is on the list"""
    game = (
        input(
            "\nWhat is your favorite type of games :\nSurvival , Racing , Sports , Fighting , Shooters , Action-Adventure , Adventure , Stealth , Horror: "
        )
        .strip()
        .lower()
    )
    while game not in [
        "survival",
        "racing",
        "sports",
        "fighting",
        "shooters",
        "action-adventure",
        "adventure",
        "stealth",
        "horror"
    ]:
        game = input(
            "\nType as in the description Survival , Racing , Sports , Fighting , Shooters , Action-Adventure , Adventure , Stealth , Horror: "
        ).strip().lower()

    return game


def stat():
    """Read the csv file and calculate average of the game and the consol
    the function return a dictionary and the value will be the average percentage"""

    
    df = pd.read_csv("user.csv")

    number_of_users = df.count().values[0]

    age=df["Age"].mean()
    

    play_stations = df[df["Consol"] == "ps5"].count().values[0] * (100/ number_of_users)
    serie_x = df[df["Consol"] == "serie x"].count().values[0] * (100/ number_of_users)

    surv = (df[df["Genre(s)"] == "Survival"].count().values[0]) * (100 / number_of_users)
    racing = (df[df["Genre(s)"] == "Racing"].count().values[0]) * (100 / number_of_users)
    sports = (df[df["Genre(s)"] == "Sports"].count().values[0]) * (100 / number_of_users)
    fight = (df[df["Genre(s)"] == "Fighting"].count().values[0]) * (100 / number_of_users)
    shooters = (df[df["Genre(s)"] == "Shooters"].count().values[0]) * (100 / number_of_users)
    action = (df[df["Genre(s)"] == "Action-Adventure"].count().values[0]) * (100/ number_of_users)
    adventure = (df[df["Genre(s)"] == "Adventure"].count().values[0]) * (100 / number_of_users)
    stealth = (df[df["Genre(s)"] == "Stealth"].count().values[0]) * (100 / number_of_users)
    horror =(df[df["Genre(s)"] == "Horror"].count().values[0]) * (100 / number_of_users)

    return {"age":age,"play_stations": play_stations,"serie_x": serie_x,"survival": surv,"racing": racing,"sports":sports,"fight": fight,"shooters":shooters,"action": action,"adventure":adventure,"stealth":stealth,"horror":horror}


if __name__ == "__main__":
    main()
    

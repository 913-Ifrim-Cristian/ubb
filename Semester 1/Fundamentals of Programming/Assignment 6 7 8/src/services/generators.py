from random import randint
from datetime import datetime


secondName = ['Gheorghidiu', 'Iancu', 'Glanetasu', 'Muller', 'Miller', 'Seagal', 'Catana',
              'Avram', 'Statham', 'Bravo', 'Usher', 'Hammond', 'Carlson', 'Dicky', 'Matthew',
              'Williamson', 'Creanga', 'Rebreanu', 'Vijelie', 'Pinkman', 'Shelby', 'Escobar',
              'Lothbrok', 'Ironside', 'Guzman', 'Arellano Felix', 'Fuentes', 'Boneless', 'Breslin',
              'Lipan', 'Sadoveanu', 'Cioata', 'Ceausescu', 'Becali', 'Iliescu', 'Dogg', 'Gray',
              'King', 'Peste', 'Mocanu', 'Camarena', 'Pena', 'Chelsea', 'Steaua', 'McDonald']

firstName = ['Aurelian', 'Liam', 'Noah', 'Oliver', 'Elijah',
             'William', 'James', 'Benjamin','Lucas', 'Henry',
             'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel',
             'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian',
             'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden',
             'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew',
             'Luke', 'Asher', 'Carter', 'Julian', 'Grayson',
             'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony',
             'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles',
             'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah',
             'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb',
             'Ryan', 'Adrian', 'Miles', 'Eli', 'Nolan', 'Christian',
             'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca',
             'Landon', 'Hunter', 'Jonathan', 'Santiago', 'Axel',
             'Easton', 'Cooper', 'Jeremiah', 'Angel', 'Roman']

titles = ["Valentine In My Town", "Boy In The Mountain", "Visitors Without Time", "Valentines Of The Stars",
     "Foreigners And Assistants", "Men And Suitors", "Kiss Of My Fascination", "Determination Of Bliss",
     "Songs Of The Wife", "Calling My Nightmares", "Secret Admirer Of The West", "Foreigner Of Hope", "Men Of Bliss",
     "Men Of Romance", "Roommates And Honeys", "Guests And Neighbors", "Rise Of Rainbows", "Origin Of The Ocean",
     "Chasing My Sweetheart", "Sounds Of The Shadows", "Friend Without Shame", "Dearest Of The Mountains",
     "Girls With Black Hair", "Secret Admirers Of Paradise", "Wifes And Angels", "Beloved And Foreigners",
     "Scent Of My Dreams", "Disruption In The River", "Admiring Lust", "Songs Of My Girl", "Boy In The Hallway",
     "Raven Project", "Knight Makeover", "Thief Prophecy", "Soldier And Girl", "Fool And Woman",
     "Parody Of The Country", "Trouble Has Been Naughty", "Trust That Idiot", "Love Of The Device",
     "Descendant Of Last Rites", "Thief Of Gold", "Horses Of The Forsaken", "Guardians Of The Nation",
     "Bringers And Collectors", "Scientists And Boys", "Border Of Glory", "Vengeance Of The Stars",
     "Avoiding The Mountains", "Altering The Shadows"]


def titleGenerator():
    """
    This function returns titles of books randomly
    :return:
    """
    randInt = randint(0, len(titles)-1)

    title = titles[randInt]
    titles.pop(randInt)

    return title

def authorGenerator():
    """
    This function return a name author generated randomly
    :return:
    """

    idxFirst = randint(0, len(firstName)-1)
    idxSecond = randint(0, len(secondName)-1)

    return firstName[idxFirst] + ' ' + secondName[idxSecond]

def dateGenerator():

    timestamp = randint(1574020518, 1621277718)
    multiplier = randint(1, 30) * 86400

    return datetime.fromtimestamp(timestamp), datetime.fromtimestamp(timestamp+multiplier)
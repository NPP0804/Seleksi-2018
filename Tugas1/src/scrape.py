import requests
import json
from bs4 import BeautifulSoup
import time

nowshowinglink =  'https://id.bookmyshow.com/bandung/film/nowshowing'
bookmyshowlink =  'https://id.bookmyshow.com'

#Mengenerate link-link tiket film yang tersedia
def getMovieLink():
    mainhtml = requests.get(nowshowinglink)

    soup = BeautifulSoup(mainhtml.text, 'html.parser')

    nowshowing = soup.findAll('div', {'class' : ['book-button', 'experience-holder']})

    link = []

    for nowshowingmovie in nowshowing :
        try:
            movieLink = bookmyshowlink + nowshowingmovie.find('a')['href']
            if (movieLink not in link):
                link.append(movieLink)
        except TypeError:
            pass

    return link

#Memparse string info ticket 'ticket' menjadi dictionary
def parseTicketInfo(ticket):
    info = ticket.find('a', {'class':'__showtime-link'})['data-cat-popup']
    parsedInfo = {}

    #Getting Price Info
    priceIdx = info.index("\"price\":\"") + len("\"price\":\"")
    endPriceIdx = info.index("\"", priceIdx)
    price = int(info[priceIdx:endPriceIdx].replace(",", ""))

    #Getting Venue Type
    venueIdx = info.index("\"desc\":\"") + len("\"desc\":\"")
    endVenueIdx = info.index("\"", venueIdx)
    venueType = info[venueIdx:endVenueIdx]

    return {'price':price, 'venue':venueType}

def getMovieRating(soup):
    time.sleep(1)
    movie = {}

    movieTitle = soup.find('h1', {})['content']
    movie['title'] = movieTitle

    movieLink = bookmyshowlink + soup.find('h1', {}).find('a')['href']

    movieSoup = BeautifulSoup(requests.get(movieLink).text, 'html.parser')

    movie['love'] = {}
    movie['love']['percentage'] = movieSoup.find('span', {'class':'__percentage'}).get_text().strip()
    movie['love']['votes'] = movieSoup.find('div', {'class':'__votes'}).get_text().strip()

    movie['rating'] = []
    try:
        userRating = movieSoup.find('div', {'class':'user-rating'})
        movie['rating'].append({'five star':userRating.find('div', {'class':'five histo-rate'}).find('span', {'class':'point'}).get_text().strip()})
        movie['rating'].append({'four star':userRating.find('div', {'class':'four histo-rate'}).find('span', {'class':'point'}).get_text().strip()})
        movie['rating'].append({'three star':userRating.find('div', {'class':'three histo-rate'}).find('span', {'class':'point'}).get_text().strip()})
        movie['rating'].append({'two star':userRating.find('div', {'class':'two histo-rate'}).find('span', {'class':'point'}).get_text().strip()})
        movie['rating'].append({'one star':userRating.find('div', {'class':'one histo-rate'}).find('span', {'class':'point'}).get_text().strip()})
    except AttributeError:
        movie['rating'] = "Not Yet Rated"

    return movie


#Mengenerate informasi bioskop dan tiket yang tersedia dari suatu film
def getMovieTheatre(soup):
    movietheatrelist = soup.findAll('li', {'class' : 'list', 'data-sub-region-name' : 'Bandung' })
    movieTheatre = []

    for theatre in movietheatrelist:
        theatre_available = {}
        theatre_available['theatre'] = theatre['data-name']

        theatre_available['available-tickets'] = []
        ticketList = theatre.findAll('div', {'data-online' : 'Y'})
        for ticket in ticketList:
            ticketInfo = {}
            ticketInfo['time'] = ticket.find('a', {'class':'__showtime-link'})['data-showtime-code']
            ticketInfo.update(parseTicketInfo(ticket))
            theatre_available['available-tickets'].append(ticketInfo)
        movieTheatre.append(theatre_available)

    return movieTheatre

#Mengenerate informasi judul dan tiket tersedia dari link film
def getMovieData(link):
    moviehtml = requests.get(link)

    soup = BeautifulSoup(moviehtml.text, 'html.parser')

    movie = {}
    movie.update(getMovieRating(soup))
    movie['available-theatre'] = getMovieTheatre(soup)
    return movie

# --------------MAINPROGRAM------------------#
movieLink = getMovieLink()
movies = {}
movies['ticket'] = []
for link in movieLink:
    movies['ticket'].append(getMovieData(link))


with open('../data/data.json', 'w') as file:
    file.write(json.dumps(movies, indent=4))

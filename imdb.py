"""Gather IMDB keywords from 2019's top grossing movies."""
import sys
import csv

import requests
from bs4 import BeautifulSoup


def main():
    # TODO: Add API to a config and make year configurable
    URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2019,2019"
    movies = get_top_grossing_movie_links(URL)
    with open('data/top-movies-2019.csv', 'w') as output:
        writer = csv.writer(output)
        for movie in movies:
            writer.writerow([movie])


def get_top_grossing_movie_links(url):
    """Return a list of tuples containing top grossing movies of 2019 and link to their IMDB page."""
    # TODO: Look into proper logging solution
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies_list = []
    # <a href="/title/tt4777008/">Maleficent: Mistress of Evil</a>
    return [entry.text for entry in soup.select('.lister-item-header a')]


if __name__ == '__main__':
    sys.exit(main())
import requests
import re
from bs4 import BeautifulSoup


URL = 'https://www.kickstarter.com/projects/squonk/funkey-s-the-worlds-smallest-foldable-handheld-console'
page = requests.get(URL)
pledgeTitle = "Kickstarter Price"
amountForAlert = 160


def scrapeKickstart():
    availableRewards = getAvailableRewards()

    if availableRewards < amountForAlert:
        lowRewards = True
    else:
        lowRewards = False

    return lowRewards


def getAvailableRewards():
    results = getResults()

    splitText1 = results.split('(')
    splitText2 = splitText1[1].split(' ')
    availableRewards = int(splitText2[0])

    return availableRewards


def getResults():
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find('h3', text=re.compile(pledgeTitle)).findNext(class_='pledge__limit').getText()

    return results

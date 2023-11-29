import requests
import time
from bs4 import BeautifulSoup as BS

import tabula


def main():
    domain = "https://www.health.pa.gov/"
    url = "https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx"

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

    response = requests.get(url , headers=headers)


    if response.status_code == 200:

        print("Success fetching web page: Status Code {}".format(response.status_code))
        
        soup = BS(response.content, "lxml")

        countryCase = soup.find("a", {"title" : "County case counts by date"})["href"]
        deathCase = soup.find("a", {"title" : "Death by county of residence"})['href']

        countyCasePDFLink = domain + countryCase
        deathCasePDFLink  = domain + deathCase

        with open("countryCase.pdf", "wb") as f:
            resonse = requests.get(countyCasePDFLink)
            f.write(resonse.content)

        df = tabula.convert_into("countryCase.pdf", "countryCase.csv", output_format="csv", pages="all")

        with open("deathCase.pdf", "wb") as f:
            resonse = requests.get(deathCasePDFLink)
            f.write(resonse.content)

        df = tabula.convert_into("deathCase.pdf", "deathCase.csv", output_format="csv", pages="all")

    else:
        print("Status Code : {}".format(response.status_code))
        print("Please try again after a few minutes: Seems Your IP is hitting server")


if __name__ == "__main__":
    main()

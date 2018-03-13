import urllib
from bs4 import BeautifulSoup

class WebScrap(object):
    def getWeb(self, web):
        f = urllib.urlopen(web)
        myFile = f.read()
        f.close()
        return myFile

    def getTitle(self, myFile):
        soup = BeautifulSoup(myFile, "html.parser")
        title = soup.find("div", "dotd-title").find("h2").text
        print title
        return title

    def main(self):
        link = 'https://www.packtpub.com/packt/offers/free-learning/'
        file = self.getWeb(link)
        title = self.getTitle(file)

if __name__ == "__main__":
    wS = WebScrap()
    wS.main()


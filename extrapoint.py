import urllib
from bs4 import BeautifulSoup
import telebot


class WebScrap(object):
    def getWeb(self, web):
        f = urllib.urlopen(web)
        myFile = f.read()
        f.close()
        return myFile

    def getTitle(self, myFile):
        soup = BeautifulSoup(myFile, "html.parser")
        title = soup.find("div", "dotd-title").find("h2").text
        return title

    def getDescription(self, myFile):
        soup = BeautifulSoup(myFile, "html.parser")
        description = soup.find("div", "dotd-main-book-summary float-left").find_all("div")
        return description[2].text

    def printMessage(self, title):
        msg = "El llibre gratuit diari es: " + title
        return msg

    def main(self):
        link = 'https://www.packtpub.com/packt/offers/free-learning/'
        file = self.getWeb(link)
        title = self.getTitle(file)
        description = self.getDescription(file)
        print description
        msg = self.printMessage(title)
        id = 556991265
        token = "519788410:AAEQQBFj4RSMnh8UnYx8SHPYwD2MVgSAQaA"
        bot = telebot.TeleBot(token)
        bot.send_message(id, "Today the free book on Packt is: " + msg)

if __name__ == "__main__":
    wS = WebScrap()
    wS.main()


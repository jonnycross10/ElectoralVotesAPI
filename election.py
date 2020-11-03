import requests
from bs4 import BeautifulSoup as b
import time

def queryGuardian():
	r = requests.get("https://www.theguardian.com/us-news/ng-interactive/2020/nov/03/us-election-2020-live-results-donald-trump-joe-biden-who-won-presidential-republican-democrat")
	soup = b(r.content, "html.parser")

	bidens_votes = soup.find(class_ = "ge-bar__count ge-bar__count--p color--D").get_text()
	trumps_votes = soup.find(class_ = "ge-bar__count ge-bar__count--p color--R").get_text()
	updates = soup.find(class_ = "ge-ticker-waiting").get_text()

	apiInfo = {
		"Biden": bidens_votes.strip("\n"),
		"Trump": trumps_votes.strip("\n"),
		"ElectionUpdates": updates.strip("\n")
	}
	print(apiInfo)

#get info from the guradian website, and update every x seconds
while True:
	queryGuardian()
	time.sleep(5)
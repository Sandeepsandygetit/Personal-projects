from bs4 import BeautifulSoup
import requests
import csv
# website urls
url_icc_rankings="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
url_top_songs="https://www.jiosaavn.com/s/playlist/phulki_user/Weekly_Top_Songs/FnWfzTurhhg_"
url_top_ten_news="https://timesofindia.indiatimes.com/india/timestopten.cms"

response1=requests.get(url_icc_rankings)
icc_ranking=response1.text

response2=requests.get(url_top_songs)
top_songs=response2.text

response3=requests.get(url_top_ten_news)
top_news=response3.text

icc_ranking_soup=BeautifulSoup(icc_ranking,"html.parser")
top_songs_soup=BeautifulSoup(top_songs,"html.parser")
top_news_soup=BeautifulSoup(top_news,"html.parser")

# scraping icc rankings

teams=icc_ranking_soup.find_all(name="span", class_="u-hide-phablet")
top_teams=[team.getText() for team in teams]
print(top_teams)

songs=top_songs_soup.find_all(name="a",class_="u-color-js-gray")
top_songs_week=[song.getText() for song in songs]
print(top_songs_week)
top_songs_links=[song.get("href") for song in songs]
print(top_songs_links)

with open("icc_rank.csv", "w") as f:
    data=csv.writer(f)
    for teamss in top_teams:
      data.writerow(teamss)
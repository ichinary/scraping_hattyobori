import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
for i in range(21, 29):
    
    html = urlopen("https://tabelog.com/tokyo/A1302/A130203/R7958/rstLst/lunch/cond20-00-00/" + str(i) + "/?SrtT=trend&LstReserve=0&LstSmoking=0&svd=20200625&svt=1900&svps=2&vac_net=0&Srt=D")
    bsObj = BeautifulSoup(html, "html.parser")


    # contents_box = bsObj.findAll("div", {"class":"list-rst js-bookmark js-list-rst js-done"})
    restaurant_name_html = bsObj.findAll("a", {"class":"list-rst__rst-name-target cpy-rst-name"})
    # restaurant_name_html = contents_box.select_one("a.list-rst__rst-name-target cpy-rst-name")
    area_genre_html = bsObj.findAll("div", {"class":"list-rst__area-genre cpy-area-genre"}) #微妙にズレてる可能性あり
    print("--------page" + str(i) + "----------")
    for num in range(len(restaurant_name_html)):
        restaurant_name = restaurant_name_html[num].text
        restaurant_link = restaurant_name_html[num].get("href")
        area_genre = area_genre_html[num].text
        # lunch_price = lunch_price_html[num].text

        html2 = urlopen(restaurant_link)
        bsObj2 = BeautifulSoup(html2, "html.parser")
        star_html = bsObj2.find("span", {"class":"rdheader-rating__score-val-dtl"})
        lunch_price_html = bsObj2.find("a", {"class":"rdheader-budget__price-target"})
        # area_genre_html = bsObj.findAll("div", {"class":"list-rst__area-genre cpy-area-genre"})
        if(star_html == None):
            star = None
        else:
            star = star_html.text
        if(lunch_price_html == None):
            lunch_price = None
        else:
            lunch_price = lunch_price_html.text
        print("-------index" + str(num) + "----------")
        print(restaurant_name)
        print(restaurant_link)
        print(area_genre)
        print(star)
        print(lunch_price)
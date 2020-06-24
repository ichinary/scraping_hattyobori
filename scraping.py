import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
i = "1"
html = urlopen("https://tabelog.com/tokyo/A1302/A130203/R7958/rstLst/lunch/cond20-00-00/" + i + "/?SrtT=trend&LstReserve=0&LstSmoking=0&svd=20200625&svt=1900&svps=2&vac_net=0&Srt=D")
bsObj = BeautifulSoup(html, "html.parser")
print(i)
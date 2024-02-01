import requests
from bs4 import BeautifulSoup
def return_value(address, addition):
  url = requests.get(address + addition)
  soup = BeautifulSoup(url.content, 'html.parser')
  print(soup)

  frame = soup.find('iframe', id = "frame_ex1")
  iframesrc = address + frame['src']
  
  newurl = requests.get(iframesrc)
  newsoup = BeautifulSoup(newurl.content, 'html.parser')
  items = newsoup.select('body>div>table>tbody>tr')
  
  for item in items:
    name = item.select('td')[0].text.replace("\n","")
    name = name.replace("\t", "")
    print(name + "\t" + item.select('td')[1].text)

baseaddress = "https://finance.naver.com/"
info = "/marketindex/?tabSel=exchange#tab_section"

return_value(baseaddress, info)
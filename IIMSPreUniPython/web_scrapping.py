import requests 
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/los-angeles-ca/restaurants"

response = requests.get(url) # response is variable requests.get(url) get the response if 200 website allows if not it dosen't.
print(response.content) #.content pulls the code of the website

soup  = BeautifulSoup(response.content , "html.parser") 
# soup is variable 
# rest takes the code of the website and 2nd arguement states which type of code it is 
wrapper = soup.find_all(class_ = "n") # from that code find call that is called class_ = :"n" after that append into a list

for wrap in wrapper : # from that wrapper find all (dont know figure it out)
    print(wrap.find("a").text)


    
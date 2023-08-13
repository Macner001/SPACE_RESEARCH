import os
from PIL import Image
import requests
Api_key="xUWb7AGJHmq7xCkimmydQO5Xp7JbKLdnmJ6gLpol"
'''
def Mars_Img():
    name = "curiosity"
    date="2020-12-3"
    Api=str(Api_key)
    url=f"https://api.nasa.gov./mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api}"
    print(url)
    r=requests.get(url)
    Data=r.json()
    Photos = Data['photos']
    for index,photo in Photos:
        FileName="Database/Mars/"+"photo.jpg"
        img = Image.open(FileName)
        img.show()
'''

def Nasa_News_Date(Date):
    Url="https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)
    params={'date':str(Date)}
    r=requests.get(Url,params=params)
    Data=r.json()
    #print(Data)
    Info=Data['explanation']
    Title=Data['title']
    Image_url=Data['url']
    Image_r=requests.get(Image_url)
    FileName="Database/"+str(Date)+'.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    print(Title)
    print(Info)
    img = Image.open(FileName)
    img.show()

User = input("Enter the Date: ")


Nasa_News_Date(User)

#Mars_Img()

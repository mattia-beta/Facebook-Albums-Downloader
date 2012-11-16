from urllib import urlretrieve
import imp
import sys
import os
import requests

urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fbconsole.py')
fb = imp.load_source('fb', '.fbconsole.py')

fb.AUTH_SCOPE = ['user_photos','friends_photos']

fb.APP_ID = '234667136659071'
destinazione = "foto/"
id_user = "me"

fb.authenticate()


def SalvaFoto(photo_url, photo_name, album_name):
    dir = os.path.join(destinazione, album_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    req = requests.get(photo_url)
    with open(os.path.join(dir,photo_name) + ".jpg","w") as f:
        f.write(req.content)

def main():
    for album in fb.graph("/" + id_user + "/albums")["data"]:
        print "\n\nEntro in album", album["name"] , album["id"]

        for foto in fb.graph("/" + album["id"] + "/photos")["data"]:    
	    print foto["source"], album["id"]
            SalvaFoto(foto["source"], foto["id"], album["name"])

main()

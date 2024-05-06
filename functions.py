import urllib.request 
from inscriptis import get_text 

def Israel():
    url = "https://www.standwithus.com/situationroom"

    html = urllib.request.urlopen(url).read().decode('utf-8') 
    
    text = get_text(html) 

    data = text[900:2500]

    
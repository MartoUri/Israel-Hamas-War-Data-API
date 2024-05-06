import urllib.request 
from inscriptis import get_text 
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel('gemini-1.0-pro-latest')

def Israel():
    url = "https://www.standwithus.com/situationroom"

    html = urllib.request.urlopen(url).read().decode('utf-8') 
    
    text = get_text(html) 

    data = text[900:2500]

    response = model.generate_content("I will send you some data, with that complete the following JSON and DO NOT send nothing but the JSON. ALWAYS include the rockets fired from Iran and Lebanon in the total. Only respond with a JSON file. This is the following JSON: {'RocketsFiredTowardsTotal':int, 'RocketsFiredFromGaza':int, 'RocketsFiredFronIranAndLebanon':int, 'Casualties':int, 'Injured':int, 'Hostages':int, 'HostageBodies':int, 'Displaced':int, 'HostagesReleased':int, 'HostagesRescued':int}  The data is the following: " + data, stream=False)

    dictionary = eval(response.text)

    return dictionary

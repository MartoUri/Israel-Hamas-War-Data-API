import urllib.request 
from inscriptis import get_text 
import google.generativeai as genai
import datetime
import time



genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel('gemini-1.0-pro-latest')

def Israel():
    url = "https://www.standwithus.com/situationroom"

    html = urllib.request.urlopen(url).read().decode('utf-8') 
    
    text = get_text(html) 

    data = text[900:2500]

    response = model.generate_content("I will send you some data, with that complete the following JSON and DO NOT send nothing but the JSON. ALWAYS include the rockets fired from Iran and Lebanon in the total. ONLY use integers. Only respond with a JSON file. This is the following JSON: {'RocketsFiredTowardsTotal':int, 'RocketsFiredFromGaza':int, 'RocketsFiredFronIranAndLebanon':int, 'Casualties':int, 'Injured':int, 'Hostages':int, 'HostageBodies':int, 'Displaced':int, 'HostagesReleased':int, 'HostagesRescued':int}  The data is the following: " + data, stream=False)

    dictionary = eval(response.text)

    return dictionary

def Palestine():
    url = "https://www.aljazeera.com/news/longform/2023/10/9/israel-hamas-war-in-maps-and-charts-live-tracker"

    html = urllib.request.urlopen(url).read().decode('utf-8') 
    
    text = get_text(html) 

    data = text[2300 :4000]

    response = model.generate_content("I will send you some data, with that complete the following JSON and DO NOT send nothing but the JSON. Complete the JSON ONLY with information of Gaza. ONLY use integers. Only respond with a JSON file. This is the following JSON: {'Casualties':int, 'Injured':int, 'Missing':int}  The data is the following: " + data, stream=False)

    GazaDictionary = eval(response.text)

    response = model.generate_content("I will send you some data, with that complete the following JSON and DO NOT send nothing but the JSON. Complete the JSON ONLY with information of the West Bank. ONLY use integers. Only respond with a JSON file. This is the following JSON: {'Casualties':int, 'Injured':int }  The data is the following: " + data, stream=False)

    WestBankDictionary = eval(response.text)

    AllPalestineDictionary = GazaDictionary.copy()

    AllPalestineDictionary["Casualties"] += WestBankDictionary["Casualties"]

    AllPalestineDictionary["Injured"] += WestBankDictionary["Injured"]

    return GazaDictionary, WestBankDictionary, AllPalestineDictionary

def Both():
    import main

    TotalCasualties = main.Palestine[2]["Casualties"] + main.Israel["Casualties"]

    TotalInjuries = main.Palestine[2]["Injured"] + main.Israel["Injured"]

    TimeSinceOctuber7 = datetime.datetime.now(datetime.UTC) - datetime.datetime.fromtimestamp(1696563000, datetime.UTC)

    BothDictionary = {"TimeSinceOctober7" : {"Days" : TimeSinceOctuber7.days, "Hours" : int(TimeSinceOctuber7.seconds/60/60), "Minutes" : int(TimeSinceOctuber7.seconds/60%60), "Seconds" : int(TimeSinceOctuber7.seconds%60)}, "TotalInjuries" : TotalInjuries, "TotalCasualties" : TotalCasualties}

    return BothDictionary

def ConstantUpdate():
    import main

    while True:
        try:
            main.Palestine = Palestine()
            time.sleep(60)
            main.Israel = Israel()
            time.sleep(60)
            main.Both = Both()
            time.sleep(60)
        except:
            print("Error. Continuing")
            continue
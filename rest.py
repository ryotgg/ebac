import requests
import json
import pandas as pd

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def matchdetails(match):
    #jprint(match)
    dados = pd.read_json(match)
    dados

def itsme(match): 
    if match["account_id"] == "201336344":
        return True
    else:    
        return False 

try:
    response = requests.get("https://api.opendota.com/api/matches/7246362743")
    # jprint(response.json())

    # dados = pd.read_json(response.json())    
    # dados

    filtered_players = list(filter(itsme, response.json()["players"]))
    # jprint(response.json()["players"][6]["account_id"])
    print(filtered_players)
    # matchdetails(response.json()["players"])

except ValueError as exc:
    raise ValueError(f'Falha ao processar as faturas devido ao seguinte erro: "{exc}"')

  

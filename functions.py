import pandas as pd
import numpy as np
import json

def load_data(file_path):
    '''
    Takes in the file_path of the JSON event and returns the matchCentreData
    '''
    with open(file_path, 'r') as j:
        contents = json.loads(j.read())
    data = contents["matchCentreData"]
    return data

def players_list(data):
    players = pd.DataFrame.from_dict(data["playerIdNameDictionary"],  orient='index')
    players = players.reset_index()
    players.columns = ["players_id", "player_name"]
    return players
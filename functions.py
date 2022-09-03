import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mplsoccer import Pitch, VerticalPitch, FontManager
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

    '''
    Takes in matchCentreData and outputs a dataframe of player_id and name.
    '''
    players = pd.DataFrame.from_dict(data["playerIdNameDictionary"],  orient='index')
    players = players.reset_index()
    players.columns = ["players_id", "player_name"]
    return players

def passes_plot(df_suc, df_unsuc):

    '''
    Plots the successful and unsuccessful passes on a pitch.
    '''
    # Setup the pitch
    pitch = Pitch(pitch_type='opta', pitch_color='#22312b', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=False, tight_layout=True)
    fig.set_facecolor('#22312b')

    # Plot the completed passes
    lc1 = pitch.lines(df_suc.x, df_suc.y,
                    df_suc.endX, df_suc.endY,
                    lw=5, transparent=True, comet=True, label='completed passes',
                    color='#ad993c', ax=ax)

    # Plot the other passes
    lc2 = pitch.lines(df_unsuc.x, df_unsuc.y,
                    df_unsuc.endX, df_unsuc.endY,
                    lw=5, transparent=True, comet=True, label='other passes',
                    color='#ba4f45', ax=ax)

    # Plot the legend
    ax.legend(facecolor='#22312b', edgecolor='None', fontsize=20, loc='upper left', handlelength=4)
    plt.show()



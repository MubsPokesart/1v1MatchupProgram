import csv
import pandas as pd
from handlers import ProgramHandler

MATCHUP_KEYS = ['test', 'rby', 'gsc', 'adv', 'dpp', 'bw', 'oras', 'sm', 'ss', 'sv']
PROGRAM_GEN = 0 #int_selection(set(range(0, 9)), '"Enter the generation in which this program is to import its matchups from: ', 'Your previous response was not a valid number. Input a number: ')

MATCHUP_START = MATCHUP_KEYS[PROGRAM_GEN]
MATCHUP_FILE_PATH = f'data/{MATCHUP_START}matchups.csv'
print(f'Selected Generation: {MATCHUP_START}')
PROGRAM_HANDLER = ProgramHandler(MATCHUP_START)

MATCHUP_DATAFRAME = pd.read_csv(MATCHUP_FILE_PATH)

for index, column in enumerate(MATCHUP_DATAFRAME.columns):
    if index > 0:
        PROGRAM_HANDLER.parse_mon_matchups(column, MATCHUP_DATAFRAME[column].tolist(), index - 1)
    else:
        pass

GENMERATED_TEAMS = PROGRAM_HANDLER.prompt_team_method()

csv_form = '\n'.join([f'{",".join(item[0])}, {item[1]}' for item in GENMERATED_TEAMS])
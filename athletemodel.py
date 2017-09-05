import pickle
from lesson import AthleteList
from lesson import get_coach_data


def put_to_store(file_list):
    all_athlete = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athlete[ath.name] = ath
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athlete, athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return all_athlete


def get_to_store():
    all_athlete = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return all_athlete



import os
import csv
from random import randint
from time import sleep

module_home = os.path.abspath(os.curdir)  # gather file location


def location_confirm():  # confirm the python module can locate resource file
    if os.path.exists(module_home + '/resources'):
        resource_file = os.path.abspath(module_home + '/resources')
        return resource_file
    else:
        print('Please place the file %s' % module_home + '/resources')

        # assign the confirmed resource file location to variable


resources = location_confirm()

LIST_NAMES = ['SENTENCES', 'NOUNS', 'VERBS', 'ADJECTIVES']


def load_cvs_to_list(list_name):  # Get data from CSV files
    if os.path.exists(resources + '/' + LIST_NAMES[list_name] + '.csv'):
        csv_to_open = (resources + '/' + LIST_NAMES[list_name] + '.csv')
        # print(csv_to_open)
        with open(csv_to_open, 'r', newline='') as csv_open_r:
            csv_line = csv_open_r.readline()
            pass_back = []
            while csv_line:
                pass_back.append(csv_line.strip())
                csv_line = csv_open_r.readline()
        return pass_back

    else:
        print('File could not be found.')


# lists of words
SENTENCES = load_cvs_to_list(0)
NOUNS = load_cvs_to_list(1)
VERBS = load_cvs_to_list(2)
ADJECTIVES = load_cvs_to_list(3)

# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
    len(SENTENCES),
    len(NOUNS),
    len(VERBS),
    len(ADJECTIVES),
)


def shuffle_list(target_list):
    random_out = []
    while len(random_out) != len(target_list):
        new_item = target_list[randint(0, len(target_list) - 1)]
        if new_item not in random_out:
            random_out.append(new_item)
    return random_out


RANDOM_SENTENCES = tuple(shuffle_list(SENTENCES))
RANDOM_NOUNS = tuple(shuffle_list(NOUNS))
RANDOM_VERBS = tuple(shuffle_list(VERBS))
RANDOM_ADJECTIVES = tuple(shuffle_list(ADJECTIVES))

PLAYER_ID = input('Please give me your username, use only A-Z and or 1-0: \n')


def player_file_info():  # confirm or create user file(s).
    plyr_un = PLAYER_ID
    user_folder_path = os.path.join(module_home, plyr_un)
    user_save_file = os.path.join(user_folder_path, plyr_un + '.csv')
    # print(user_folder_path)
    # print(user_save_file)
    if os.path.exists(user_folder_path):
        print("You're now logged in.")
    else:
        os.mkdir(user_folder_path)
        print('Account created!')
    return user_folder_path, user_save_file


PLAYER_FOLDER_PATH, PLAYER_SAVE_FILE = player_file_info()


def player_data_load():  # load player data

    if os.path.exists(PLAYER_SAVE_FILE):
        user_data_raw = []
        user_data_in = []
        with open(PLAYER_SAVE_FILE, 'r', newline='') as user_read:
            data_reader = csv.reader(user_read)
            for i in data_reader:
                user_data_raw.append(i)
            user_data_raw.sort(key=lambda item: item[1])
            for saved_data in user_data_raw:
                user_data_in.append(saved_data[0])
    else:
        with open(PLAYER_SAVE_FILE, 'w', newline='') as generate_user_save:
            generate_user_save.close()
            user_data_in = []
    return user_data_in


def player_data_save(new_data):
    user_sentences = player_data_load()
    with open(PLAYER_SAVE_FILE, 'a', newline='') as user_save:
        data_writer = csv.writer(user_save, delimiter=',')
        count = len(user_sentences)
        data_writer.writerow([new_data, count])
    user_save.close()


def play_game(lower_bound=MIN_VALUE, upper_bound=MAX_VALUE):
    is_keep_playing = None
    while is_keep_playing != 'n':  # main game
        user_sentences = player_data_load()

        user_str_number = input('Please give me a number between {} - {} \n'.format(lower_bound, upper_bound))
        try:
            user_number = int(float(user_str_number))
        except:
            print("Sorry the value provided is not an integer.")
            user_number = None

        if user_number is not None:
            if user_number < MIN_VALUE:
                print("Sorry the number provided is too small (lower than {})".format(MIN_VALUE))
            elif user_number > MAX_VALUE:
                print("Sorry the number provided is too big (greater than {})".format(MAX_VALUE))
            else:
                if user_number > len(RANDOM_SENTENCES) - 1:
                    sentence_idx = user_number % 2
                else:
                    sentence_idx = user_number
                if user_number > len(RANDOM_NOUNS) - 1:
                    noun_idx = user_number % 2
                else:
                    noun_idx = user_number
                if user_number > len(RANDOM_VERBS) - 1:
                    verb_idx = user_number % 2
                else:
                    verb_idx = user_number
                if user_number > len(RANDOM_ADJECTIVES) - 1:
                    adjective_idx = user_number % 2
                else:
                    adjective_idx = user_number

                # generate the mad lib sentence
                print('Generating sentence...\n')
                sleep(1)
                sentence = RANDOM_SENTENCES[sentence_idx].format(
                    noun=RANDOM_NOUNS[noun_idx],
                    verb=RANDOM_VERBS[verb_idx],
                    adjective=RANDOM_ADJECTIVES[adjective_idx],
                )
                print('Your sentence is: \n{}'.format(sentence))
                if sentence not in user_sentences:
                    user_sentences.append(sentence)
                    player_data_save(sentence)

                else:
                    print("The generated sentence is already used, discarding it.")

                print("Your current mad lib is:\n")

                for sentence in user_sentences:
                    print(sentence)
        is_keep_playing = None  # reset

        while 'y' != is_keep_playing and 'n' != is_keep_playing:
            is_keep_playing = input("\nDo you want to play again? ('y' or 'n'): ")
            try:
                is_keep_playing = is_keep_playing.lower()
            except:
                is_keep_playing = None

            if 'y' != is_keep_playing and 'n' != is_keep_playing:
                print("Sorry, I did not get that.")

    print("Bye!")


play_game()

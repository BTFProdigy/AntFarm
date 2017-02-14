import random

# lists of words
SENTENCES = []
NOUNS = []
VERBS = []
ADJECTIVES = []

# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
        len(SENTENCES),
        len(NOUNS),
        len(VERBS),
        len(ADJECTIVES),
)

# user's mad lib
user_sentences = []
is_keep_playing = None

while is_keep_playing != 'n':
  user_str_number = "" # TODO: read data here

  try:
    user_number = 0 # TODO: validate and parse data here from unicode to int
  except:
    print("Sorry the value provided is not an integer.")
    user_number = None

  if user_number is not None:
    if user_number < MIN_VALUE:
      print("Sorry the number provided is too small (lower than {})".format(MIN_VALUE))
    elif user_number > MAX_VALUE:
      print("Sorry the number provided is too big (greater than {})".format(MAX_VALUE))
    else:
      # TODO: pick random indexes here
      sentence_idx = 0
      noun_idx = 0
      verb_idx = 0
      adjective_idx = 0

      # generate the mad lib sentence
      sentence = SENTENCES[sentence_idx].format(
              noun=NOUNS[noun_idx],
              verb=VERBS[verb_idx],
              adjective=ADJECTIVES[adjective_idx],
      )

      if sentence not in user_sentences:
        user_sentences.append(sentence)
      else:
        print("The generated sentence is already used, discarding it.")

      print("Your current madlib is:")

      for sentence in user_sentences:
        print(sentence)

  is_keep_playing = None # reset

  while 'y' != is_keep_playing and 'n' != is_keep_playing:
    is_keep_playing = '' # TODO: read data here
    try:
      is_keep_playing = '' # TODO: validate and normalize data here
    except:
      is_keep_playing = None

    if 'y' != is_keep_playing and 'n' != is_keep_playing:
      print("Sorry, I did not get that.")

print("Bye!")

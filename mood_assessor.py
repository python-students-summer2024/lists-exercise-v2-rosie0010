'''
Functions used to complete the assignment.
'''

import datetime
from pathlib import Path

def create_data_file_if_not_exists(filepath):
  # if the directory does not exist, create it.
  if not filepath.parent.exists():
    filepath.parent.mkdir()

  # if the file does not exist, create it.
  if not filepath.is_file():
    f = open(filepath, 'w')
    f.close()

def get_num_entries():
  """
  Count the entries in the mood diary.
  :returns: The number of entries in the mood diary.
  """
  # open the file in read mode
  filepath = Path("data/mood_diary.txt")
  create_data_file_if_not_exists(filepath)
  f = open(filepath, 'r')
  # return the number of lines.
  return len(f.readlines())

def get_latest_seven_entries():
  """
  Get the 7 most recent entries in the data file
  :returns: A list of seven entries, as ints
  """
  # figure out how many entries are in the file
  num_lines = get_num_entries()
  # open the file in read mode
  filepath = Path("data/mood_diary.txt")
  create_data_file_if_not_exists(filepath)
  f = open(filepath, 'r')
  # loop through until we reach the seventh-from-last
  counter = 0
  target = num_lines - 7
  entries = []
  for line in f:
    if counter >= target:
      mood = line[line.find(',') + 1:].strip()
      mood = int(mood)
      entries.append(mood)
    counter += 1
  return entries

def already_done_today():
  """
  Checks whether the user has already saved their mood today.
  :returns: True if so, False otherwise.
  """
  # get the date today
  date_today = str(datetime.date.today())

  # open the file in read mode
  filepath = Path("data/mood_diary.txt")
  create_data_file_if_not_exists(filepath)
  with open(filepath, 'r') as f:
    # loop through each line
    for line in f:
      # get the date from each line
      date = line[:line.find(',')]
      # print(date, date_today)
      # see if the date matches today's date
      if date == date_today:
        # return True if there is a match
        return True
    # return False if there is no match
  return False

def get_current_mood():
  """
  Get the user's current mood.
  :returns: Their current mood, as an int.
  """
  # a mapping of good responses and their int equivalents
  mood_map = {
    'happy': 2, 'relaxed' : 1, 'apathetic' : 0, 'sad' : -1, 'angry' : -2
  }
  # get a good response from the user
  response = ''
  while response not in mood_map.keys():
    response = input("What is your mood today? ")
    response = response.lower()
  # return the int for the given mood
  return mood_map[response]

def get_average_mood(entries):
  """
  Calculates the average mood, based on a list of integer entries.
  :returns: The average mood as a string, e.g. 'happy', 'relaxed', 'apathetic', 'sad', 'angry'.
  """
  # calculate the average mood
  total = 0
  # add up the entries
  for mood in entries:
    total += mood
  # divide by the number of entries
  avg = total / len(entries)
  avg = round(avg, 0)  # remove decimal place
  # a mapping of good responses and their int equivalents
  mood_map = {
    2: 'happy', 1: 'relaxed', 0: 'apathetic', -1: 'sad', -2: 'angry'
  }
  # return the string coresponding with this mood
  return mood_map[avg]

def save_mood(mood, date):
  """
  Save aa mood entry into the mood diary.
  :param mood: The user's mood, as an int.
  :param date: The date today.
  """
  # append the new mood, along with the date
  filepath = Path("data/mood_diary.txt")
  create_data_file_if_not_exists(filepath)
  f = open(filepath, 'a')    
  line = "{},{}\n".format(date, mood)
  f.write(line)

def assess_mood():
  '''
  Assess the user's mood by analyzing the contents of the mood_diary.txt file.
  '''

  # check whether the user has already entered their mood today
  if already_done_today():
    # quit, if so
    print("Sorry, you have already entered your mood today.")
    return

  # otherwise ...
  
  # get the user's current mood
  mood = get_current_mood()

  # get the date today
  date_today = datetime.date.today()

  # log it in the data file
  save_mood(mood, date_today)

  # if there have not yet been 7 entries...
  if not get_num_entries() >= 7:
    # do nothing further
    return

  # get 7 most recent entries
  entries = get_latest_seven_entries()

  # by default, the diagnosis is the average mood
  diagnosis = get_average_mood(entries)

  # count happies, sads, and apathetics
  num_happies = 0
  num_sads = 0
  num_apathetics = 0
  for mood in entries:
    if mood == 2:
      num_happies += 1
    elif mood == 0:
      num_apathetics += 1
    elif mood == -1:
      num_sads += 1
  
  # diagnose mania
  if num_happies >= 5:
    diagnosis = 'mania'
  elif num_sads >= 4:
    diagnosis = 'depressive'
  elif num_apathetics >= 6:
    diagnosis = 'schizoid'
  
  # output the diagnosis
  print("Your diagnosis: {}!".format(diagnosis))

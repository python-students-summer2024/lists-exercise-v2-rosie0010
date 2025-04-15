# Asking for a mood entry
# Every day the program is run, it should do the following once:

# ask the user to input their current mood
# validate the user's response (the code must accept the following moods: happy, relaxed, apathetic, sad, and angry)
# if the response was invalid, repeat starting from step 1 until valid response is gathered
# translate the user's response to an integer (happy -> 2, relaxed -> 1, apathetic -> 0, sad -> -1, angry -> -2)
# store the integer as a new line in a text file named mood_diary.txt within a subdirectory named data.



import os
import datetime


def diagnose_mood():
    with open("data/mood_diary.txt", "r") as f:
        lines = f.readlines()

    if len(lines) >= 7:
        latest7 = lines[-7:]

        num_happy = 0
        num_relaxed = 0
        num_apathetic = 0
        num_sad = 0
        num_angry = 0

        for line in latest7:
            mood_value = int(line.split(",")[1].strip())
            if mood_value == 2:
                num_happy += 1
            elif mood_value == 1:
                num_relaxed += 1
            elif mood_value == 0:
                num_apathetic += 1
            elif mood_value == -1:
                num_sad += 1
            elif mood_value == -2:
                num_angry += 1

        if num_happy >= 5:
            diagnosis = "manic"
        elif num_sad >= 4:
            diagnosis = "depressive"
        elif num_apathetic >= 6:
            diagnosis = "schizoid"
        else:
            average =  round(((num_happy * 2) + (num_relaxed * 1) + (num_apathetic * 0) + (num_sad * -1) + (num_angry * -2)) / 7)
            if average >= 2:
                diagnosis = "happy"
            elif average == 1:
                diagnosis = "relaxed"
            elif average == 0:
                diagnosis = "apathetic"
            elif average == -1:
                diagnosis = "sad"
            elif average <= -2:
                diagnosis = "angry"

        print(f"Your diagnosis: {diagnosis}!")
    else:
        return



def assess_mood():

    valid_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]

    date_today = str(datetime.date.today())

    if not os.path.exists("data"):
        os.makedirs("data")

    if os.path.exists("data/mood_diary.txt"):
        with open("data/mood_diary.txt", "r") as f:
            for line in f:
                if line.startswith(date_today):
                    print("Sorry, you have already entered your mood today.")
                    return

    user_mood = input('What is your current mood? ("happy", "relaxed", "apathetic", "sad" or "angry"): ').lower()
    while user_mood not in valid_moods:
        print("Invalid response")
        user_mood = input('Select: "happy", "relaxed", "apathetic", "sad" or "angry": ').lower()

    if user_mood == "happy":
        mood_value = 2
    elif user_mood == "relaxed":
        mood_value = 1
    elif user_mood == "apathetic":
        mood_value = 0
    elif user_mood == "sad":
        mood_value = -1
    else:
        mood_value = -2


    date_today = str(datetime.date.today())

    with open("data/mood_diary.txt", "a") as f:
        f.write(f"{date_today}, {mood_value}\n")


    diagnose_mood()


assess_mood()

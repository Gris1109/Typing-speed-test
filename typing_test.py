import random
import time

def get_sentence():
    "this is a function that reads a random line from a file"
    # the argment holds the file name that is should be read
    f = open('stone-of-tears.txt').read()
    sen_text = f.split("\n")
    sen_text = random.choice(sen_text)
    return sen_text


def typing_test():
    clr = ['\033[1;32m', '\033[m']
    sentence = get_sentence()
    start_time = time.time()
    user_input = input(f'Type the following sentence as fast as you can: "{clr[0]}{sentence}{clr[1]}"\n')
    end_time = time.time()
    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = words / (time_taken / 60)
    round_wpm = round(wpm, 2)
    accuracy = (len(sentence) - sum(1 for a, b in zip(sentence, user_input) if a != b)) / len(sentence)
    round_accuracy = round(accuracy, 2)
    return round_wpm, round_accuracy

round_wpm, round_accuracy = typing_test()
time.sleep(2)
print(f'Typing speed: {round_wpm} words per minute')
time.sleep(2)
print(f'Accuracy: {round_accuracy}%')


## set a while to run random line if previous line is empty
## set if condition to display more than certain words in a line

import random
from collections import defaultdict
from datetime import datetime

def print_string(n, dots):
    print(''.join('+--0--' if dots and i in dots else '+-----' for i in range(n)) + '+')

def print_wood(n):
    print('|     ' * n + '|')

def print_keyboard(dots=dict()):
    for i in range(6):
        string_dots = dots.get(i)
        print_string(5, string_dots)
        if i < 5:
            print_wood(5)

def random_pos(strings, frets):
    return (random.randint(0, strings-1), random.randint(0, frets-1))

def random_interval(strings=6, frets=5):
    interval = ((0, 0), (0, 0))
    while calc_distance(interval) < 2:
        interval = (random_pos(strings, frets), random_pos(strings, frets))
    return interval

def make_dots(interval):
    (string1, fret1), (string2, fret2) = interval
    dots = defaultdict(set)
    dots[string1].add(fret1)
    dots[string2].add(fret2)
    return dots

def string_pitch(string):
    pitch = (5 - string) * 5
    if string < 2:
        pitch -= 1
    return pitch

def calc_distance(interval):
    (string1, fret1), (string2, fret2) = interval
    return abs(string_pitch(string1) + fret1 - string_pitch(string2) - fret2)

def guess_distance():
    start_time = datetime.now()
    quiz_number = 0
    correct_answers = 0
    while True:
        interval = random_interval()
        dots = make_dots(interval)
        print_keyboard(dots)
        distance = calc_distance(interval)
        win = False
        for attempt in range(3):
            answer = input('What is the distance in semitones? ')
            if answer == 'q':
                elapsed_sec = (datetime.now() - start_time).total_seconds()
                print(f'{correct_answers} correct answers out of {quiz_number} quizzes in {elapsed_sec} seconds.')
                return
            win = int(answer) == distance
            if win:
                print('Bravo!!\n\n')
                correct_answers += 1
                break
            else:
                print(f'Wrong answer ({attempt + 1})')
        if not win:
            print(f'The correct answer was: {distance}\n\n')
        quiz_number += 1

if __name__ == '__main__':
    guess_distance()

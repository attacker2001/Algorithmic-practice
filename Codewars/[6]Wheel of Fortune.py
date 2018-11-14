# coding=utf-8

"""
Wheel of Fortune

Three candidates take part in a TV show.

In order to decide who will take part in the final game and probably become rich, they
have to roll the Wheel of Fortune!

The Wheel of Fortune is divided into 20 sections, each with a number from 5 to 100
(only mulitples of 5).

Each candidate can roll the wheel once or twice and sum up the score of each roll.
The winner one that is closest to 100 (while still being lower or equal to 100).
In case of a tie, the candidate that rolled the wheel first wins.

You receive the information about each candidate as an array of objects: each object
should have a name and a scores array with the candidate roll values.

Your solution should return the name of the winner or false if there is no winner
(all scored more than 100).

Example:

c1 = {"name": "Bob", "scores": [10, 65]}
c2 = {"name": "Bill", "scores": [90, 5]}
c3 = {"name": "Charlie", "scores": [40, 55]}
winner([c1, c2, c3]) #Returns "Bill"

Please note that inputs may be invalid: in this case, the function should return false.
"""


def check_candidates(candidates):
    if len(candidates) != 3:
        return False

    for person in candidates:
        try:
            if person['name'] == '' or type(person['name']) != str:
                return False

            if 1 <= len(person['scores']) <= 2:

                for scores in person['scores']:
                    if scores % 5 != 0:
                        return False
                    if scores > 100 or scores < 5:
                        return False
            else:
                return False

        except KeyError:
            return False

    return True


def winner(candidates):
    winner_name = ''
    winner_score = 0
    if check_candidates(candidates):

        for person in candidates:

            score_temp = 0
            for i in person['scores']:
                score_temp += i

            if 0 <= score_temp <= 100 and score_temp > winner_score:
                winner_score = score_temp
                winner_name = person['name']

        if winner_name != '':
            return winner_name
        else:
            return False

    else:
        return False


if __name__ == '__main__':
    c1 = {'name': "Bob", 'scores': [10, 65]}
    c2 = {'name': "Bill", 'scores': [90, 5]}
    c3 = {'name': "Jennifer", 'scores': [55]}

    print winner([c1, c2, c3])

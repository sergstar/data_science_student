"""Guess the number
Computer plays with itself"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Guess random number

        Args:
            number (int, optional): Guessed number. Defaults to 1.

        Returns:
            int: Count of tries
        """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(2, 500)
        if number == predict_number:
            break

    return count


def score_game(random_predict) -> int:
    """For what mean count of tries of 1000 times our algorithm guessed the number

    Args:
        random_predict ([type]): guess function

    Returns:
        int: mean count of tries
    """

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(2, 500, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f'Our algorithm guessed the number for {score} tries mean')
    return score


if __name__ == '__main__':
    score_game(random_predict)

"""print(f'Count of tries is {random_predict()}')

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100'))

    if predict_number > number:
        print('Number is smaller')
    elif predict_number < number:
        print("Number is bigger")
    else:
        print(f'Your have guessed the number. This is {number} for {count} tries')
        break
"""
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


number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))

    if predict_number > number:
        print('Number is smaller')
    elif predict_number < number:
        print("Number is bigger")
    else:
        print(f'Your have guessed the number. This is {number} for {count} tries')
        break

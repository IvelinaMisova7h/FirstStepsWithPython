# Here is another solution for score program, using function.

s = float(input('Enter score: '))


def compute_grade(score):
    if 0.9 <= score <= 1.0:
        print("A")
    elif 0.8 <= score <= 0.9:
        print("B")
    elif 0.7 <= score <= 0.8:
        print("C")
    elif 0.6 <= score <= 0.7:
        print("D")
    elif 0 < score <= 0.6:
        print("F")
    else:
        if not score <= 1.0 or score < 0.0:
            raise AssertionError('Scores must be within the 1.0 and 0.0 range!')


compute_grade(s)
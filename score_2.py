# Here is another solution for score program, using function.
try:
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
            print("Please input score between 0.1 and 1.0!")
    compute_grade(s)

except:
    if  == 'perfect':
        print('Bad score! ')
    else:
        print('Error! ')









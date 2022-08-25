# Here is another solution for pay computation, using def function.
h = float(input('Enter hours: '))
r = float(input('Enter rate: '))


def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
    print('Pay: ', pay)


compute_pay(h, r)

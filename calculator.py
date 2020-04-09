def sum(*args):
    ans = args[0]
    for _ in args[1:]:
        ans += _
    return ans


def sub(*args):
    ans = args[0]
    for _ in args[1:]:
        ans -= _
    return ans


def def_op(string):
    op = string[0]
    for i in string[1:]:
        if (i == op) & (op == '+' or op == '-'):
            op = '+'
        else:
            op = '-'
    return op


def user_command():
    try:
        op = input().split(' ')
    except ValueError:
        print('Invalid expression')
    else:
        while len(op) > 1 and '' in op:
            op.remove('')
    finally:
        return op


while True:
    entrance = user_command()

    if entrance[0] == '':
        continue

    if entrance[0] == '/exit':
        break

    if entrance[0] == '/help':
        print('The program calculates the sum and subtraction of numbers')
        continue

    try:
        ans = int(entrance[0])
    except ValueError:
        if entrance[0][0] == '/':
            print('Unknown command')
        else:
            print('Invalid expression')
        continue

    if len(entrance) == 2:
        print('Invalid expression')
        continue

    for p in range(1, len(entrance) - 1, 2):

        if entrance[p][0] == '+' or '-':
            op = def_op(entrance[p])
        if op == '+':
            ans += int(entrance[p+1])
        if op == '-':
            ans -= int(entrance[p+1])
    print(ans)
print('Bye!')

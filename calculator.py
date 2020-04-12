dict_vars = {}
ans = 0


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


def check_var(var, assign=False):
    if any(map(str.isdigit, var)):
        if assign:
            print('Invalid assignment')
        else:
            print('Invalid identifier.')
        return False
    return True


def check_key(key, assign=False):
    if key not in dict_vars:
        if assign:
            print('Invalid assignment')
        else:
            print('Unknown variable')
        return False
    return True


def lit_eval(entrance):
    ev = ''
    entrance = ''.join(entrance)
    print(entrance)
    for i in entrance:
        if i in '+-':
            ev += i
        elif check_var(i):
            if check_key(i):
                ev += str(dict_vars[i])
    print(ev)
    print('done')


while True:
    entrance = user_command()

    if entrance[0] == '':
        continue

    if entrance[0][0] == '/':
        if entrance[0] == '/exit':
            break

        if entrance[0] == '/help':
            print('The program calculates the sum and subtraction of numbers')
            continue

        else:
            print('Unknown command')
            continue

    try:
        ans = eval(' '.join(entrance))
        print(ans)
    except Exception as e:

        if type(e) == ZeroDivisionError:
            print(e)

        elif type(e) == SyntaxError:
            entrance = ''.join(entrance)
            var, val = entrance.split('=', 1)
            if check_var(var):
                if val.isdigit():
                    dict_vars[var] = int(val)
                else:
                    if check_var(val, assign=True):
                        if check_key(val):
                            dict_vars[var] = dict_vars[val]

        elif type(e) == NameError:

            if '+' in entrance or '-' in entrance:
                ans = 0
                if entrance[0].isdigit():
                    ans = int(entrance[0])
                elif check_key(entrance[0]):
                    ans = dict_vars[entrance[0]]

                op = ''

                for i in entrance[1:]:
                    if i == '+' or i == '-':
                        op = i
                        continue
                    if i.isdigit():
                        ans = eval(f'{ans} {op} {i}')
                    elif check_key(i):
                        ans = eval(f'{ans} {op} {dict_vars[i]}')
                print(ans)

            else:
                if check_key(entrance[0]):
                    print(dict_vars[entrance[0]])

        else:
            print('here')
            print(dict_vars[entrance])
print('Bye!')

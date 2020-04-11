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

    if entrance[0] == '/exit':
        break

    if entrance[0] == '/help':
        print('The program calculates the sum and subtraction of numbers')
        continue

    try:
        ans = eval(' '.join(entrance))
        print(ans)
    except Exception as e:
        entrance = ''.join(entrance)

        if type(e) == ZeroDivisionError:
            print(e)

        elif type(e) == SyntaxError:
            var, val = entrance.split('=', 1)
            if check_var(var):
                if val.isdigit():
                    dict_vars[var] = int(val)
                else:
                    if check_var(val, assign=True):
                        if check_key(val):
                            dict_vars[var] = val

        elif type(e) == NameError and ('+' not in entrance or '-' not in
                                       entrance):
            if check_var(entrance[0]):
                if check_key(entrance[0]):
                    print(dict_vars[entrance[0]])
        else:
            print('merda')
            lit_eval(entrance)
print('Bye!')

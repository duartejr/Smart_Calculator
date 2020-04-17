dict_vars = {}
ans = 0


def user_command():
    try:
        op = input().split(' ')
    except ValueError:
        print('Invalid expression')
    else:
        if len(op) > 1:
            op = list(filter(lambda x: x != '', op))

    return op


def check_var(var_in, assign=False):
    if any(map(str.isdigit, var_in)):
        if assign:
            print('Invalid assignment')
        else:
            print('Invalid identifier')
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


def lit_eval(in_eval):
    ev = ''
    in_eval = ''.join(in_eval)
    for i in in_eval:
        if i in '+-':
            ev += i
        elif check_var(i):
            if check_key(i):
                ev += str(dict_vars[i])
    print(ev)


def exc_expression(exp):
    exp = ''.join(exp)
    var_exp, val_exp = exp.split('=', 1)
    if check_var(var_exp):
        if val_exp.isdigit():
            dict_vars[var_exp] = int(val_exp)
        else:
            if check_var(val_exp, assign=True):
                if check_key(val_exp):
                    dict_vars[var_exp] = dict_vars[val_exp]


def refactor_expression(exp):
    exp = ''.join(exp).replace('^', '**')
    for key in exp:
        if key in dict_vars:
            exp = exp.replace(key, str(dict_vars[key]))
    return exp


def process_error(in_error, error):
    if isinstance(error, ZeroDivisionError):
        print(error)

    elif isinstance(error, SyntaxError):
        try:
            exc_expression(in_error)
        except ValueError:
            print('Invalid expression')

    elif isinstance(error, NameError):
        in_error = refactor_expression(in_error)
        print(int(eval(in_error)))

    else:
        print(dict_vars[in_error])


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

        print('Unknown command')
        continue

    try:
        ans = int(eval(' '.join(entrance).replace('^', '**')))
        print(ans)
    except Exception as e:
        process_error(entrance, e)

print('Bye!')

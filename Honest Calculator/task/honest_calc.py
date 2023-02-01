# write your code here
# write your code here
import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0

def is_operator(char):
    return char == "+" or char == "-" or char == "*" or char == "/"

def do_math_operation(x,char,y):
    if char == "+":
        result = x + y
    elif char == "-":
        result = x - y
    elif char == "*":
        result = x * y
    elif char == "/":
        result = x / y
    return result

def is_one_digit(a):
    a = float(a)
    return a > -10 and a < 10 and a.is_integer()

def check(x, y, char):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1.0 or y == 1.0) and char == "*":
        msg += msg_7
    if (x == 0.0 or y == 0.0) and (char == "*" or char =="+" or char == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

def print_message(index):
    if index == 10:
        print(msg_10)
    if index == 11:
        print(msg_11)
    if index == 12:
        print(msg_12)


def negotiation(result):
    msg_index = 10
    if is_one_digit(result):
        while msg_index <= 12:
            print_message(msg_index)
            decision = input()
            if decision == "y":
                msg_index += 1
            elif decision == "n":
                return True
    return False


while True:
    print(msg_0)
    calc = input()
    calc_list = calc.split()
    if calc_list[0] == "M" and calc_list[2] == "M":
        x = memory
        y = memory
    elif calc_list[0] == "M":
        x = memory
        try:
            y = float(calc_list[2])
        except ValueError:
            print(msg_1)
            continue
    elif calc_list[2] == "M":
        y = memory
        try:
            x = float(calc_list[0])
        except ValueError:
            print(msg_1)
            continue
    else:
        try:
            x = float(calc_list[0])
            y = float(calc_list[2])
        except ValueError:
            print(msg_1)
            continue
    if is_operator(calc_list[1]):
        check(x,y,calc_list[1])
        try:
            print(do_math_operation(x, calc_list[1], y))
        except ZeroDivisionError:
            print(msg_3)
            continue

        while True:
            print(msg_4)
            store_result = input()
            if store_result == "y":
                if negotiation(do_math_operation(x, calc_list[1],y)):
                    break
                else:
                    memory = do_math_operation(x, calc_list[1], y)
                    break
            elif store_result == "n":
                break
            else:
                continue

        while True:
            print(msg_5)
            want_continue = input()
            if want_continue == "y":
                break
            elif want_continue == "n":
                sys.exit()
            else:
                continue
    else:
        print(msg_2)
        continue




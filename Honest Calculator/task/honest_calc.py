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

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
        return output
    else:
        output = False
        return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    else:
        pass
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    else:
        pass
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    else:
        pass
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    else:
        pass


memory = 0
logic = True

while logic:
    print(msg_0)
    calc = x, operation, y = input().split()
    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
        check(x,y,operation)
    except TypeError:
        print(msg_1)

    except ValueError:
        print(msg_1)
    else:
        if operation == "+":
            result = x + y
            print(result)
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = result
                                print(msg_5)
                                break
                        elif answer == "n":
                            print(msg_5)
                            break
                        else:
                            pass
                else:
                    memory = result
                    print(msg_5)
                #memory = result
                #print(msg_5)
                answer = input()
                if answer == "y":
                    pass
                elif answer == "n":
                    logic = False
            elif answer == "n":
                print(msg_5)
                answer = input()
                if answer == "n":
                    logic = False
                elif answer == "y":
                    pass
            #logic = False
        elif operation == "-":
            result = x - y
            print(result)
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = result
                                print(msg_5)
                                break
                        elif answer == "n":
                            print(msg_5)
                            break
                        else:
                            pass
                else:
                    memory = result
                    print(msg_5)
                # memory = result
                # print(msg_5)
                answer = input()
                if answer == "y":
                    pass
                elif answer == "n":
                    logic = False
            elif answer == "n":
                print(msg_5)
                answer = input()
                if answer == "n":
                    logic = False
                elif answer == "y":
                    pass
            #logic = False
        elif operation == "*":
            result = x * y
            print(result)
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = result
                                print(msg_5)
                                break
                        elif answer == "n":
                            print(msg_5)
                            break
                        else:
                            pass
                else:
                    memory = result
                    print(msg_5)
                # memory = result
                # print(msg_5)
                answer = input()
                if answer == "y":
                    pass
                elif answer == "n":
                    logic = False
            elif answer == "n":
                print(msg_5)
                answer = input()
                if answer == "n":
                    logic = False
                elif answer == "y":
                    pass
            #logic = False
        elif operation == "/":
            if y != 0:
                result = x / y
                print(result)
                print(msg_4)
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                else:
                                    memory = result
                                    print(msg_5)
                                    break
                            elif answer == "n":
                                print(msg_5)
                                break
                            else:
                                pass
                    else:
                        memory = result
                        print(msg_5)
                    # memory = result
                    # print(msg_5)
                    answer = input()
                    if answer == "y":
                        pass
                    elif answer == "n":
                        logic = False
                elif answer == "n":
                    print(msg_5)
                    answer = input()
                    if answer == "n":
                        logic = False
                    elif answer == "y":
                        pass
                #logic = False
            else:
               print(msg_3)
        else:
            print(msg_2)

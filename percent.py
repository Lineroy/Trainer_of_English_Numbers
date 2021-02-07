import os
import sys
import threading
import time
import datetime
import random
import colorama
import keyboard


print("\nHello! This program was created to hone the pronunciation and spelling of English numbers "
      "- large numbers, dates, percentages. If this is what you need - go ahead! :)")

print("\nPress the space bar in the field for writing the answer to the question "
      "- there will be a menu with all the settings.")


def show(text, color=colorama.Fore.YELLOW):
    lines = ['' for _ in range(7)]
    for c in text:
        symbol = symbol_numbers[c].split('\n')
        for i, line in enumerate(symbol):
            lines[i] += color + line.strip() + ' '

    print(*lines, sep='\n')


def clear(command=False, down=None):
    if command:
        os.system("CLS || clear")
    if down is not None:
        print("\n" * down)


while True:
    try:
        print("\nChoose the topic you want to study: "
              "\n 1) - Large and small numbers;"
              "\n 2) - Percentage pronunciation;"
              "\n 3) - Dates.")

        mode = int(input(">>> "))
        if mode == 3:
            print("\nDates will be in form: \n\n*Number* of *month* *year*")
            time.sleep(1)
            print("\nAll date elements are written in words, not numbers.")
            time.sleep(2)

        if mode in list(range(1, 4)):
            break

        clear(True)
    except ValueError:
        pass

colorama.init(autoreset=True)

symbol_numbers = {
    "0": """
            ░█████╗░
            ██╔══██╗ 
            ██║░░██║ 
            ██║░░██║ 
            ╚█████╔╝ 
            ░╚════╝░""",
    "1": """ 
            ░░███╗░░
            ░████║░░ 
            ██╔██║░░ 
            ╚═╝██║░░ 
            ███████╗ 
            ╚══════╝ """,
    "2": """ 
            ██████╗░
            ╚════██╗ 
            ░░███╔═╝ 
            ██╔══╝░░ 
            ███████╗ 
            ╚══════╝ """,
    "3": """ 
            ██████╗░
            ╚════██╗ 
            ░█████╔╝ 
            ░╚═══██╗ 
            ██████╔╝ 
            ╚═════╝░ """,
    "4": """ 
            ░░██╗██╗
            ░██╔╝██║ 
            ██╔╝░██║ 
            ███████║ 
            ╚════██║ 
            ░░░░░╚═╝""",
    "5": """ 
            ███████╗
            ██╔════╝ 
            ██████╗░ 
            ╚════██╗ 
            ██████╔╝ 
            ╚═════╝░ """,
    "6": """ 
            ░█████╗░
            ██╔═══╝░ 
            ██████╗░ 
            ██╔══██╗ 
            ╚█████╔╝ 
            ░╚════╝░ """,
    "7": """ 
            ███████╗
            ╚════██║
            ░░░░██╔╝
            ░░░██╔╝░
            ░░██╔╝░░
            ░░╚═╝░░░""",
    "8": """ 
            ░█████╗░
            ██╔══██╗
            ╚█████╔╝
            ██╔══██╗
            ╚█████╔╝
            ░╚════╝░""",
    "9": """
            ░█████╗░
            ██╔══██╗
            ╚██████║
            ░╚═══██║
            ░█████╔╝
            ░╚════╝░""",
    ".": """
            ░░░
            ░░░
            ░░░
            ░░░
            ██╗
            ╚═╝""",

    "%": """  
            ██╗░██╗
            ╚═╝██╔╝
            ░░██╔╝░
            ░██╔╝░░
            ██╔╝██╗
            ╚═╝░╚═╝""",
    "t": """
            ████████╗
            ╚══██╔══╝
            ░░░██║░░░
            ░░░██║░░░
            ░░░██║░░░
            ░░░╚═╝░░░""",
    "h": """
            ██╗░░██╗
            ██║░░██║
            ███████║
            ██╔══██║
            ██║░░██║
            ╚═╝░░╚═╝"""
}

colors = [i for i in colorama.Fore.__dict__.values() if i != "\x1b[30m"]

start = input("\nWe can start? [Y]es / [N]o: ")

if start.upper() == "Y" or start.upper() == "Д":

    # Standard values (Begin);

    list_with_exceptions_one = list(range(10, 20))
    list_with_exceptions_two = list(range(2, 10))

    single_numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    date_exceptions_single = ["first", "second", "third", (8, "eighth"), (9, "ninth"), (12, "twelfth")]

    date_exceptions_dozens = {
        2: "twentieth",
        3: "thirtieth"
    }

    dozens_of_exceptions = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        8: "eighty"
    }

    units_in_the_period = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        15: "fifteen",
        18: "eighteen"
    }

    seasons = ["january", "february", "march",
               "april", "may", "june",
               "july", "august", "september",
               "october", "november", "december"]

    random_from, random_to = 0, 9999999

    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Standard values (End);

    after_continue_number, after_continue_color = None, None
    after_result = None
    after_month = None

    permission = False

    number_of_tips = 0

    while True:
        # Big numbers elements (Begin) - 1;
        values_1 = [str(random.randint(random_from, random_to)), random.choice(colors)]
        # Big numbers elements (Begin) - 1.

        # Percentage values (Begin) - 2;
        values_2 = [str(random.randint(0, 100)), random.choice(colors)]
        values_to_check = []
        # Percentage values (End) - 2.

        # Date elements (Begin) - 3;
        quantity_using_exceptions = 0
        selected_element = 0  # To select from two date values.
        ending = 0

        parts_year = str(random.randint(1000, 9999))
        day_and_year = [str(random.randint(1, 31)), parts_year[:2], parts_year[2:]]
        month = random.randint(0, 11)

        display_restart_code = ""

        for i in range(50):
            display_restart_code += random.choice(symbols)

        # Date elements (End) - 3.

        # Standard values (Begin);
        the_number = ""

        result = ""

        steps = 1
        # Standard values (End).

        clear(True, 5)

        if mode == 1:
            if after_continue_number and after_continue_color is not None:
                the_number = after_continue_number
                show(the_number, color=after_continue_color)

            else:
                the_number = values_1[0]
                show(the_number, values_1[1])

            if len(the_number) >= 4:
                steps = 2
                if len(the_number) == 7:
                    result += single_numbers[int(the_number[0])] + " million "

                the_number = the_number.rjust(6, "0")[::-1][:6][::-1]

        elif mode == 2:
            if after_result is not None:
                values_to_check = after_continue_number
                values_to_check.insert(1, ".")
                show("".join(values_to_check) + "%", color=after_continue_color)
                values_to_check.remove(".")

            else:
                values_to_check = [values_2[0]]
                if values_2[0] != "100":
                    fraction = str(random.randint(0, 99)).rjust(2, "0")
                    if fraction != "00":
                        values_to_check += list("." + fraction)
                        steps = 3

                show("".join(values_to_check) + "%", color=values_2[1])
                if len(values_to_check) != 1:
                    values_to_check.remove(".")

        else:
            if sys.getwindowsversion().platform_version[0] in [6, 7]:
                symbol_numbers["."] = """    
                                        ░░
                                        ░░
                                        ░░
                                        ░░
                                        ░░
                                        ██"""
            try:
                datetime.datetime(int(day_and_year[1]), month + 1, int(day_and_year[0]))
            except ValueError:
                day_and_year[0] = str(int(day_and_year[0]) - 1)

            print("Press the 'F10' button to see the tooltip for the months of the year.\n")

            steps = 3
            if after_result is not None:
                show(after_continue_number[0].rjust(2, "0") + "." + str(after_month + 1).rjust(2, "0") +
                     "." + "".join(after_continue_number[1:]), color=after_continue_color)
            else:
                show(day_and_year[0].rjust(2, "0") + "." + str(month + 1).rjust(2, "0") +
                     "." + parts_year, color=values_1[1])

            symbol_numbers["."] = """
                                     ░░░
                                     ░░░
                                     ░░░
                                     ░░░
                                     ██╗
                                     ╚═╝"""

            if permission:
                print("\n\n|    1 - January     |    5 - May       |    9 - September    |"
                      "\n|    2 - February    |    6 - June      |    10 - October     |"
                      "\n|    3 - March       |    7 - July      |    11 - November    |"
                      "\n|    4 - April       |    8 - August    |    12 - December    |")

                print(result)

                permission = False


            def prompt():
                global number_of_tips

                def pressed_keys(e):
                    global number_of_tips, permission
                    if e.name == "f10" and number_of_tips == 0:
                        number_of_tips += 1
                        permission = True
                        keyboard.write(" " + display_restart_code)
                        keyboard.press("enter")

                keyboard.hook(pressed_keys)
                keyboard.wait()


            threading.Thread(target=prompt, daemon=True).start()

        for i in range(steps):
            check = the_number[0:3].rjust(3, "0")
            if mode == 2:
                try:
                    check = values_to_check[selected_element].rjust(3, "0")
                except IndexError:
                    break
            elif mode == 3:
                if after_result is not None:
                    result = after_result
                    break

                elif parts_year[1:3] == "00" and parts_year[-1] in list(range(1, 10)) and selected_element == 2:
                    result += single_numbers[int(parts_year[0])] + " thousand and " + \
                              single_numbers[int(parts_year[-1])]
                    break

                else:
                    check = day_and_year[selected_element].rjust(3, "0")
                    if selected_element == 1 and parts_year.count("0") == 3:  # 2000, 3000, 4000...
                        result += single_numbers[int(parts_year[0])] + " thousand "
                        break

            selected_element += 1

            if int(check[0]) >= 1:
                if int(check[1:2]) == 0:
                    result += single_numbers[int(check[0])] + " hundred and "
                else:
                    result += single_numbers[int(check[0])] + " hundred "

            if int(check[1:]) in list_with_exceptions_one:

                if mode == 3 and selected_element == 1 and int(check[1:]) == 12:
                    result += "twelfth"
                    quantity_using_exceptions += 1

                elif int(check[1:]) in units_in_the_period:
                    result += units_in_the_period[int(check[1:])]

                else:
                    result += single_numbers[int(check[-1])] + "teen"

            else:
                counter = 1
                for o in check[1:]:
                    if int(check[1]) in list_with_exceptions_two and counter == 1:

                        if mode == 3 and int(check[1:]) in list(range(20, 40, 10)) and selected_element == 1:
                            result += date_exceptions_dozens[int(check[1])]
                            quantity_using_exceptions += 1

                        elif int(check[1]) in dozens_of_exceptions:
                            result += dozens_of_exceptions[int(check[1])]
                        else:
                            result += single_numbers[int(check[1])] + "ty"

                        counter += 1

                    else:
                        if mode == 3 and int(o) in [1, 2, 3, 5, 8, 9] and selected_element == 1:
                            quantity_using_exceptions += 1
                            if int(o) == 5:
                                result += " fifth "

                            elif int(o) in list(range(1, 4)):
                                result += " " + date_exceptions_single[int(o) - 1]

                            else:
                                get = 0
                                for d in date_exceptions_single[3:]:
                                    if int(o) in d:
                                        get = date_exceptions_single[3:].index(d)

                                result += " " + date_exceptions_single[get + 3][1]

                        else:
                            if mode == 2 and selected_element in [1, 2] and check[1] == "0" \
                                    and values_to_check[0] != str(100) and counter == 2 and int(o) == 0:

                                result += " zero "

                            else:
                                result += " " + single_numbers[int(o)]

                        counter += 1

            if 2 != mode and steps - 1 and the_number[0:3] != "000":

                if mode == 3:

                    if quantity_using_exceptions == 0 and ending == 0:
                        result += "th"

                    if selected_element == 1:
                        result += " of "

                    if ending == 0:
                        result += " " + seasons[month]

                    if selected_element == 2 and day_and_year[2] == "00":
                        result += " hundred"
                        break

                    ending += 1

                elif mode == 1 and len(the_number) == 6:
                    result += " thousand "

            elif mode == 2 and selected_element == 1 and len(values_to_check) > 1 and values_to_check[0] != str(100):
                result += " point "

            if len(the_number) > 3:
                the_number = the_number[3:6]

            result += " "

        if mode == 2 or len(values_to_check) == 1:
            result += " percent "

        try:
            result = " ".join(result.split())
        except AttributeError:
            result = " ".join(result)

        comparison = input("\n>>> ")

        accept_f10 = False

        if display_restart_code in comparison.split():
            if after_result is None:
                after_continue_number, after_continue_color = day_and_year, values_1[1]
                after_result = result
                after_month = month
                permission = True

            accept_f10 = True

        after_counter = 0

        if comparison == after_result:
            after_counter = 1

        if comparison == "":
            # Menu
            while True:
                try:
                    clear(True)
                    print("You have opened the settings menu:"
                          "\n1) - Continue to use;"
                          "\n2) - Exit from program;"
                          f"\n3) - Change maximum and minimum numbers - from {random_from} to {random_to};"
                          f"\n4) - Change training mode."
                          "\n\nSelect an item which you want to change: ")

                    select = int(input(">>> "))
                    if select in list(range(1, 5)):
                        break
                except ValueError:
                    pass

            if select == 1:
                if after_continue_number is None and after_continue_color is None:
                    if mode == 1:
                        after_continue_number, after_continue_color = values_1
                    elif mode == 2:
                        after_continue_number, after_continue_color = values_to_check, values_2[1]
                        after_result = result
                    else:
                        after_continue_number, after_continue_color = day_and_year, values_1[1]
                        after_result = result
                        after_month = month
                        number_of_tips = 0

            elif select == 2:
                break

            elif select == 3:
                print_done = None
                while True:
                    clear(True)
                    print("\nWhat do you want to change? Minimum or maximum? [Min / Max]: ")
                    change = input("\n>>> ")
                    if change.lower().startswith("min"):
                        while True:
                            try:
                                random_from = abs(int(input("\nEnter the minimum number: ")))
                                if random_from > random_to:
                                    random_from = 100000
                                    print("\nThe low returned to 100,000 because it was above the high.")

                                    time.sleep(2)

                                else:
                                    print_done = True

                                break
                            except ValueError:
                                pass

                    elif change.lower().startswith("max"):
                        while True:
                            try:
                                random_to = abs(int(input("\nEnter the maximum number: ")))
                                if random_to >= 10000000 or random_to == 0 or random_to <= random_from:
                                    random_to = 9999999
                                    print("\nThe value cannot be 0, be higher than 10.000.000"
                                          " and must not be lower or equal to the minimum. ")

                                    time.sleep(2)

                                    print("\nMaximum value has been changed to 9.999.999!")

                                    time.sleep(2)

                                else:
                                    print_done = True

                                break
                            except ValueError:
                                pass

                    if print_done:
                        clear(True, down=8)
                        print(colorama.Fore.BLUE +
                              '\t\t\t██████╗░░█████╗░███╗░░██╗███████╗██╗\n'
                              '\t\t\t██╔══██╗██╔══██╗████╗░██║██╔════╝██║\n'
                              '\t\t\t██║░░██║██║░░██║██╔██╗██║█████╗░░██║\n'
                              '\t\t\t██║░░██║██║░░██║██║╚████║██╔══╝░░╚═╝\n'
                              '\t\t\t██████╔╝╚█████╔╝██║░╚███║███████╗██╗\n'
                              '\t\t\t╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝\n')

                        time.sleep(2)

                        break

            else:
                try:
                    while True:
                        clear(True)
                        print("You have selected the menu to change the training mode,"
                              " now write the mode number you want to train. Let me remind you:"
                              "\n1) - Large numbers;"
                              "\n2) - Percentage pronunciation;"
                              "\n3) - Dates")

                        mode = int(input(">>> "))

                        if mode in list(range(1, 4)):
                            clear(True, down=8)
                            print(colorama.Fore.BLUE +
                                  '\t\t\t██████╗░░█████╗░███╗░░██╗███████╗██╗\n'
                                  '\t\t\t██╔══██╗██╔══██╗████╗░██║██╔════╝██║\n'
                                  '\t\t\t██║░░██║██║░░██║██╔██╗██║█████╗░░██║\n'
                                  '\t\t\t██║░░██║██║░░██║██║╚████║██╔══╝░░╚═╝\n'
                                  '\t\t\t██████╔╝╚█████╔╝██║░╚███║███████╗██╗\n'
                                  '\t\t\t╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝\n')

                            time.sleep(2)

                            break

                except ValueError:
                    pass

        elif comparison == result or after_counter and not accept_f10:

            clear(True, 8)
            print(colorama.Fore.GREEN +
                  '░█████╗░██╗░░██╗███████╗██╗░░░██╗░░██████╗░░█████╗░██╗░░██╗███████╗██╗░░░██╗██╗\n'
                  '██╔══██╗██║░██╔╝██╔════╝╚██╗░██╔╝░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚██╗░██╔╝██║\n'
                  '██║░░██║█████═╝░█████╗░░░╚████╔╝░░░██║░░██║██║░░██║█████═╝░█████╗░░░╚████╔╝░██║\n'
                  '██║░░██║██╔═██╗░██╔══╝░░░░╚██╔╝░░░░██║░░██║██║░░██║██╔═██╗░██╔══╝░░░░╚██╔╝░░╚═╝\n'
                  '╚█████╔╝██║░╚██╗███████╗░░░██║░░░░░██████╔╝╚█████╔╝██║░╚██╗███████╗░░░██║░░░██╗\n'
                  '░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝\n')
        elif comparison != result and not accept_f10:
            clear(True, 8)
            print(colorama.Fore.RED +
                  '\t\t\t░██╗░░░░░░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░██╗\n'
                  '\t\t\t░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██║\n'
                  '\t\t\t░╚██╗████╗██╔╝██████╔╝██║░░██║██╔██╗██║██║░░██╗░██║\n'
                  '\t\t\t░░████╔═████║░██╔══██╗██║░░██║██║╚████║██║░░╚██╗╚═╝\n'
                  '\t\t\t░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝██║░╚███║╚██████╔╝██╗\n'
                  '\t\t\t░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝\n')

        if comparison != "" and not accept_f10:

            time.sleep(3)
            if after_counter:
                decomposition_one = after_result.split()
            else:
                decomposition_one = result.split()

            decomposition_two = comparison.split()

            combination = []

            counter_split = -1

            for machine in decomposition_two:
                counter_symbol = 0
                counter_split += 1
                for part_of_machine in machine:
                    try:
                        if part_of_machine == decomposition_one[counter_split][counter_symbol]:
                            combination.append(
                                colorama.Style.BRIGHT + colorama.Fore.GREEN + decomposition_one[counter_split][
                                    counter_symbol])
                        else:
                            combination.append(
                                colorama.Style.BRIGHT + colorama.Fore.RED + decomposition_two[counter_split][
                                    counter_symbol])

                        counter_symbol += 1

                    except IndexError:
                        combination.append(colorama.Style.BRIGHT + colorama.Fore.RED + part_of_machine)

                try:
                    for i in range(len(decomposition_one[counter_split]) - len(machine)):
                        combination.append(colorama.Style.BRIGHT + colorama.Fore.RED + "?")
                except IndexError:
                    break

                combination.append(" ")

            print("\nYou: " + "".join(combination))

            if after_counter:
                print("\nReq: " + colorama.Fore.GREEN + after_result)
            else:
                print("\nReq: " + colorama.Fore.GREEN + result)

            after_continue_number, after_continue_color = None, None
            after_month = None
            after_result = None

            number_of_tips = 0

            time.sleep(3)

else:
    clear(True, 6)
    print(colorama.Fore.LIGHTYELLOW_EX +
          "\t░█████╗░░█████╗░███╗░░░███╗███████╗░░██████╗░░█████╗░░█████╗░██╗░░██╗\n"
          "\t██╔══██╗██╔══██╗████╗░████║██╔════╝░░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝\n"
          "\t██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░██████╦╝███████║██║░░╚═╝█████═╝░\n"
          "\t██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░\n"
          "\t╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░██████╦╝██║░░██║╚█████╔╝██║░╚██╗\n"
          "\t░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\n"
          "\t\t\t░██████╗░█████╗░░█████╗░███╗░░██╗██╗\n"
          "\t\t\t██╔════╝██╔══██╗██╔══██╗████╗░██║██║\n"
          "\t\t\t╚█████╗░██║░░██║██║░░██║██╔██╗██║██║\n"
          "\t\t\t░╚═══██╗██║░░██║██║░░██║██║╚████║╚═╝\n"
          "\t\t\t██████╔╝╚█████╔╝╚█████╔╝██║░╚███║██╗\n"
          "\t\t\t╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝\n")

    time.sleep(3)

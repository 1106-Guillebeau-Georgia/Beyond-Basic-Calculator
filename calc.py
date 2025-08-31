#Author: Georgia Guillebeau
#Date: 12.23.2024
#Purpose: Multi-functional calculator 

import statistics
import math
import sys

#Main Function
def main():
    calc_on = True
    valid = False
    previous_answer = 0 
    calc_mode = 0
    while calc_on is True:
        for i in range(0, 3):
            print("\n")
        operation = input("What operation would you like to compute (+, -, *, /, ^, GCF, LCM, STATS, H to view calculation history, X to Quit): ")
        calc_mode, valid, operation = check_op(operation, valid)
        user_input = [] #Empty list
        if(calc_mode == -1):
            write_to_terminal()
        elif(calc_mode == 0):
            sys.exit()
        elif(calc_mode == 1):
            factors = 2
            user_input = prompt_check_num(user_input, factors) 
            previous_answer = basic(operation, user_input)  
        elif(calc_mode == 2):
            factors = 2
            user_input = prompt_check_num(user_input, factors) 
            previous_answer = gcf(user_input) 
        elif(calc_mode == 3):
            factors = 2
            user_input = prompt_check_num(user_input, factors)
            previous_answer = lcm(user_input)
        elif(calc_mode == 4):
            factors = int(input("How many numbers are in your data set: "))
            user_input = prompt_check_num(user_input, factors)
            previous_answer_int = stats(user_input)
        yes_or_no = False
        user_active = input("\nContinue calculating? ")
        while yes_or_no == False:
            if user_active == 'Yes' or user_active == 'Y' or user_active == 'yes' or user_active == 'y':
                yes_or_no = True
                calc_on = True
                valid = False
                print("\n")
            elif user_active == 'No' or user_active == 'N' or user_active =='no' or user_active == 'n':
                yes_or_no = True
                calc_on = False
                print("\n") 
            else:
                user_active = input("\nPlease enter valid answer: ")
    return 0  #End program

#Function 1: Check Valid Input
def check_op(op, status): #Status is the current validty of the users desired operation
    type_char = 0 #Each operation has a specific interger associated with it
    while status == False:
        if(op == 'H' or op == 'h'):
            status = True
            type = -1
        elif(op == 'X' or op == 'x'):
            status = True
            type = 0
        elif (op == '+' or op == '-' or op == '*' or op == '/' or op == '^'):
            status = True
            type = 1
        elif(op == 'GCF' or op == 'gcf"'):
            status = True
            type = 2
        elif(op == 'LCM' or op == 'lcm'):
            status = True
            type = 3
        elif(op == 'Stats' or op == 'stats'):
            status = True
            type = 4
        else:
            op = input("Input valid operation (+, -, *, /, ^, GCF, LCM, H to view calculation history, X to Quit): ")
    return type, status, op

#Function 2: Check numerical Valid Input make sure enough numbers are in
def prompt_check_num(num_list, inputs): #Inputs is how many numbers the user should enter, num_list is the 'str' of numbers that stores the group of numbers
    pass_test = False #Used to loop until appropriate numbers have been entered
    while pass_test == False:
        try:
            num_list = list(map(float, input(f"\nEnter {inputs} numbers seprated by a space: ").split()))
            print("\n")
        except ValueError:
            print("Invalid.")
            continue
        else: 
            length = len(num_list)
            if(length != inputs):
                num_list = list(map(float, input(f"\nInvalid. Enter {inputs} numbers separated by a space: ").split()))
                print("\n")
            break
    return num_list   
   
#Function 3: Basic Calculations - Modify for continuous calculations
def basic(op, num_list): #Add sqaure root calculations
    result = 0
    value1 = int_convert(num_list[0])
    value2 = int_convert(num_list[1])   
    if(op == "+"):  #Use double quotes for conditionals
        result = int_convert((value1 + value2))
    elif( op== "-"):
        result = int_convert((value1 - value2))
    elif(op == "*"):
        result = int_convert((value1 * value2))
    elif(op == "^"):
        result = int_convert((value1 ** value2))
    elif(op == "/"):
        if(value2 == 0):
            print(f"\n{value1} divided by 0 is undefined")
            return 0
        else:
            result = int_convert((value1 / value2))
    if(op == "/"):
         calc_str = f"\n{value1}" + u" \u00F7 " + f"{value2} = {result}"
    else:
        calc_str = f"\n{value1} {op} {value2} = {result}"
    print(calc_str)
    write_to_file(calc_str, 1)
    return result

#Function 4: Find GCF(Greatest Common Factor)
def gcf(num_list):
    value1 = int_convert(num_list[0])
    value2 = int_convert(num_list[1])
    greatest_common_factor = 1 #Default just in case they do not have a GCF greater than 1
    if(value1 <= value2):
        cap = value1 #Cap is equal to the least factor, because that is the highest each number can be checked for GCF
    else:
        cap = value2
    i = 1
    for num in range(0, cap + 1):
        if((value1 % i) == 0 and (value2 % i) == 0):
            greatest_common_factor = i
            i += 1
        else: 
            i += 1
    int_convert(greatest_common_factor)
    calc_str = f"\nThe greatest common factor of {value1} and {value2} is {greatest_common_factor}"
    print(calc_str)
    write_to_file(calc_str, 1)

#Function 5: Find LCM(Least Common Multiple)
def lcm(num_list):
    value1 = int_convert(num_list[0])
    value2 = int_convert(num_list[1])
    if(value1 <= value2):
        cap = value1 #Cap int is equal to the least factor, because that is the highest each number can be checked for GCF
    else:
        cap = value2
    i = cap
    while(i > 1): #Since one is a universal factor, looping through it would be ineffective
        if((value1 % i) == 0 and (value2 % i) == 0):
            least_common_factor = i
            i -= 1
        else: 
            if(i == 2):
                least_common_factor = 1
            i -= 1
    least_common_multiple = int_convert((value1 / least_common_factor) * (value2 / least_common_factor) * least_common_factor) #Muliply their least common factor (which is prime) and their unique factors that pair with it
    calc_str = f"\nThe least common multiple of {value1} and {value2} is {least_common_multiple}"
    print(calc_str)
    write_to_file(calc_str, 1)


#Function 6: Statistics - sorts data set and finds min, max, mean, median, mode, range, and standard deviation
def stats(num_list):
    swap = 1 #Initialize it to one, to allow to run at least once
    while(swap != 0): #This loop sorts data set
        swap = 0
        for i in range(0, len(num_list) - 1, 1):
            if(num_list[i] > num_list[i + 1]):
                temp_int = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = temp_int
                i += 1
                swap += 1
            elif(num_list[i] < num_list[i + 1]):
                i += 1
            else: 
                i += 1
    min = int_convert(num_list[0])
    max = int_convert(num_list[-1])
    range_in_set = int_convert(max - min)
    mean = int_convert(sum(num_list)/len(num_list))
    modes = [] #Lines 182-196 find the mode
    highest_counter = 2
    for i in range(0, len(num_list), 1):
        counter = 0
        current_num = num_list[i]
        for j in range(0, len(num_list), 1):
            if(num_list[j] == current_num):
                counter += 1
        if(counter > highest_counter):
            highest_counter = counter
            modes.clear()
            modes.append(num_list[i])
        elif(counter == highest_counter):
            if num_list[i] not in modes:
                modes.append(num_list[i])
    median = int_convert(statistics.median(num_list))
    stdev = int_convert(statistics.stdev(num_list)) 
    calc_str = f"\n{num_list}" #Try to fix odd space before list and try to turn them into ints
    print(calc_str)
    write_to_file(calc_str, 0)
    calc_str = f"The statistics for your data set are: \nMinimum: {min}\nMaximum: {max}\nRange: {range_in_set}\nMean: {mean}\nMedian: {median}"
    print(calc_str)
    write_to_file(calc_str, 0)
    if(len(modes) > 1):
        calc_str = f"Mode: {modes[0]}"
        print(calc_str)
        write_to_file(calc_str, 0)
        calc_str = f"Standard Deviation: {stdev}"
        print(calc_str)
        write_to_file(calc_str, 0)
    elif(len(modes) == 1):
        calc_str = "Modes: " + ", ".join(map(str, modes))
        print(calc_str)
        write_to_file(calc_str, 0)
        calc_str = f"Standard Deviation: {stdev}"
        print(calc_str)
        write_to_file(calc_str, 0)
    else:
        calc_str = f"Standard Deviation: {stdev}"
        print(calc_str)
        write_to_file(calc_str, 0)
        calc_str = "This data set has no mode, each value appears once."
        print(calc_str)
        write_to_file(calc_str, 1) #Try to make it only incremnet by one for stats calculations
        
#Function 7: Integer Conversion - Simplifys the number to make it look pretty
def int_convert(num):
    if(num == int(num)):
        num = int(num)
    return num
    
#Function 8: Writes Calculations to File
def write_to_file(output, mode):
    try:
        with open("calcs.txt", "r") as file:
            for line in file:
                pass
            try:
                calculations = int(line)
                try:
                    with open("calcs.txt", "r+") as file:
                        lines = file.readlines()
                        if lines:
                            del lines[-1]
                            file.seek(0)
                            file.writelines(lines)
                            file.truncate()
                except IOError:
                        print("1. An I/O Error occured.")
                if(calculations > 25):
                        try:
                            with open("calcs.txt", "w") as file:
                                file.write(output)
                                file.write("\n1")
                        except IOError:
                            print("2. An I/O error occured.")
                elif(calculations <= 25):
                    if(mode == 1):
                        calculations += 1
                    try:
                        with open("calcs.txt", "a") as file:
                            file.write(output)
                            file.write(f"\n{calculations}")
                    except IOError:
                        print("3. An I/O error occured.")
                else:
                    print("Check file.\n")
            except ValueError:
                "Last line could not be converted to an integer.\n"
    except FileNotFoundError:
        print("File could not be found")

#Function 9: Writes from file to Terminal
def write_to_terminal():
    try:
        with open("calcs.txt", "r") as file:
            lines = file.readlines()
            for line in lines[:-1]:
                print(line)
    except FileNotFoundError:
        print("FIle could not be found.")

#Execute Program 
if __name__ == '__main__':
    main()
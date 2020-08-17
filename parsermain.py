from parsertable import Compiler
def tokenfunction(inputprogram):
    tokens = Compiler.tokens
    pointer = 0
    inputprogram += '$'
    token_string = ""
    while inputprogram[pointer] != '$':
        current_token = ""
        if inputprogram[pointer].isalpha() or inputprogram[pointer] == '_':
            current_token += inputprogram[pointer]
            pointer += 1
            while inputprogram[pointer].isalnum() or inputprogram[pointer] == '_':
                current_token += inputprogram[pointer]
                pointer += 1
            if current_token in tokens.keys():
                token_string += tokens[current_token]
            else:
                token_string += tokens['var']
        elif inputprogram[pointer].isnumeric():
            current_token += inputprogram[pointer]
            pointer += 1
            while inputprogram[pointer].isnumeric() or inputprogram[pointer] == '.':
                current_token += inputprogram[pointer]
                pointer += 1
            token_string += tokens['num']
        else:
            if inputprogram[pointer] in tokens:
                token_string += tokens[inputprogram[pointer]]
                pointer += 1
            else:
                nl_count = 1

                for j in range(pointer):
                    if inputprogram[j] == '\n':
                        nl_count += 1

                print("Error in line " + str(nl_count))
                exit()
    return token_string


# The parsing function
def parsefunction(token_string, new_line):

    rules = Compiler.productions

    # The parsetable is present in the file parsertable.py  We import it from there.
    parse_table = Compiler.parse_table

    token_string += "$"        # Appending $ at the end of the string.

    # Stack that is used for parsing

    stack = ['$', '0']

    # Main parsing part of the program
    pointer = 0
    while True:

        pivot = parse_table[stack[-1]][token_string[pointer]]

        if pivot[0] == 'S':
            print("Shift")
            stack.append(token_string[pointer])
            pointer += 1
            stack.append(pivot[1:])
            print(stack)
            continue
        elif pivot[0] == 'R':
            print("Reduce")
            rule = rules[int(pivot[1:])]
            for _ in range(2 * len(rule[1])):
                stack.pop()
            stack.append(rule[0])
            print(stack)
            new_pivot = parse_table[stack[-2]][stack[-1]]
            if new_pivot != 'E':
                stack.append(new_pivot)
                continue
            else:
                break
        elif pivot[0] == 'A':
            print("Program is parsed successfully.\nThanks for using the compiler!!")
            exit()
        else:
            break
    line_count = 1
    for k in range(pointer):
        if token_string[k] == new_line:
            line_count += 1
    print("Error in line " + str(line_count))


# Main function which calls the remaining functions for tokenization and parsing
def main():
    print("Enter the input filename (The name of the file which contains the input program):")
    filename=input()                                # The input file consists the input program which is to be parsed.
    file = open(filename, "r")
    inputprogram = file.read()
    print("\nInput program\n-----------------------------------------------------------------------\n")
    print(inputprogram)
    print("\n----------------------------------------------------------------------\nTOKENS GENERATED:")

    # Using the tokenfunction  for tokenization
    token_string = tokenfunction(inputprogram)
    print(token_string)
    lst=[]
    for i in token_string:
        lst.append(i)
    print("(Mapping of tokens is according to the below given dictionary:)")
    matchtoken=Compiler.tokens
    for i,j in matchtoken.items():
        print(i,j)
    print("---------------------------------------------------------------------\nPARSER RESULT")

    # Parsing the input program using parsefunction
    parsefunction(token_string, Compiler.tokens['\n'])

try:
    main()
except Exception as e:
    print("Error occured during compile time")
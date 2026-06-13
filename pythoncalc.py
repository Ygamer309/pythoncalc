print('Basic calculator by Yusuf, using pure Python.\n')
        print('''Type 1 for addition,
        2 for subtraction,
        3 for multiplication,
        4 for division
        and 5 for power under "Select operation input".\n''')

        operation = input('Select operation: ')
        if operation == '1':
            first_number = input('Number: ')
            second_number = input('Added by: ')
            print('The sum of', int(first_number), 'and', int(second_number), 'is', int(first_number) + int(second_number))
            print('Equationized: ', int(first_number), '+', int(second_number), '= ', int(first_number) + int(second_number))

        elif operation == '2':
            first_number = input('Number: ')
            second_number = input('Subtracted by: ')
            print('The difference of', int(first_number), 'and', int(second_number), 'is', int(first_number) - int(second_number))
            print('Equationized: ', int(first_number), '-', int(second_number), '= ', int(first_number) - int(second_number))

        elif operation == '3':
            first_number = input('Number: ')
            second_number = input('Multiplied by: ')
            print('The product of', int(first_number), 'and', int(second_number), 'is', int(first_number) * int(second_number))
            print('Equationized: ', int(first_number), '*', int(second_number), '= ', int(first_number) * int(second_number))

        elif operation == '4':
            first_number = input('Divisor: ')
            second_number = input('Dividend: ')
            print('The quotient of', int(first_number), 'and', int(second_number), 'is', int(first_number) / int(second_number))
            print('Equationized: ', int(first_number), '/', int(second_number), '= ', int(first_number) / int(second_number))

        elif operation == '5':
            first_number = input('Base: ')
            second_number = input('Exponent: ')
            print('The power of', int(first_number), 'and', int(second_number), 'is', int(first_number) ** int(second_number))
            print('Equationized: ', int(first_number), '^', int(second_number), '= ', int(first_number) ** int(second_number))

        else:
            print('INVALID INPUT, TYPE ERROR 301')

# import numpy as np
import pandas as pd
from IPython.display import display


class Question:
    
    def __init__(self, readme, inputs=None, outputs=None, level='easy', index=[]):
        self.__readme = readme
        self.__inputs = inputs
        self.__outputs = outputs
        self.level = level
        self.index = index

    def __str__(self):
        keys = ['Input'+str(i+1) 
                for i in range(len(self.__inputs[0]))] + ['Output']
        cheat_dict = {key: [] for key in keys}
        cheat_table = pd.DataFrame(cheat_dict)
        for i in self.index:
            cheat_list = []
            each_input = self.__inputs[i]
            each_output = self.__outputs[i]
            for n in range(len(each_input)):
                cheat_list.append(str(each_input[n]))
            cheat_list = cheat_list + [str(each_output[0])]
            sample_dict = {keys[j]: cheat_list[j] 
                           for j in range(len(keys))}
            cheat_table = cheat_table.append(sample_dict, ignore_index=True)
        
        print("Example(s):")
        display(cheat_table)
            
        return self.__readme + '\n\033[1mLevel:\033[0;0m ' + self.level + '\n'

    def __repr__(self):
        keys = ['Input'+str(i+1) 
                for i in range(len(self.__inputs[0]))] + ['Output']
        cheat_dict = {key: [] for key in keys}
        cheat_table = pd.DataFrame(cheat_dict)
        for i in self.index:
            cheat_list = []
            each_input = self.__inputs[i]
            each_output = self.__outputs[i]
            for n in range(len(each_input)):
                cheat_list.append(str(each_input[n]))
            cheat_list = cheat_list + [str(each_output[0])]
            sample_dict = {keys[j]: cheat_list[j] 
                           for j in range(len(keys))}
            cheat_table = cheat_table.append(sample_dict, ignore_index=True)
        
        print("Example(s):")
        display(cheat_table)
        
        return self.__readme + '\n\033[1mLevel:\033[0;0m ' + self.level + '\n'

    def check(self, func, cheat=False):
        correct = []
        keys = ['Input'+str(i+1) 
                for i in range(len(self.__inputs[0]))] + \
               ['Your output'] + ['Correct output'] + ['Correct']
        cheat_dict = {key: [] for key in keys}
        cheat_table = pd.DataFrame(cheat_dict)
        for each_input, each_output in zip(self.__inputs, self.__outputs):
            arg_string = ''
            cheat_list = []
            for n in range(len(each_input)):
                arg_string = arg_string + 'each_input[{0:d}]'.format(n)
                if n < len(each_input) - 1:
                    arg_string = arg_string + ', '
                cheat_list.append(str(each_input[n]))
            this_output = eval('func(' + arg_string + ')')
            if this_output == each_output[0]:
                correct.append(True)
            else:
                correct.append(False)
            cheat_list = cheat_list + [str(this_output),
                                       str(each_output[0]),
                                       str(this_output == each_output[0])]
            test_dict = {keys[i]: cheat_list[i] 
                         for i in range(len(keys))}
            cheat_table = cheat_table.append(test_dict, ignore_index=True)
        
        if cheat:
            display(cheat_table)
            
        correctness = 'incorrect' if False in correct else 'correct'
        right_ones = sum(correct)
        print('You passed {0} of the {1} tests. \n'
              'The solution is {2}'.format(right_ones,
                                           len(correct), correctness))

        
def all_questions():
    
    question_list = []
    
    readme = 'Define a function with two strings to be the input arguments. ' \
             'The output is the summation of the numerical values of the ' \
             'input strings. For example, if the inputs are "3.5" and "2.7",' \
             ' then the output is 6.2.'
    inputs = (['3.5', '2.7'], ['1.2', '5'], ['2', '4'])
    outputs = ([6.2], [6.2], [6])
    question_list.append(Question(readme, inputs, outputs, index=[0]))

    readme = 'Write a function to determine whether an integer is a ' \
             'palindrome. An integer is a palindrome when it reads the same ' \
             'backward as forward. For example, 121 is a palindrome so the ' \
             'output is True, 10 is not a palindrome so the output is False.'
    inputs = ([151], [-26000], [234565432], [1], [101], [-5], [234321])
    outputs = ([True], [False], [True], [True], [True], [True], [False])
    question_list.append(Question(readme, inputs, outputs, index=[0, 5]))
    
    readme = 'Write a function with a given argument n to return a list ' \
             'containing all positive integers no larger than n, and these ' \
             'integers can be divided by 7 but can not be divided by 5. For ' \
             'example, if n=50, then the returned list is [7, 14, 21, 28, ' \
             '42, 49].'
    inputs = ([20], [50], [100], [120], [150])
    outputs = ([[7, 14]], [[7, 14, 21, 28, 42, 49]], 
               [[7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98]],
               [[7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98, 112, 119]],
               [[7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98, 112, 119,
                 126, 133, 147]])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1]))
    
    readme = 'Write a function to determine if a given positive integer n ' \
             'is a prime number. For example, 37 is a prime the output is ' \
             'True, 10 is not so the output is False.'
    inputs = ([2], [3], [4], [5], [6], [39], [47],
              [53], [65], [61], [73], [81], [93], [97])
    outputs = ([True], [True], [False], [True], [False], [False], [True],
               [True], [False], [True], [True], [False], [False], [True])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[4, 6, 7, 9]))

    readme = 'Given a list of numbers as the first input argument, write a ' \
             'function to remove an item, as the second input argument. For ' \
             'example, the first argument is [1, 3, 2, 2, 4, 2, 5] and the ' \
             'second input number is 2, then the output is [1, 3, 4, 5] ' \
             'where the three 2s are removed.'
    inputs = ([[0, 1, 2, 3, 2, 5], 2], [[2, 3, 5, 6, 8, 3, 4, 3, 3, 4, 5], 3],
              [[0, 1, 2, 3], 4], [[8, 7, 6, 5, 5, 4, 3, 3, 2], 5])
    outputs = ([[0, 1, 3, 5]], [[2, 5, 6, 8, 4, 4, 5]], [[0, 1, 2, 3]],
               [[8, 7, 6, 4, 3, 3, 2]])
    question_list.append(Question(readme, inputs, outputs, index=[0, 2]))

    readme = 'Write a function to find the longest common prefix string ' \
             'amongst a list of strings. For example, the input argument is ' \
             '["flower", "flow", "flight"], then the output is "fl". If ' \
             'there is no common prefix among the input strings, the output ' \
             'is an empty string.'
    inputs = ([['flower', 'flow', 'flight']],
              [['coldplay', 'cold storage', 'cold', 'cold war']],
              [['dog', 'racecar', 'car']],
              [['flower', 'flow', 'flight', 'inflow']])
    outputs = (['fl'], ['cold'], [''], [''])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 3]))

    readme = 'Write a function to find the Nth number in the Fibonacci ' \
             'Sequence, In the Fibonacci Sequence, the next number is the ' \
             'sum of the two numbers before it, i.e. 0, 1, 1, 2, 3, 5, 8, ' \
             '13, 21, 34, ... For example, if N=0, then the output is 0; if ' \
             'N=1 or N=2, then the output is 1; if N=3, then the output is ' \
             '2; if N=4, then the output is 3.'
    inputs = ([0], [1], [2], [3], [4], [15], [20], [50], [80], [100], [200])
    outputs = ([0], [1], [1], [2], [3], [610], [6765], [12586269025],
               [23416728348467685], [354224848179261915075],
               [280571172992510140037611932413038677189525])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[4, 6, 9]))

    readme = 'Create a function to transform the time data as a string of ' \
             '"XX:XX:XXam" or "XX:XX:XXpm" to the number of seconds counted ' \
             'from 12:00am. For example, the input of "10:35:29am" gives an ' \
             'output of 38129; the input of 06:21:33pm gives an output of ' \
             '66093.'
    inputs = (['10:35:29am'], ['06:21:33pm'], ['03:11:12am'], ['09:45:01pm'])
    outputs = ([38129], [66093], [11472], [78301])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1]))

    readme = 'Reverse the digits of an integer. For example, if the input ' \
             'is 123, then the output is 321; if the input is -456, then ' \
             'the output is -654.'
    inputs = ([123], [-456], [392], [-14567], [-2], [1])
    outputs = ([321], [-654], [293], [-76541], [-2], [1])
    question_list.append(Question(readme, inputs, outputs, index=[0, 1]))

    readme = 'Create a function to remove all duplicates in a list, so that ' \
             'the output is a list containing the unique values of the ' \
             'original list. For example, if the input list is [2, 3, 5, 2, ' \
             '3, 4, 7], then the output must be [2, 3, 5, 4, 7].'
    inputs = ([[2, 3, 5, 2, 3, 4, 7]], [[3.5, '4', '4', True, False, False]],
              [[1.2, 3.5, 3.5, 2.4, 3.5, True, False, 0.01, 3.5, False]])
    outputs = ([[2, 3, 5, 4, 7]], [[3.5, '4', True, False]],
               [[1.2, 3.5, 2.4, True, False, 0.01]])
    question_list.append(Question(readme, inputs, outputs, index=[0, 1]))

    readme = 'Create a function with the input argument to be a string. The ' \
             'output is the longest word in the string. For example, the ' \
             'input is a string "NUS Business School is a magical place", ' \
             'then the output is the string "Business". If there are two or ' \
             'more words with the same maximum length, then return the ' \
             'first one.'
    inputs = (['NUS Business School is a magical place'],
              ["Take a sad song and make it better"],
              ['We are the champions my friend'],
              ['Manners maketh man'],
              ['All models are wrong but some are useful'],
              ['Simple is better than complex'])
    outputs = (['Business'], ['better'], ['champions'],
               ['Manners'], ['models'], ['complex'])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 5]))
    
    readme = 'Create a function to return the length of the last word in a ' \
             'string. For example, if the input is "NUS Business School is ' \
             'a magical place", then the output is 5, the length of the ' \
             'last word "place". '
    inputs = (['NUS Business School is a magical place'],
              ["Take a sad song and make it better"],
              ['We are the champions my friend'],
              ['Manners maketh man'],
              ['All models are wrong but some are useful'],
              ['Simple is better than complex'])
    outputs = ([5], [6], [6],
               [3], [6], [7])
    question_list.append(Question(readme, inputs, outputs, index=[0, 1]))
    
    readme = 'Create a function to convert a list of scores to grades. ' \
             'Grade "A" accounts for scores higher than 90; grade "B" ' \
             'accounts for scores between 80 to 89; and grade "C" accounts ' \
             'for scores between 70 and 79; scores lower than 70 are ' \
             'recorded as "D". For example, if the input is [85.5, 92, 45, ' \
             '74, 79], then the output is ["B", "A", "D", "C", "C"]. '
    inputs = ([[85.5, 92, 45, 74, 79]],
              [[25, 26, 55, 70, 80, 99]],
              [[100, 95, 85]])
    outputs = ([['B', 'A', 'D', 'C', 'C']], 
               [['D', 'D', 'D', 'C', 'B', 'A']], 
               [['A', 'A', 'B']])
    question_list.append(Question(readme, inputs, outputs, index=[0]))
    
    readme = 'Create a function to grade bubble cards. The first input ' \
             'argument is list of answers to be graded, and the second ' \
             'input argument is a list of correct answers. The function ' \
             'compares these two lists, and returns the number of answers ' \
             'to be the same. For example, if the inputs are ["A", "C", ' \
             '"B", "D", "A", "D"] and ["A", "B", "C", "D", "D", "D"], then ' \
             'the output is 3 because three values are the same in these ' \
             'two lists.'
    inputs = ([["A", "C", "B", "D", "A", "D"], 
               ["A", "B", "C", "D", "D", "D"]],
              [["A", "B", "C", "D", "D", "D"],
               ["A", "B", "C", "D", "D", "D"]],
              [["C", "B", "B", "C", "B", "D"],
               ["C", "A", "B", "D", "B", "D"]],
              [["C", "B", "A"],
               ["A", "C", "B"]])
    outputs = ([3], [6], [4])
    question_list.append(Question(readme, inputs, outputs, index=[0, 1]))

    readme = 'Create a function to present the unique values in a given ' \
             'list and the number of their appearances. The output of the ' \
             'function is a dictionary where the keys are the unique values,' \
             ' and the associated values are the number of their ' \
             'appearances. For example, if the inputs are ["A", "C", "B", ' \
             '"D", "A", "D"] then the output is {"A": 2, "C": 1, "B": 1, ' \
             '"D": 2}.'
    inputs = ([["A", "C", "B", "D", "A", "D"]], 
              [[1, 2, 2, 5, 3, 1, 2, 5, 4, 2, 4, 8, '1', '2', '1']],
              [[1.2, 3.5, '2.4', 'B', 'B', 1.2, 1.2, 'B', 3.5]])
    outputs = ([{"A": 2, "C": 1, "B": 1, "D": 2}], 
               [{1: 2, 2: 4, 3: 1, 4: 2, 5: 2, 8: 1, '1': 2, '2': 1}], 
               [{1.2: 3, 3.5: 2, '2.4': 1, 'B': 3}])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0]))
    
    readme = 'Write a function to sort a list from the smallest value to ' \
             'the largest value. For example, if the input is [3.5, 2.1, ' \
             '2.1, 3.4, 2.8, 1.2], the output is [1.2, 2.1, 2.1, 2.8, ' \
             '3.4, 3.5]. As a practice, do not use the build-in function sort.'
    inputs = ([[3.5, 2.1, 2.2, 1.6, 0.8, 3.9, 2.5]], 
              [[3.5, 2.1, 2.1, 3.4, 2.8, 1.2]],
              [[3.5, 2.1, 2.1, 3.4, 2.8, 3.4, 1.2]])
    outputs = ([[0.8, 1.6, 2.1, 2.2, 2.5, 3.5, 3.9]],
               [[1.2, 2.1, 2.1, 2.8, 3.4, 3.5]],
               [[1.2, 2.1, 2.1, 2.8, 3.4, 3.4, 3.5]])
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[0]))
    
    readme = "Write a function with one argument n, to return the nth row " \
             "of the Pascal's triangle. For example, if n=1, the output is " \
             "[1]; if n=2, then the output is [1, 1]; if n=3, then the " \
             "output is [1, 2, 1]; if n=4, then the output is [1, 3, 3, 1]. "
    inputs = ([1], [2], [3], [4], [5], [8], [10], [11])
    outputs = ([[1]], [[1, 1]], [[1, 2, 1]], [[1, 3, 3, 1]], 
               [[1, 4, 6, 4, 1]], [[1, 7, 21, 35, 35, 21, 7, 1]],
               [[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]],
               [[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]])
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[2, 4, 6]))
    
    readme = 'There are n stairs, a person standing at the bottom wants to ' \
             'reach the top of the stairs. This person can climb either 1 ' \
             'stair or 2 stairs at a time. Write a function with the input ' \
             'argument n to count the number of ways, the person can reach ' \
             'the top. For example, if n = 2, this person has 2 ways to get ' \
             'to the top; if n = 3, this person has 3 ways to get to the ' \
             'top; if n = 4, this person has 5 ways to get to the top.'
    inputs = ([1], [2], [3], [4], [5], [8], [10], [11], [14])
    outputs = ([1], [2], [3], [5], [8], [34], [89], [144], [610]) 
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[1, 4, 7]))
    
    readme = 'Given positive integers n and m as input arguments, write a '\
             'function to select all positive integers that are no larger ' \
             'than n and the summations of all digits are the same as m. ' \
             'Return these selected integers as a list. For example, if ' \
             'n = 30 and m = 5, the returned output is [5, 14, 23], if '\
             'n = 50 and m = 9, then returned output is [9, 18, 27, 36, 45]'
    inputs = ([30, 5], [50, 9], [100, 12], [200, 8])
    outputs = ([[5, 14, 23]], [[9, 18, 27, 36, 45]],
               [[39, 48, 57, 66, 75, 84, 93]],
               [[8, 17, 26, 35, 44, 53, 62, 71, 80, 107, 116, 125, 134,
                 143, 152, 161, 170]])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1]))

    readme = 'For a sequence of numbers in a list, create a new list ' \
             'containing the squares of all non-negative numbers, and cubes ' \
             'of all negative numbers. For example, if the input is ' \
             '[1, 2, 3, -4, -5, 6], then the output is [1, 4, 9, -64, -125, ' \
             '36]. As a practice, please use list comprehension.'
    inputs = ([[1, 2, 3, -4, -5, 6]], [[-2.5, 1.1, 3.0, -0.3, 0.5]])
    outputs = ([[1, 4, 9, -64, -125, 36]],
               [[-2.5**3, 1.1**2, 3.0**2, -0.3**3, 0.5**2]])
    question_list.append(Question(readme, inputs, outputs, index=[0]))

    readme = 'Given a list of numbers as the input argument, write a ' \
             'function to return a list of numbers that only appear once ' \
             'in the list. For example, if the input is [1, 2, 1, 4, 3, 2, ' \
             '0], then the  output is [4, 3, 0]; if the input is [1.5, 2, ' \
             '2.0, 3.5, 1.5, 2], then the output is [3.5].'
    inputs = ([[1, 2, 1, 4, 3, 2, 0]], [[1.5, 2, 2.0, 3.5, 1.5, 2]],
              [[2.5, 3, 3.0, 2.5, 2.5]])
    outputs = ([[4, 3, 0]], [[3.5]], [[]])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1]))

    readme = 'Given two strings as the input arguments, write a function to ' \
             'return the longest substring shared by these two input ' \
             'strings. For example, if the inputs are "cdbabcde" and ' \
             '"babcffg", then the output is "abc"; if the inputs are "This ' \
             'is an apple" and "Check the app store", then the output is ' \
             '" app". '
    inputs = (['cdeabcde', 'babcffg'],
              ['This is an apple', 'Check the app store'],
              ['DAO', '2702'])
    outputs = (['abc'], [' app'], [''])
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[0, 1]))

    readme = 'Given a string containing different types of parentheses, ' \
             'write a function to check if these parentheses matches. For ' \
             'example, if the input is "(this is {a test})", then the ' \
             'output is True; if the input is "(this is {a test)}", then ' \
             'the output is False.'
    inputs = (['(this is {a test})'], ['(this is {a test)}'],
              ['(this is )a {test}'], ['(this [is] a {test} '],
              ['(this [is a {test})'], ['this (is {a }) test'],
              ['this [is {a}} test'], ['this is a test'])
    outputs = ([True], [False], [True], [False],
               [False], [True], [False], [True])
    question_list.append(Question(readme, inputs, outputs, level=' very hard', index=[0, 1]))

    readme = 'Given a list of numbers as the input argument, write a ' \
             'function to move all zeros to the end of the list, while the ' \
             'order of the other numbers remain the same. For example, if ' \
             'the input is [0, 1, 0, 3, 12], then the output is [1, 3, 12, ' \
             '0, 0]. '
    inputs = ([[0, 1, 0, 3, 12]], [[1, 0, 0, 2.5, 3, 0, 1]],
              [[-4, -2, 1, 0, 0, 2, 0]], [[2, 3, 5]])
    outputs = ([[1, 3, 12, 0, 0]], [[1, 2.5, 3, 1, 0, 0, 0]],
               [[-4, -2, 1, 2, 0, 0, 0]], [[2, 3, 5]])
    question_list.append(Question(readme, inputs, outputs, index=[0, 2]))

    readme = 'Given two lists of sorted numbers as the input arguments, ' \
             'write a function to merge these two lists as one list, with ' \
             'all numbers sorted. For example, if the inputs are [1, 2, 4] ' \
             'and [1, 3, 4], then the output is [1, 1, 2, 3, 4, 4]. As a '\
             'practicce, do not use the built-in method sort.'
    inputs = ([[1, 2, 4], [1, 3, 4]],
              [[0, 1, 1, 2, 5, 6], [1, 2, 3]],
              [[-4, -2, 0, 0, 1, 2], [-1, 0, 2, 3, 4, 5]])
    outputs = ([[1, 1, 2, 3, 4, 4]], [[0, 1, 1, 1, 2, 2, 3, 5, 6]],
               [[-4, -2, -1, 0, 0, 0, 1, 2, 2, 3, 4, 5]])
    question_list.append(Question(readme, inputs, outputs, index=[0]))
    
    readme = 'Given a list representing the prediction of stock prices ' \
             'in a number of days, design a function to find the maximum ' \
             'profit. For example, if the input list is [7, 1, 5, 3, 6, 4] ' \
             'then the profit is 4+3=7, because you can buy the stock on ' \
             'day 2 (price=1) and sell it on day 3 (price=5) so the profit ' \
             'is 4, then you can buy on day 4 (price=3) and sell it on day 5 ' \
             '(price=6) so the profit is 3. Note that you can make the buy ' \
             'and sell transcations in the same day, but you cannot buy the '\
             'stock again before selling it, so if the given input list is ' \
             '[1, 2, 3, 4, 5] then the output is 5-1=4, or '\
             '(2-1)+(3-2)+(4-3)+(5-4)=4.'
    inputs = ([[7, 1, 5, 3, 6, 4]],
              [[1, 2, 3, 4, 5]],
              [[7, 6, 4, 3, 1]],
              [[4, 2, 1, 2, 3, 9, 0, 2]], 
              [[1, 2, 3, 2, 4, 5, 0, 1]])
    outputs = ([7], [4], [0], [10], [6])
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[0, 1, 2]))

    readme = 'At a lemonade stand, each lemonade costs $5. Customers are ' \
             'standing in a queue to buy from you, and order one at a time. ' \
             'Each customer will only buy one lemonade and pay with either ' \
             'a $5, $10, or $20 bill, and these payments are kept in a list as ' \
             'the input argument. You must provide the correct change ' \
             'to each customer, so that the net transaction is that the ' \
             "customer pays $5. Note that you don't have any change in hand " \
             'at first. Return True if and only if you can provide every ' \
             'customer with the correct change, otherwise False. For ' \
             'example, if the input is [5, 5, 5, 10, 20], then the output is ' \
             'Ture, because we collected three $5 bills to pay back the ' \
             'subsequent customers. If the input is [10, 10], then the output ' \
             'is False, because there is no way to pay back the customers. '
    inputs = ([[5, 5, 5, 10, 20]],
              [[10,10]],
              [[5, 10, 20, 5, 5, 10]],
              [[5, 5, 10, 10, 5, 20]], 
              [[5, 5, 10, 10, 20]],
              [[5, 10, 5, 10, 5, 20, 5, 10, 5, 5, 20]], 
              [[5, 10, 5, 10, 5, 20, 5, 20, 5, 5, 20]])
    outputs = ([True], [False], [False], [True], [False], [True], [False])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1, 2]))
    
    readme = 'An array is monotonic if it is either monotone increasing or ' \
             'monotone decreasing. A list a is monotone increasing if for all ' \
             'i <= j, a[i] <= a[j]. A list a is monotone decreasing if for ' \
             'all i <= j, a[i] >= a[j]. Write a function to return True if ' \
             'and only if the given input list is monotonic. For example, if ' \
             'the input is [1,2,2,3], then the output is True. If the input is ' \
             '[1,3,2], then the output is False.'
    inputs = ([[1,2,2,3]], [[6,5,4,4]], [[2, 3, 2,  4, 5]],
              [[1,3,2]], [[1,2,4,5]], [[1,1,1]], [[1, 1, 1, 2, 3, 7]],
              [[1, 2, 2, 2, 3, 3, 3, 2]])
    outputs = ([True], [True], [False], [False], [True], [True], [True], [False])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0, 1, 3]))
    
    readme = 'Given a nested list of integers, implement an iterator to flatten ' \
             'it. Each element is either an integer, or a list -- whose elements ' \
             'may also be integers or other lists. For example, if the input is ' \
             '[[1,1],2,[1,1]], then the output is [1, 1, 2, 1, 1]. If the input ' \
             'is [1,[4,[6]]], then the output is [1, 4, 6]. '
    inputs = ([[[1,1],2,[1,1]]], [[1,[4,[6]]]], [[[1], [2, [3], None], [[[4]]]]])
    outputs = ([[1, 1, 2, 1, 1]], [[1, 4, 6]], [[1, 2, 3, None, 4]])
    question_list.append(Question(readme, inputs, outputs, level='hard', index=[0, 1]))
    
    readme = 'Given a list of daily temperatures T, return a list such that, for ' \
             'each day in the input, tells you how many days you would have to wait ' \
             'until a warmer temperature. If there is no future day for which this ' \
             'is possible, put 0 instead. For example, given the list of temperatures ' \
             'T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be ' \
             '[1, 1, 4, 2, 1, 1, 0, 0].'
    inputs = ([[73, 74, 75, 71, 69, 72, 76, 73]], [[73, 74, 73, 71, 69, 75, 76, 73]],
              [[72, 71, 75, 78, 72, 73, 70, 69]], [[72, 75, 79, 71, 73, 69]])
    outputs = ([[1, 1, 4, 2, 1, 1, 0, 0]], [[1, 4, 3, 2, 1, 1, 0, 0]],
               [[2, 1, 1, 0, 1, 0, 0, 0]], [[1, 1, 0, 1, 0, 0]])
    question_list.append(Question(readme, inputs, outputs, level='medium', index=[0]))
    
    # Return all questions
    return tuple(question_list)


book = all_questions()

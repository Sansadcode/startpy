#ny part of the code placed between try and except is executed in a very
# special way – any error which occurs here won't terminate program execution.
# Instead, the control will immediately jump to the first
# line situated after the except keyword, and no other part of the try branch is executed;
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:    #another except with different value- if one of the branches is executed, all the other branches remain idle.
    print('Division by zero is not allowed in our Universe.')
except:                # it has no exception name specified - The default except branch must be the last except branch
    print('Something strange has happened here... Sorry!')

# A code with bug
temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")
else:
    print("Zero")

#example1
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")

#example2
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")


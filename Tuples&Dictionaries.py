#create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored
# in a tuple (the tuple may be a dictionary value - that's not a problem at all)
school_class = {}

while True:  # enter an "infinite" loop
    name = input("Enter the student's name: ") #read the student's name here;
    if name == '':       # if the name is an empty string (), leave the loop;
        break
    score = int(input("Enter the student's score (0-10): ")) #ask for one of the student's scores (an integer from the range 0-10)
    if score not in range(0, 11):  #if the score entered is not within the range from 0 to 10, leave the loop;
        break

    if name in school_class:   # if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
        school_class[name] += (score,)
    else:
        school_class[name] = (score,) # if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;

for name in sorted(school_class.keys()):  #iterate through the sorted students' names;
    adding = 0
    counter = 0
    for score in school_class[name]:  # initialize the data needed to evaluate the average (sum and counter)
        adding += score
        counter += 1
#we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
    print(name, ":", adding / counter)

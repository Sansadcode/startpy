#prepare a simple code able to evaluate the end time of a
# period of time, given as a number of minutes (it could be arbitrarily large).
# The start time is given as a pair of hours (0..23) and minutes (0..59).
# The result has to be printed to the console
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')

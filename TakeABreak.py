# imports the library for controlling the web browser
import webbrowser
import time

total_breaks = 3
break_count = 0

# if break_count is less then total_breaks loop through the program
print('The program started at %s.' % time.ctime())
while break_count < total_breaks:
# opens the default web browsers with the url as the argument
    
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=KKny_ia8Fvo')
    break_count += 1
import os
import sys
from datetime import datetime

initial_count = 0 #counter
dir = input() #input directory name to check
dir_tuple = [x[0] for x in os.walk(dir)] #write all folders & subfolders to the tuple

for item in dir_tuple: 
    print(str(item))

for directory in dir_tuple: #check all files in sub/folders and count them
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            initial_count += 1

result = "Total number of files in dir: "+ str(initial_count)
print("---------")
print(result)
print("---------")

now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

log_output = ['------', date_time, str(dir),result, '------'] #Write data to log.txt 
with open('log.txt', 'a') as f:
    f.writelines('\n'.join(log_output))

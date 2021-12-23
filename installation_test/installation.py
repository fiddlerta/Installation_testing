import os
import sys
from datetime import datetime

initial_count = 0
#dir = str(sys.argv[0])
#dir = "C://Users//vpfai//Desktop//jmeter_DATA"
dir = input()
[x[0] for x in os.walk(dir)]
dir_tuple = [x[0] for x in os.walk(dir)]
#print(dir_tuple,sep='\n',end='\n')
for item in dir_tuple:
    print(str(item))

for directory in dir_tuple:
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            initial_count += 1

result = "Total number of files in dir: "+ str(initial_count)
print("---------")
print(result)
print("---------")

now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("Date",date_time)

log_output = ['------', date_time, str(dir),result, '------']
with open('log.txt', 'a') as f:
    f.writelines('\n'.join(log_output))
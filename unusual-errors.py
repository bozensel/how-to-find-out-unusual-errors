from pprint import pprint
import re
from termcolor import colored
import sys

with open("file.show") as f:
    data_to_parse = f.readlines()

i = 0 # This counter is needed because we need to catch the line after where 'UNUSUAL' errors captured. 
unusual_counter = False # To inform user if there is any UNUSUAL Errors in the TS or not. 

for line in data_to_parse:
    i = i + 1
    if "UNUSUAL" in line:
        unusual_counter = True
        #print(f"{line} {data_to_parse[i]}")
        #print(data_to_parse[i])
        with open("unusual_errors.txt", "a") as f:
            f.write(f"{line} {data_to_parse[i]} {data_to_parse[i-2]}")

if unusual_counter == False:
    print(colored("\nThere is no unusual errors observed in this node.", "green"))
elif unusual_counter == True:
    print(colored("\nThere are unusual errors observed in this node. Please check attached 'unusual_errors.txt' file.", "red"))

"""

Sample output: 

  372 2022/02/01 23:25:54.944 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxx 0 FAILED"
 
  371 2022/02/01 23:25:54.942 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: cannot start xxxx to chip 10"
 
  360 2022/02/01 23:24:56.280 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxx 0 FAILED"
 
  359 2022/02/01 23:24:56.279 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: cannot start xxxx to chip 10"
 
  348 2022/02/01 23:24:01.560 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxxx 0 FAILED"
 
  347 2022/02/01 23:24:01.559 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: cannot start xxxx to chip 10"
 
  51 2022/02/01 23:27:52.419 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxxx 0 FAILED"
 
  50 2022/02/01 23:27:52.417 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: cannot start xxxx to chip 10"
 
  46 2022/02/01 23:26:57.624 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxxx 0 FAILED"
 
  45 2022/02/01 23:26:57.623 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: cannot start xxxxx to chip 10"
 
  41 2022/02/01 23:25:54.944 GMT CRITICAL: LOGGER #2002 Base B:XXX:UNUSUAL_ERROR
   "Slot B: **private**: BIST/repair for xxxxx 0 FAILED"

"""

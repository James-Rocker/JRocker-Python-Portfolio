# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:42:17 2018

@author: James
"""

from time import time, sleep

print("Press ENTER to begin, press Ctrl + C to stop")
while True:
    try:
        input()
        start_time = time()
        print("Started")
    except KeyboardInterrupt:
        print("Stopped")
        end_time = time()
        print("Total Time:", round(end_time - start_time, 2), "secs")
        sleep(2)
        break

#!/usr/bin/env python



import os
import datetime
from time import sleep
from subprocess import call 

DATE='%Y-%m-%d_%H:%M:%S'

call('fswebcam -r 1920x1080 --no-banner /home/khalob/Camera/images/' + DATE + '.jpg', shell=True)
call('git add -A', shell=True)
call('git commit -m "PI: Taking and uploading photo"', shell=True)
call('git push origin master', shell=True)


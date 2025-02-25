# create csv file with first/initial/default time
# open time log (csv) 
# retrieve last time from time log
# record current time (save in log)
# return tuple with last time and new time

import csv
from datetime import datetime


def get_time_window():

    time = datetime.now()

    with open('logs/last_run.csv', 'r+') as file:
        last_line = file.readlines()[-1]
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow([time, "None"])
    
    return (last_line.split(',')[0], str(time))


get_time_window()


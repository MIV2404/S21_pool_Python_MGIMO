import csv
import time
import random
from datetime import datetime

def current_date():
    d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return d

def timestamp():
    ts = int(round(time.time() * 1000))
    return ts

def current_temperature():
    temp = round(random.uniform(-50, 50), 1)
    return temp

def current_exchange_rate():
    rate = round(random.gammavariate(4, 2), 2)
    return rate

data = []
N = 300
for i in range(N):
    data.append([str(i + 1).ljust(7), current_date(), timestamp(), str(current_temperature()).ljust(11), current_exchange_rate()])
    time.sleep(0.1)

with open('src/task4/results.csv', 'w', newline='') as file:
    columns = ['№записи', 'текущая дата       ', 'timestamp    ', 'температура', 'курс валюты']
    writer = csv.writer(file, delimiter='|')
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)
        

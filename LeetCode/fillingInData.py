from datetime import datetime
import math
def retrivewMilSecond(time):
    dateTime = datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
    return int(dateTime.timestamp() * 1000)

def helper(time, time1, time2, level1, level2):
    # print('time', time, retrivewMilSecond(time))
    # print('time1', time1, retrivewMilSecond(time1))
    # print('time2', time2, retrivewMilSecond(time2))
    # print('level1', level1)
    # print('level2', level2)
    time = retrivewMilSecond(time)
    time1 = retrivewMilSecond(time1)
    time2 = retrivewMilSecond(time2)
    return level1 + (time - time1) * (level2-level1) / (time2 - time1)

def calcMissing(readings):
    readings_count = len(readings)
    for i in range(readings_count):
        if not readings[i]['level']:
            # find lower level1
            k = i
            record1 = None
            while k >= 0:
                if readings[k]['level']:
                    record1 = readings[k]
                    break
                else:
                    k -= 1
                    
            # find upper level2
            j = i 
            record2 = None
            while j < readings_count:
                if readings[j]['level']:
                    record2 = readings[j]
                    break
                else:
                    j += 1
                    
            if not record1 and record2:
                readings[i]['level'] = record2['level']       
            elif record1 and not record2:
                readings[i]['level'] = record1['level']            
            elif record1 and record2:
                # print('record1', record1)
                # print('record2', record2)
                # print(readings[i])
                time = readings[i]['time']
                time1 = record1['time']
                time2 = record2['time']
                readings[i]['level'] = helper(time, time1, time2, record1['level'], record2['level'])
            print(abs(readings[i]['level']))

readings_count = int(input().strip())

readings = []

for _ in range(readings_count):
    readings_item = input()
    print('=====',readings_item.split('\t'))
    # date, level = filter(lambda x: x, readings_item.split('\t'))
    date, level = readings_item.split('\t')
    try:
        level = float(level)
    except ValueError:
        level = None
    # print(level)
    readings.append({
        'time': date,
        'level': level
    })
calcMissing(readings)


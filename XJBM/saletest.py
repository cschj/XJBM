import random
import numpy as np

import pandas as pd

daysalelist = [865, 1955, 402, 1154, 1722, 126, 547, 1187, 248, 795, 1747, 1394, 1878, 1156, 695, 850, 1069, 1435, 1893, 1140, 1782, 1292, 1262, 1545, 445, 1616, 1311, 846, 971, 614, 1003, 1498, 798, 767, 674, 100, 907, 773, 428, 369, 1845, 309, 1542, 1101, 570, 112, 1005, 1514, 1783, 658, 862, 1261, 1194, 1835, 187, 1897, 82, 969, 970, 1154, 565, 1936]
monsalelist = [33942, 34080, 33623, 34019, 33632, 32584, 32558, 32918, 32504, 32684, 32258, 32356, 31271, 30935, 30880, 30755, 30017, 29953, 30032, 29922, 29440, 28520, 28489, 28421, 28711, 28453, 28734, 27505, 27628, 27627]


def daysale():
    pass
    for x in range(62):
        y = random.randrange(50, 2000)
        daysalelist.append(y)
    print(daysalelist)

def monsale():
    pass
    try:
        for x in range(30):
            # index1 = x
            y =0
            for z in range(30):
                index2 = x + z
                y += daysalelist[index2]
            monsalelist.append(y)
    except Exception as e:
        print(index2,' ',e)
    print(len(monsalelist),monsalelist)


daysaletruedict = {'day46': 112, 'day51': 862, 'day7': 547, 'day35': 674, 'day59': 970, 'day47': 1005, 'day3': 402, 'day49': 1783, 'day60': 1154, 'day14': 1156, 'day1': 865, 'day42': 309, 'day2': 1955, 'day37': 907, 'day23': 1262, 'day50': 658, 'day20': 1140, 'day9': 248, 'day21': 1782, 'day18': 1435, 'day55': 187, 'day11': 1747, 'day44': 1101, 'day34': 767, 'day48': 1514, 'day17': 1069, 'day19': 1893, 'day6': 126, 'day24': 1545, 'day32': 1498, 'day33': 798, 'day54': 1835, 'day31': 1003, 'day26': 1616, 'day8': 1187, 'day38': 773, 'day52': 1261, 'day57': 82, 'day61': 565, 'day29': 971, 'day40': 369, 'day22': 1292, 'day53': 1194, 'day27': 1311, 'day41': 1845, 'day16': 850, 'day5': 1722, 'day30': 614, 'day43': 1542, 'day39': 428, 'day4': 1154, 'day45': 570, 'day25': 445, 'day36': 100, 'day15': 695, 'day13': 1878, 'day28': 846, 'day62': 1936, 'day10': 795, 'day56': 1897, 'day12': 1394, 'day58': 969}

daysaletruelist = [{'day1': 865}, {'day2': 1955}, {'day3': 402}, {'day4': 1154}, {'day5': 1722}, {'day6': 126}, {'day7': 547}, {'day8': 1187}, {'day9': 248}, {'day10': 795}, {'day11': 1747}, {'day12': 1394}, {'day13': 1878}, {'day14': 1156}, {'day15': 695}, {'day16': 850}, {'day17': 1069}, {'day18': 1435}, {'day19': 1893}, {'day20': 1140}, {'day21': 1782}, {'day22': 1292}, {'day23': 1262}, {'day24': 1545}, {'day25': 445}, {'day26': 1616}, {'day27': 1311}, {'day28': 846}, {'day29': 971}, {'day30': 614}, {'day31': 1003}, {'day32': 1498}, {'day33': 798}, {'day34': 767}, {'day35': 674}, {'day36': 100}, {'day37': 907}, {'day38': 773}, {'day39': 428}, {'day40': 369}, {'day41': 1845}, {'day42': 309}, {'day43': 1542}, {'day44': 1101}, {'day45': 570}, {'day46': 112}, {'day47': 1005}, {'day48': 1514}, {'day49': 1783}, {'day50': 658}, {'day51': 862}, {'day52': 1261}, {'day53': 1194}, {'day54': 1835}, {'day55': 187}, {'day56': 1897}, {'day57': 82}, {'day58': 969}, {'day59': 970}, {'day60': 1154}, {'day61': 565}, {'day62': 1936}]

daysaleanadict = {}

daysaleanalist = []

def random30(monsale):
    randaysalelist = []
    rannumlist = []
    # total = 0
    for x in range(30):
        ran1 = random.randrange(monsale*0.4,monsale*0.7)
        # total += ran1
        # print(total)
        rannumlist.append(ran1)
        # total += 1
        # rannumlist.append(1)
    # print(total)

    n = np.array(rannumlist)
    # print(n)
    total = n.sum()
    # print(total)

    print(rannumlist)
    # num = 0
    list =[]
    for x in range(30):
        # num +=rannumlist[x]/total*monsale
        num2 = round(rannumlist[x]/total*monsale)
        randaysalelist.append(int(num2))
        # list.append(int(num2))
        # randaysalelist.append(rannumlist[x]/total*monsale)


    # print(list)
    print(randaysalelist)
    n = np.array(randaysalelist)
    # print(n)
    total = n.sum()
    print(total)

def daysaletrue():
    daysaletruedict = {}
    for x in range(len(daysalelist)):
        daysale = {}
        daysaletruedict['day'+str(x+1)] = daysalelist[x]

        daysale['day'+str(x+1)] = daysalelist[x]

        daysaletruelist.append(daysale)


    print(daysaletruedict)
    print(daysaletruelist)

def daysaleana():
    for x in range(len(monsalelist)):
        monsale = monsalelist[x]



if __name__ == '__main__':
    pass
    random30(100)



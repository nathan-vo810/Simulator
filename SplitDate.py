import os
from shutil import copy
import re


def whichday(date):
    hold = date.split('-')
    y = int(hold[0])
    m = int(hold[1])
    d = hold[2].split(".")
    d = int(d[0])
    wd = (d + 2 * m + (3 * (m + 1)) // 5 + y + (y // 4)) % 7
    result = []
    result.append(wd)
    result.append(m)
    return result


filePath = "C:\\Users\\ngpbh\\Desktop\\Project\\household1\\01_plugs_csv\\01\\07\\"
allFiles = os.listdir(filePath)

weekdaySum = filePath + "weekday-summer\\"
if not os.path.exists(weekdaySum):
    os.makedirs(weekdaySum)

weekdayWin = filePath + "weekday-winter\\"
if not os.path.exists(weekdayWin):
    os.makedirs(weekdayWin)

weekendSum = filePath + "weekend-summer\\"
if not os.path.exists(weekendSum):
    os.makedirs(weekendSum)

weekendWin = filePath + "weekend-winter\\"
if not os.path.exists(weekendWin):
    os.makedirs(weekendWin)

pattern = re.compile("201[2-3]-[0-1][0-9]-[0-3][0-9].csv")

for filename in allFiles:
    if (pattern.match(filename)):
        wd = whichday(filename)[0]
        m = whichday(filename)[1]
        fileUrl = filePath + filename
        if wd >= 1 and wd <= 5:
            if m >= 6 and m <= 9:
                copy(fileUrl, weekdaySum)
            else:
                copy(fileUrl, weekdayWin)
        else:
            if m >= 6 and m <= 9:
                copy(fileUrl, weekendSum)
            else:
                copy(fileUrl, weekendWin)

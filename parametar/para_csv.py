import csv


def readcsv():
    data=list()
    with open('loginshuju.csv','r') as f:
        reader=csv.reader(f)
        next(reader)   #跳过csv文件的第一行
        for item in reader:
            data.append(item)
    print(data)
    print(data[0])
    return data
for item in readcsv():
    print(item)
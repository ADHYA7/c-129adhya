import csv 
data1=[]
data2=[]

with open ('data1.csv','r')as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data1.append(row)


with open ('newData2.csv','r')as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data2.append(row)

header1=data1[0]
planet_data_1=data1[1:]

header2=data2[0]
planet_data_2=data2[1:]

headers=header1+header2
planet_data=[]
for index,data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open ('final.csv','a+')as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)
    

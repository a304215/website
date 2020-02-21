import csv
import matplotlib.pyplot as plt
import numpy as np
area = []
price = []
with open('data.csv',newline='') as csvfile:
    row = csv.reader(csvfile)
    for rows in row:
        if(rows[1]!='average price'):
            area.append(rows[0])
            price.append(rows[1])
        else:
            area.append('')
            price.append('0')
price = tuple(price)
k = plt.bar(price, .5)
plt.show()
# plt.bar(area,price)
# plt.show()

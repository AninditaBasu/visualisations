#
# Titanic
# How many people of which gender and travelling by which class survived?
# What was the ratio of survivors to total passengers
#
import csv

masterlist = []
with open('./data/titanic3.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        masterlist.append(row)
print masterlist[0]

# get survivors
survivors = []
for item in masterlist:
    if item[1]=='1':
        survivors.append(item)

# segregate survivors by class of travel and gender
males_s = []
females_s = []
males_s_1 = []
males_s_2 = []
males_s_3 = []
females_s_1 = []
females_s_2 = []
females_s_3 = []
for item in survivors:
    if item[3]=='male':
        males_s.append(item)
        if item[0]=='1':
            males_s_1.append(item)
        elif item[0]=='2':
            males_s_2.append(item)
        else:
            males_s_3.append(item)
    else:
        females_s.append(item)
        if item[0] == '1':
            females_s_1.append(item)
        elif item[0] == '2':
            females_s_2.append(item)
        else:
            females_s_3.append(item)

# segregate total passengers by class of travel and gender
males_t = []
females_t = []
males_t_1 = []
males_t_2 = []
males_t_3 = []
females_t_1 = []
females_t_2 = []
females_t_3 = []
for item in masterlist:
    if item[3]=='male':
        males_t.append(item)
        if item[0] == '1':
            males_t_1.append(item)
        elif item[0] == '2':
            males_t_2.append(item)
        else:
            males_t_3.append(item)
    else:
        females_t.append(item)
        if item[0] == '1':
            females_t_1.append(item)
        elif item[0] == '2':
            females_t_2.append(item)
        else:
            females_t_3.append(item)

# draw the chart
#
# code is from http://matplotlib.org/examples/pylab_examples/barchart_demo.html

import numpy as np
#import matplotlib.pyplot as plt
# added this code from http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
# so that the generated figure can be saved as well
import matplotlib
matplotlib.use('Agg')
#
import matplotlib.pyplot as plt

n_groups = 6

# this is the order of plots on the X-axis: 1st class males, 1st class females, 2nd class males, ...
means_total = (len(males_t_1),len(females_t_1),len(males_t_2),len(females_t_2),len(males_t_3),len(females_t_3))
#std_total = (0, 0, 0, 0, 0, 0)

means_survivors = (len(males_s_1),len(females_s_1),len(males_s_2),len(females_s_2),len(males_s_3),len(females_s_3))
#std_survivors = (0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.375

opacity = 0.75
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_total, bar_width,
                 alpha=opacity,
                 color='#F99504', #color = 'b'
                 #yerr=std_total,
                 error_kw=error_config,
                 label='Total')

rects2 = plt.bar(index + bar_width, means_survivors, bar_width,
                 alpha=opacity,
                 color='#036220', #color = 'r'
                 #yerr=std_survivors,
                 error_kw=error_config,
                 label='Survivors')

plt.xlabel('Class and gender')
plt.ylabel('No. of passengers')
plt.title('Titanic casualties')
plt.xticks(index + bar_width, ('1st class males', 'females', '2nd class males', 'females', '3rd class males', 'females'))
plt.legend()
plt.tight_layout()
plt.show()
# save the figure
plt.savefig('./examples/titanic_bargraph')
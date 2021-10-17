import matplotlib.pyplot as plt
f = open(r'files/students.csv')
lines = f.readlines()
preps = []
groups = []
marks = []
for line in lines:
    preps.append(line.split(';')[0])
    groups.append(line.split(';')[1])
    if line.split(';')[2][0] != '1':
        marks.append((line.split(';')[2])[0])
    else:
        marks.append('10')
width = 0.9

#MARKS PER PREP

labels = sorted(set(preps))
means = [[], [], [], [], [], [], [], []]
lists = [[], [], [], [], [], [], []]
prep_tmp = """prep{ii}"""
for i1 in range(7):
    ii = i1 + 1
    str1 = prep_tmp.replace('{ii}', str(ii))
    for i in range(len(preps)):
        if preps[i] == str1:
            lists[i1].append(int(marks[i]))
for i in range(8):
    i1 = i + 3
    for ii in range(7):
        means[i].append(lists[ii].count(i1))
bottoms = [[], [], [], [], [], [], []]
bottoms[0] = means[0]
for i in range(6):
    i1 = i + 1
    for ii in range(7):
        bottoms[i1].append(means[i1][ii] + bottoms[i1 - 1][ii])
    
fig, ax = plt.subplots()

label_tmp = """{num}"""
ax.bar(labels, means[0], width, label = '3')
for i in range(7):
    ax.bar(labels, means[i + 1], width, bottom = bottoms[i], label = label_tmp.replace('{num}', str(i + 4)))

ax.set_title('Marks per prep')
ax.legend()

#plt.show()
fig.savefig("Marks per prep" + ".png")

#MARKS PER GROUP
labels_ = sorted(set(groups))
means_ = [[], [], [], [], [], [], [], []]
lists_ = [[], [], [], [], [], [], []]
group_tmp = """{ii}"""
for i1 in range(6):
    ii = i1 + 751
    str12 = group_tmp.replace('{ii}', str(ii))
    for i in range(len(groups)):
        if groups[i] == str12:
            lists_[i1].append(int(marks[i]))
for i in range(8):
    i1 = i + 3
    for ii in range(6):
        means_[i].append(lists_[ii].count(i1))
bottoms_ = [[], [], [], [], [], [], []]
bottoms_[0] = means_[0]
for i in range(6):
    i1 = i + 1
    for ii in range(6):
        bottoms_[i1].append(means_[i1][ii] + bottoms_[i1 - 1][ii])

fig, ax = plt.subplots()

label__tmp = """{num}"""
ax.bar(labels_, means_[0], width, label = '3')
for i in range(7):
    ax.bar(labels_, means_[i + 1], width, bottom = bottoms_[i], label = label__tmp.replace('{num}', str(i + 4)))

ax.set_title('Marks per group')
ax.legend()

#plt.show()
fig.savefig("Marks per group" + ".png")

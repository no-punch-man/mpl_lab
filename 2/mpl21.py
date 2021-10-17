import matplotlib.pyplot as plt
f = open(r'files\frames.dat.txt')
lines = f.readlines()
i = 1
n = 1
while i < len(lines):
    x = []
    y = []
    inp = lines[i].split(' ')
    inpb = lines[i - 1].split(' ')
    for i1 in inpb:
        x.append(float(i1))
    for i2 in inp:
        y.append(float(i2))
    i += 2
    fig, axs = plt.subplots()
    axs.plot(x, y)
    plt.xlim(0, 15)
    plt.ylim(-15, 15)
    plt.title("Frame " + str(n))
    plt.grid()
    #plt.show()
    fig.savefig(str(n) + ".png")
    n += 1

import matplotlib.pyplot as plt
data = [r'C:\Users\Anton\Downloads\dead_moroz\001.dat', r'C:\Users\Anton\Downloads\dead_moroz\002.dat', r'C:\Users\Anton\Downloads\dead_moroz\003.dat', r'C:\Users\Anton\Downloads\dead_moroz\004.dat', r'C:\Users\Anton\Downloads\dead_moroz\005.dat']
for i in data:
    f = open(i, 'r')
    x = []
    y = []
    N = int(f.readline())
    for i1 in range(N):
        line = f.readline()
        inp = line.split(' ')
        x.append(float(inp[0]))
        y.append(float(inp[1]))
    fig = plt.figure()
    plt.plot(x, y, 'bo')
    plt.title("Number of points: %d" %N)
    fig.savefig(i[-7:-1] + ".png")


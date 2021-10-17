import matplotlib.pyplot as plt
data = [r'files\001.dat', r'files\002.dat', r'files\003.dat', r'files\004.dat', r'files\005.dat']
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


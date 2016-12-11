# It is written under Python 2.7
# Not using jupyter is because the minepy lib is not in anaconda.

import numpy as np
from minepy import MINE

data = np.genfromtxt('recs2009_public.csv',delimiter=',', dtype="float")
# The first line is description and should be deleted.
data = np.delete(data, 0, axis=0)

# total_heat = data[:, 908]
total_elec = data[:, 907]
# heat_areas = data[:, 829]

# consumption per area as output Y
# Y = np.divide(total_heat, heat_areas)
Y = total_elec
# print min(Y)
# print min(heat_areas)
# print data[0, 908], data[2, 829]
index = []

fo = open('MIC_results.txt', 'w')
for i in range(1, len(data[0])):
    X = data[:, i]
    mine = MINE(alpha=0.6, c=15)
    mine.compute_score(X, Y)
    # index.append(mine.mic())
    fo.write(str(mine.mic())+'/n')
    print (i+1, mine.mic())

fo.close()






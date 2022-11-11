import random

import matplotlib.pyplot as plt

# 1000 tirages entre 0 et 150

x = [random.randint(0, 150) for i in range(1000)]

n, bins, patches = plt.hist(x, 50, facecolor='b', alpha=0.5)

plt.xlabel('Mise')

plt.ylabel('Probabilité')

plt.axis([0, 150, 0, 0.02])

plt.grid(True)

plt.show()

# NUL NE FONCTIONNE PAS !!!! ARNAQUE

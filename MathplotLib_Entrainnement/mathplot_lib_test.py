import matplotlib.pyplot as plt

plt.title("Danger de la vitesse")

plt.plot([50, 100, 150, 200], [1, 2, 3, 4])
plt.plot([50, 100, 150, 200], [2.5, 2.5, 2.5, 2.5])
plt.plot([125, 125, 125, 125], [1, 2, 3, 4])
plt.plot([50, 100, 150, 200], [4, 3, 2, 1])

plt.xlabel('Vitesse')

plt.ylabel('Nb Accidents par secondes')

plt.show()

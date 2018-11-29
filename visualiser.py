import matplotlib.pyplot as plt
import numpy as np

x = np.array([
    [1, 2, 2],
    [1, 1, 2],
    [2, 4, 3],
])

data = tuple(x.mean(axis=0))

index = np.arange(3)
bar_width = 0.5

plt.bar(index, data, bar_width)
plt.xticks(index, ('Garage', 'Bedrooms', 'Storeys'))

plt.show()

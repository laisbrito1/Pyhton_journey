import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Renner', 'Marisa', 'John John', 'You jeans'])
y= np.array ([300, 200, 120, 360])
plt.bar(x,y)
plt.title('Calças para jovens de 1 anos')
plt.show()
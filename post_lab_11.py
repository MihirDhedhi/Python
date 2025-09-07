import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('C:\\Users\mihir\OneDrive\Desktop\MU.jpg')
img_array = np.array(img)
padded_img = np.pad(img_array, pad_width=((50, 50), (50, 50), (0, 0)), mode='constant', constant_values=0)
plt.imshow(padded_img)
plt.title('Image with Black Border')
plt.show()

import matplotlib.pyplot as plt
x1 = [10, 20, 30]
y1 = [20, 40, 10]
plt.plot(x1, y1, label="Line 1")
x2 = [10, 20, 30]
y2 = [40, 10, 30]
plt.plot(x2, y2, label="Line 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Lines on One Plot")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(languages, popularity)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")
plt.show()


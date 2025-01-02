import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imred("logo.jpg")
plt.imshow(img)
plt.imsave("image_new.png",img)
from PIL import Image
import imageio

file_names = ["pofak1.jpg", "pofak2.jpg", "pofak3.jpg"]
images = [ ]

for file in file_names:
  image = Image.open(file)
  images.append(image)

imageio.mimsave("pofak.gif", images, duration=250, loop = 0)




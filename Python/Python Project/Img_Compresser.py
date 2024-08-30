import PIL
from PIL import Image
from tkinter.filedialog import *

import PIL.Image

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize(myHeight, myWidth)
save_path = asksaveasfilename()
img.save(save_path + "Compressed.jpg")

# ---> INCOMPLETE <---
# import PIL
# from PIL import Image
# from tkinter.filedialog import *

# filePath = askopenfilename()
# img = PIL.Image.open(filePath)
# myheight, mywidth = img.size

# img = img.resize((myheight, mywidth), PIL.Image.ANTIALIAS)
# save_path = asksaveasfile()

# img.save(save_path+"_compressed.JPG")



import PIL
from PIL import Image
from tkinter.filedialog import *

filePath = askopenfilename()
img = PIL.Image.open(filePath)
myheight, mywidth = img.size

img = img.resize((myheight, mywidth), PIL.Image.LANCZOS)
save_path = asksaveasfilename(defaultextension=".jpg")

img.save(save_path+"_compressed.jpg")

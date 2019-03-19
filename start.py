from PIL import Image
from PIL import ImageDraw
import numpy as np
import os

def drawCircle(img,x,y,r,color = (255,0,0,0)):
    draw = ImageDraw.Draw(image)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
def numpyToImage(np_data):
    return Image.fromarray(np.uint8(np_data))

image = Image.open("data3.jpg").convert('LA')
image_array = np.array(image)


diff_color = 230
diff_res = image_array<=diff_color
diff2_res = image_array>diff_color
image_array[diff_res] = 0
image_array[diff2_res] = 255


i = numpyToImage(image_array)
i.show()
image.close()

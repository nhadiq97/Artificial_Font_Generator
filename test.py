# -*- coding: utf-8 -*-
# import sys
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np


# print(sys.version_info)
image = Image.new('RGB', (700, 40))
draw = ImageDraw.Draw(image)
# Make sure the location to the font is correct
draw.text((40,5), 'നമ്മുടെ മലയാളം അടിപൊളിയായി ഇമേജിൽ വരുന്നു', font=ImageFont.truetype('Mal_Fonts/Manjari-Bold.ttf', 25))

plt.imshow(np.asarray(image))
plt.show()


from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
ct=ColorThief("dog_image.jpg")

palette=ct.get_palette(color_count=10)

plt.imshow([[palette[i] for i in range(4)]])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))
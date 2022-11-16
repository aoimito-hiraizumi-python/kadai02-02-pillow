from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("images/konjikido_01.jpg")

img_resize = img.resize((700, 400))

img_resize.save("images/resized_konjikido_01.jpg")

txt = "平泉 最高"

color = (0, 252, 231)

font = ImageFont.truetype("ヒラギノ丸ゴ ProN W4.ttc", 72)

draw = ImageDraw.Draw(img_resize)

(font_w, font_h), (offset_x, offset_y) = font.font.getsize(txt)
img_resize_w, img_resize_h = img_resize.size

# print("{}, {}, {},{}".format(font_w, font_h, img_resize_w, img_resize_h))

pos = ((img_resize_w - font_w) / 2, (img_resize_h - font_h) / 2)

draw.text(
    pos,
    txt,
    color,
    font=font
)



img_resize.show()

img_resize.save("images/new_konjikido_01.jpg")

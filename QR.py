from PIL import Image,ImageDraw
import qrcode
data="https://nishaph.github.io/food/"
img=qrcode.make(data)
img.save("foodnisha.png")

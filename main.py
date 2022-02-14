from PIL import Image, ImageFont, ImageDraw

oop = Image.open("samples/blue.png")
oop_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 75)
oop_text = "Практика №88"
oop_editeable = ImageDraw.Draw(oop)
oop_editeable.text((10, 495), oop_text, (0, 0, 0), font=oop_font)
oop.save('result.png')

oop_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 60)
oop_text = "88.88.2022"
oop_editeable = ImageDraw.Draw(oop)
oop_editeable.text((934, 550), oop_text, (0, 0, 0), font=oop_font)
oop.save('result.png')

from PIL import Image
import glob

frames = []

for i in range(999):
	new_frame = Image.open(f"pngs/{i}.png")
	frames.append(new_frame)

frames[0].save("gf.gif", format="GIF", append_images=frames[1:], save_all=True, duration=30, loop=0)
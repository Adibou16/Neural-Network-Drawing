from PIL import Image
import glob

img_list = [i for i in glob.glob("*.jpg")]

print(img_list)

for i in img_list:
    img = Image.open(i)
    img = img.resize((128, 128))
    img.save("resized_test_imgs\\" + i)

print("done")

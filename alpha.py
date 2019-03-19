from PIL import Image
from PIL import ImageDraw
import numpy as np
import os,sys

def numpyToImage(np_data):
    return Image.fromarray(np.uint8(np_data))

if len(sys.argv) < 3:
    print("输入的参数有问题 调用格式：")
    print(".exe base图片路径 diff图片路径1 diff图片路径2 diff图片路径3 ...")
    print("按回车退出")
    input()
    sys.exit(0)

base_image_path = sys.argv[1]
diff_image_paths = sys.argv[2:]
base_image_dir = os.path.dirname(base_image_path)
image_base = Image.open(base_image_path)
image_base_array = np.array(image_base)

print("输入base图片：%s" % os.path.basename(base_image_path))
print("开始合成...")
if not os.path.exists( base_image_dir +  "/合成图片" ):
    os.mkdir(base_image_dir +  "/合成图片")
for diff_path in diff_image_paths:
    diff_file_name = os.path.basename(diff_path)
    print("开始合成拆分图片：%s" % diff_file_name)
    image_diff = Image.open(diff_path)
    image_diff_array = np.array(image_diff)
    if not image_base_array.shape == image_diff_array.shape:
        print("Base图与 Diff图尺寸不同，跳过此次合成")
        continue
    new_image_array = image_base_array + image_diff_array
    new_image = numpyToImage(new_image_array)

    new_image.save(base_image_dir + "/合成图片/%s" % diff_file_name)

    new_image.close()
    image_diff.close()

image_base.close()
print("Over")
# r,g,b,a = image.split()








import os
from PIL import Image
import pytesseract

image_folder = "image_output/"
output_txt = "extracted_words.txt"

# 下载好tesseract.exe，下面是你的安装路径
pytesseract.pytesseract.tesseract_cmd = r'D:\Application\Tesseract-OCR\tesseract.exe'

# Open the output text file for writing
with open(output_txt, 'w', encoding='utf-8') as output_file:
    for image_filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_filename)
        image = Image.open(image_path)

        x1 = 100
        y1 = 310
        x2 = 410
        y2 = 3300
        crop_box = (x1, y1, x2, y2)
        cropped_image = image.crop(crop_box)

        # 下面注释是显示裁剪出来的图像，你可以看看你上面的标注对不对
        # cropped_image.show()

        extracted_text = pytesseract.image_to_string(cropped_image, lang='eng')  # 识别，lang = 'eng'表示识别为英文
        extracted_words = extracted_text.split()  # 文本分割

        # 写入txt文件，单词之间换行
        for word in extracted_words:
            output_file.write(word + '\n')

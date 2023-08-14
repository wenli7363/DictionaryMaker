import fitz  # PyMuPDF
from tqdm import tqdm

pdf_file = "gre_words.pdf"
image_folder = "image_output/"

# 打开PDF文件
pdf_document = fitz.open(pdf_file)

# 配置图像分辨率
image_resolution = 300  # 设置为你想要的分辨率，以每英寸像素数为单位

# 使用 tqdm 创建进度条
progress_bar = tqdm(total=pdf_document.page_count, desc="Converting pages", unit="page")

# 遍历每一页并保存为图像
for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    zoom = image_resolution / 72.0  # 计算缩放比例，以使分辨率一致
    mat = fitz.Matrix(zoom, zoom)
    pixmap = page.get_pixmap(matrix=mat)
    image_path = f"{image_folder}page_{page_num + 1}.png"
    pixmap.save(image_path, "png")
    
    # 更新进度条
    progress_bar.update(1)

# 关闭PDF文件
pdf_document.close()

# 关闭进度条
progress_bar.close()

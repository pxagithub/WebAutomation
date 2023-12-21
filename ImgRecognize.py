from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pytesseract
import sympy as sp
from PIL import Image, ImageOps, ImageFilter,ImageEnhance
import string
import requests
from io import BytesIO
import base64

# 调用 EDGE 浏览器
driver = webdriver.Edge()
url = "https://zhxy.jxyjxy.com:8078/lyuapServer/login?service=http://218.87.96.236:4106/shiro-cas"
driver.get(url)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

# 使用WebDriver的page_source属性获取页面源代码
page_source = driver.page_source

# 使用BeautifulSoup解析页面源代码
soup = BeautifulSoup(page_source, 'html.parser')

# 直接查找验证码图片元素
img = driver.find_element(By.CSS_SELECTOR, 'form img')
img_src = img.get_attribute('src')
print("Image source:", img_src)

 
def preprocess_image(image):
    # 调整大小
    image = image.resize((300, 100))
    # 灰度化
    image = ImageOps.grayscale(image)
    # 二值化
    threshold = 150  # 调整阈值
    image = image.point(lambda p: p > threshold and 255)

    # 去噪
    image = image.filter(ImageFilter.MedianFilter(size=3))

    # 增强对比度
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # 显示预处理后的图像（可选）
    #image.show()

    return image

# Set the path to the Tesseract executable (update this path according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_and_calculate_result(img_src):
    # 去除数据头部
    base64_data=img_src.replace("data:image/png;base64,","")
    # 解码 base64 数据
    img_bytes =  base64.b64decode(base64_data)
    # 读取为图像对象
    image = Image.open(BytesIO(img_bytes))
    image.show()

    # Apply preprocessing (you can customize this based on your needs)
    image = preprocess_image(image)

    # Use Tesseract OCR to extract text from the image
    recognize_text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789+/*=?')
    expression_text = recognize_text.replace("=?","")

    try:
        # Evaluate the expression using sympy
        result = sp.sympify(expression_text)
        return expression_text, result
    except sp.SympifyError:
        return expression_text, "Error: Unable to evaluate the expression"

if __name__ == "__main__":
    # Provide the path to the image containing the math expression

    expression, result = recognize_and_calculate_result(img_src)

    print("Math Expression:", expression)
    print("Result:", result)
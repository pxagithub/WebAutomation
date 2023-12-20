from PIL import Image
import pytesseract
import sympy as sp
from PIL import Image, ImageOps, ImageFilter,ImageEnhance
import string

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

def recognize_and_calculate_result(image_path):
    # Open the image
    image = Image.open(image_path)

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
    image_path = "authCode.png"

    expression, result = recognize_and_calculate_result(image_path)

    print("Math Expression:", expression)
    print("Result:", result)
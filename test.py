from PIL import Image
import base64
from io import BytesIO

# 图像数据字符串
img_data = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAZCAIAAABIPBwcAAACbUlEQVR42sWYO07FQAxFZyv0iA2w%0ABSQKVoH0OhooKFgRomYLdLQshkgjGT9/ru84eUJykSgTZ3xy/UnG18/3tI/3z83ktG1LfsDio/Zz%0AoI3D9zed7Od1UVil8/Dq2BPnRcXV28whos6uUrCYTes1/5iJ/C2XhaVtPyxZ09g0uES67S0YPBQG%0Alt4ov5WeuHbCYsoughXy6gmb0QsJ90BeZCxZ+CMM0sSAH/B0f2es3Nbjy43xDNY/n27FmCYA3oGc%0Avl69ifHiSmHxGuZhbYwMrHkAeGlSGa+yIJhLmlSGLE3Dtlw1LPBitavJazISZFnYGtBcqWGR6emP%0ADZo1WCbC1a4xYZWJLAs2RtNCmnJqpOQXl7BwkpKwztIwrLVkBwzTMHOixcXDKjuP3Ht9esCWSaaE%0A9VfgM1h8TwQ1KytbOhkzE1i6YAHBrsLSlZ7U5sjkDagZCWg6wiuEpQv8vEUO/BN9afcFnhkJQa4I%0AKWYUPyvwnkKpshBxKS5NLduWhhXWe/77LBuMJikwwfowU1hYXKDA6ebIz5MgDfUanYzGSZmGxr/A%0AYhQwbYDhLRsCerCyR2QQw6lKYHm3PVggOn8phVWmoaDRrnWNBwnOJIvnZco8+YcHFy88yiJYYCTJ%0A8PtW6AfUci7xz8rGd0NqDyzTB8s+FsDCbz70ZUj1vmyzrPStMNsk0xP1Gl2zwLgQK4uZ48ka3xup%0A+Ykcfw8yvJjvDS+uwf9pKOs980O9fP9LP5jIPxAkrIxX3A3Jt0c2RzJgHhY5PTIDak9cY+k/JxZg%0AGTAT7SGwQFEr5wPAayx905fZyofdvqstLhwpM4H/AhbhqltMvE75AAAAAElFTkSuQmCC"

# 去掉可能存在的填充字符
padding = len(img_data) % 4
if padding:
    img_data += '=' * (4 - padding)

# 解码 Base64 数据
try:
    img_bytes = base64.b64decode(img_data)
    img_pillow = Image.open(BytesIO(img_bytes))
    img_pillow.save("saved_image_pillow.png")
    print("Pillow decoded image saved successfully.")
except Exception as e:
    print("Decoding with Pillow failed:", e)

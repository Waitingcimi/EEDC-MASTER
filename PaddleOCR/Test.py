from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, use_gpu=True)

img_path = 'imgs/Grade7History4.jpg'

result = ocr.ocr(img_path, cls=True)

# 输出结果
for line in result:
    print(line)
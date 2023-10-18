import PIL
import pytesseract
from PIL import ImageEnhance, ImageGrab

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\Henrik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)

while True:
    image = ImageGrab.grab(bbox=(500, 0, 1650, 1000))

    # Enhance the contrast of the image
    enhancer = PIL.ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2.0)  # Increase contrast

    # Increase the resolution of the image
    scale_factor = 2  # adjust this as needed
    enhanced_image = enhanced_image.resize(
        (enhanced_image.size[0] * scale_factor, enhanced_image.size[1] * scale_factor)
    )

    # Save the enhanced image
    enhanced_image.save("imgs/enhanced_image.png")

    values = pytesseract.image_to_string(enhanced_image)

    print(values)

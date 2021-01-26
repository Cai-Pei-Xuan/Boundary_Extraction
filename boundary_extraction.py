from PIL import Image, ImageDraw

# 取得座標(x, y)附近的像素值
def getpixel(image, x, y):
    pixel_list = []

    # 取得3*3的像素值
    for i in range(-1, 2):
        for j in range(-1, 2):
            pixel = image.getpixel((x + j ,y + i))
            pixel_list.append(pixel)
    
    return(pixel_list)

# 將黑白圖片做Erosion
def Erosion(BinaryImage):
    width, height = BinaryImage.size
    ErosionImage = Image.new(BinaryImage.mode, (width, height) , (0))
    draw = ImageDraw.Draw(ErosionImage)
    
    # Square Structuring Mask(dot is the center)
    Mask = [255, 255, 255,
            255, 255, 255,
            255, 255, 255]
    
    center_pixel = Mask[5]

    for x in range(1, width - 1):       
        for y in range(1, height - 1):
            pixel_list = getpixel(BinaryImage, x, y)        # 取得黑白圖片中座標(x,y)附近的像素值

            # 如果pixel_list eroded by Mask
            if pixel_list == Mask:
                draw.point((x, y), fill = (center_pixel))   # 將像素值填進新圖中

    return ErosionImage

# 將黑白圖片減去ErosionImage
def Boundary_Extraction(BinaryImage, ErosionImage):
    width, height = BinaryImage.size
    BoundaryExtractionImage = Image.new(BinaryImage.mode, (width, height), (0)) 
    draw = ImageDraw.Draw(BoundaryExtractionImage)

    for x in range(0, width):       
        for y in range(0, height):
            new_pixel = BinaryImage.getpixel((x, y)) - ErosionImage.getpixel((x, y))        # 將兩者的像素值相減
            draw.point((x, y), fill = (new_pixel))          # 將像素值填進新圖中
    
    return BoundaryExtractionImage

def main():
    OriginalImage = Image.open('star.jpg')                  # 載入原圖

    BinaryImage = OriginalImage.convert('1')                # 將原圖轉成黑白圖片

    # 創建Erosion的圖
    ErosionImage = Erosion(BinaryImage)                     # 將黑白圖片做Erosion
    ErosionImage.save("ErosionImage.jpg")

    # 創建Boundary_Extraction的圖
    BoundaryExtractionImage = Boundary_Extraction(BinaryImage, ErosionImage)                # 將黑白圖片減去ErosionImage
    BoundaryExtractionImage.save("BoundaryExtractionImage.jpg")


if __name__ == '__main__':
    main()
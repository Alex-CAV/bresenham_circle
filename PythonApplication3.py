from PIL import Image

def draw_circle(image, center_x, center_y, radius):
    x = radius
    y = 0
    eps = 1 - x
    
    while y <= x:
        image.putpixel((center_x + x, center_y - y), (255, 255, 255))  
        image.putpixel((center_x + y, center_y - x), (255, 255, 255))  
        image.putpixel((center_x - x, center_y - y), (255, 255, 255))  
        image.putpixel((center_x - y, center_y - x), (255, 255, 255))  
        image.putpixel((center_x - x, center_y + y), (255, 255, 255)) 
        image.putpixel((center_x - y, center_y + x), (255, 255, 255))  
        image.putpixel((center_x + x, center_y + y), (255, 255, 255))  
        image.putpixel((center_x + y, center_y + x), (255, 255, 255))  
        y += 1
        if eps <= 0:
            eps += 2 * y + 1
        else:
            x -= 1
            eps += 2 * (y - x) + 1

def main():
    width,height = 1000, 1000
    image = Image.new("RGB", (width, height))

    center_x, center_y = width // 2, height // 2
    radius = 100

    draw_circle(image, center_x, center_y, radius)

    image.show()


main()

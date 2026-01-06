
def calculate_brightness(img):
	if not img or not all( len(row) == len(img[0]) for row in img):
        return -1
    
    num_pixels = 0
    total_brights = 0

    for row in img:
        for pixel in row:
            if pixel < 0 or pixel > 255:
                return -1
            total_brights += pixel
            num_pixels += 1
    
    return total_brights / num_pixels if num_pixels > 0 else -1

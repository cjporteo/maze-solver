def drawpath(img, path, color=(255, 0, 0)):
    pixels = img.load()
    for y, x in path:
        pixels[x, y] = color


def disp(img, dim):
    #  dim = desired display width - source image will scale to this width
    w, h = img.size
    if w > h:
        scale = dim / w
        new_w, new_h = dim, int(h * scale)
    else:
        scale = dim / h
        new_w, new_h = int(w * scale), dim
    new_img = img.resize((new_w, new_h))  # resize according to the dim parameter
    new_img.show()  # display the image

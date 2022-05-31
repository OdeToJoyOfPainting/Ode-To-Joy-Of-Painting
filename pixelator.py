from PIL import Image
import matplotlib.pyplot as plt

def pixelate(image, image_size):
    # image argument = path to the image file
    # image_size argument = size of the small image eg:(8,8)
    # read file
    img=Image.open(image)

    #resize small
    image_small=img.resize(image_size,Image.BILINEAR)

    #resize normal
    res=image_small.resize(img.size, Image.NEAREST)

    #Save output as jpg
    filename=f'OdeToBob_{image_size[0]}x{image_size[1]}.jpeg'
    res.save(filename)
#NFT1.jpeg is just an example filename
pixelate(image='NFT1.jpeg',image_size=(100,100))
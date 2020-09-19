from PIL import Image as Im
import numpy as np
import time
# Must have both images as a PNG file (JPG creates an error where teh pixel values dont change)



# encodes text to binary code
def EncodeText(test_str):
    ordText = []
    for i in range(len(test_str)):
        
        ordText.append(f"{ord(test_str[i]):0>8b}")
    textToBinary = str("".join(ordText))
    print('Text converted to binary',time.time(),'\n\t-', test_str, '||', textToBinary)
    return(textToBinary)



# encodes binary code into host picture
def EncodeInImage(Image1, secretBinary):
    imageOne = Im.open(Image1)
    imageOneRGBpix_val = list(imageOne.getdata())
    imageOneRGBpix_val_flat = [x for sets in imageOneRGBpix_val for x in sets]

    imageOneZise = Im.open(Image1).size
    secretImage = []
    secretBinaryUnraveled = list(secretBinary)

    for i in range(len(imageOneRGBpix_val_flat)):
        if i < len(secretBinaryUnraveled):
            if imageOneRGBpix_val_flat[i] >= 255:
                secretImage.append(int(imageOneRGBpix_val_flat[i]) - int(secretBinaryUnraveled[i]))
            else:
                secretImage.append(int(imageOneRGBpix_val_flat[i]) + int(secretBinaryUnraveled[i]))
        else:
            secretImage.append(imageOneRGBpix_val_flat[i])

    secretImageRGB = []
    for i in range(int(len(imageOneRGBpix_val_flat)/3)):
        secretImageRGB.append(tuple(secretImage[(i*3):((i+1)*3)]))


    img = Im.new("RGB", imageOneZise)
    pixels = img.load()

    for i in range(imageOneZise[0]):
        for j in range(imageOneZise[1]):
            pixels[i,j] = secretImageRGB[(imageOneZise[0])*j+i]

    img.save(Image3)



# retrieves text from encoded photo
def RetriveSecretText(original, encoded):
    encodedImage = list(encoded.getdata())
    originalImage = list(original.getdata())

    encodedImage_flat = [x for sets in encodedImage for x in sets]
    originalImage_flat = [x for sets in originalImage for x in sets]

    print('Encoded and Original Image Flattened:\n\t-',encodedImage_flat[0:10], '\n\t-',originalImage_flat[0:10])

    code = []
    for i in range(len(encodedImage_flat)):
        code.append(str((int(encodedImage_flat[i])-int(originalImage_flat[i]))**2))

    textToBinary = (str("".join(code)))

    chrtText = []
    for i in range (int(len(textToBinary)/8)):
        chrtText.append(chr(int(textToBinary[(i*8):((i+1)*8)], 2)))
    textFromBinary = str("".join(chrtText))

    print('|------------------------------------------------------------------------------------------------------------------------------------------------------|')
    print('\t', textFromBinary)  
    print('|------------------------------------------------------------------------------------------------------------------------------------------------------|')



# converts secret photo to binary
def BlackAndWhite(bwImage, hostImage):
    bw = Im.open(bwImage).resize(Im.open(hostImage).size, Im.ANTIALIAS)

    bwImageCon = bw.convert('1')
    bwImageRGBpix_val = list(bwImageCon.getdata())
    for i in range(len(bwImageRGBpix_val)):
        if bwImageRGBpix_val[i] == 255:
            bwImageRGBpix_val[i] = '1'
        else:
            bwImageRGBpix_val[i] = '0'

    textToBinary = str("".join(bwImageRGBpix_val))
    print('Secret Photo Converted (BW) and Resized:',time.time(),'\n\t-',bwImageRGBpix_val[0:10],'||', Im.open(hostImage).size, Im.open(bwImage).size)
    return(textToBinary)



# retrieves image from encoded photo
def RetriveSecretImage(original, encoded):

    imageOne = Im.open(original)
    originalImage = list(imageOne.getdata())
    originalImage_flat = [x for sets in originalImage for x in sets]

    imageEncoded = Im.open(encoded)
    encodedImage = list(imageEncoded.getdata())
    encodedImage_flat = [x for sets in encodedImage for x in sets]

    print('Encoded and Original Image Flattened:\n\t-',encodedImage_flat[0:10], '\n\t-',originalImage_flat[0:10])

    code = []
    for i in range(len(encodedImage_flat)):
        code.append(str((int(encodedImage_flat[i])-int(originalImage_flat[i]))**2))

    for i in range(len(code)):
        if code[i] == '1':
            code[i] = 255
        else:
            code[i] = 0

    print('Extracted Information:',time.time(),'\n\t-',code[0:10])


    imageOneZise = imageOne.size

    img = Im.new("1", imageOneZise)
    pixels = img.load()

    for i in range(imageOneZise[0]):
        for j in range(imageOneZise[1]):
            pixels[i,j] = code[(imageOneZise[0])*j+i]
    img.save(Image4)



# # ORIGINAL PHOTO
Image1 = r'D:\2019_2020\PYTHON_PROJECTS\OriginalImage.png'
# SECRET IMAGE
Image2 = r'D:\2019_2020\PYTHON_PROJECTS\SecretImage.png'
# ENCODED PHOTO
Image3 = r'D:\2019_2020\PYTHON_PROJECTS\MergedImage.png'
# SECRET IMAGE TO BE EXTRACTED
Image4 = r'D:\2019_2020\PYTHON_PROJECTS\RetrievedImage.png'
# ENCODE TEXT INTO PHOTOS
text = 'abcdefghijklmnopqrstuvwxyz1234567890'



# ENCODE TEXT INTO PHOTOS
# EncodeInImage(Image1,EncodeText(list(text)))
# RETRIEVE TEXT FROM ENCODED PHOTOS
# RetriveSecretText(Im.open(Image1), Im.open(Image3))   

# ENCODE IMAGE INTO PHOTO
# EncodeInImage(Image1, BlackAndWhite(Image2, Image1))
# RETRIEVE IMAGE FROM ENCODED PHOTO
# RetriveSecretImage(Image1, Image3)
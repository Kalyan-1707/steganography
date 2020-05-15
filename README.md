# steganography
Implementing Image Steganography technique using python 

**Requirements**
* Python v3.6+
* open cv2
* numpy

**Usage**

Image before steganography

![Input](https://github.com/Kalyan-1707/steganography/blob/master/arch.jpeg)

1. Run the image.py file to embedd text into image.

```
C:\Users\#Lee1707\Desktop\steganography>python3 image.py

Enter message to encrypt :Hey this is kalyan I am alive..

Enter name of image(ex:nature.jpg):arch.jpg

Enter name to save encrypted image(ex:enc_nature):steg_img
```

**Output**
```
######## Message Successfully Encrypted #########
Image:steg_img.png

```

2. Run the dec.py file to get text from image.

```
C:\Users\#Lee1707\Desktop\steganography>python3 dec.py

Enter name of image to decrypt message(ex:enc_nature.png):steg_img.png

```

**Output**
```
#### Message Decrypted Successfully ####
Message : Hey this is kalyan I am alive..
```

Image after steganography

![Input](https://github.com/Kalyan-1707/steganography/blob/master/output.png)

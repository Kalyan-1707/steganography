
import cv2
import numpy as np
import binascii


def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary

def encode(img,bin_msg):
    len_msg=len(bin_msg)
    width=img.shape[0]
    height=img.shape[1]

    count=0

    copy_img = np.zeros((width, height, 3), np.uint8) 

    for i in range(width):
        for j in range(height):
            for k in range(3):
                temp=format(img[i][j][k],'08b')
                if(count<=len_msg-1):
                    #print(count)
                    #print("Image Before:"+str(int(temp,2)))
                    temp=temp[:-1]+bin_msg[count]
                    #print("Image After:"+str(int(temp,2)))
                    count+=1
                copy_img[i][j][k]=int(temp,2)

    return copy_img

def enc(msg,filename,result):
    data_bytes=msg.encode("utf-8")
    bin_msg=str2bin(data_bytes)+'11111110'  
    bin_msg=bin_msg[2:]
    img=cv2.imread(filename,1)
    enc_img=encode(img,bin_msg)
    #print("Enc image"+str(enc_img[0][0][1]))
    #print("Image"+str(img[0][0][1]))
    #print(bin_msg[-8:])
    result=result+'.png'
    cv2.imwrite(result,enc_img)
    print("######## Message Successfully Encrypted #########")
    print("Image:"+str(result))


if __name__ == "__main__":
    msg=str(input("Enter message to encrypt :"))
    filename=str(input("Enter name of image(ex:nature.jpg):"))
    result=str(input("Enter name to save encrypted image(ex:enc_nature):"))
    enc(msg,filename,result)




import cv2
import binascii


def bin2str(binary):
	message = binascii.unhexlify('%x' % (int(binary,2)))
	return message

def decode(img):
    width=img.shape[0]
    height=img.shape[1]
    len_msg=47

    count=0

    bin_msg=''

    for i in range(width):
        for j in range(height):
            for k in range(3):
                temp=format(img[i][j][k],'08b')
                #print("Enc_image:"+str(int(temp,2)))
                bin_msg+=temp[-1]
                if(len(bin_msg)>=8):
                    if(bin_msg[-8:]=='11111110'):
                        return bin_msg
                    

def dec(filename):

    image=cv2.imread(filename,1)
    bin_msg=decode(image)
    #print(bin_msg)      #0001111111110111001110001100011101101101101110
    dec_msg=(bin2str(bin_msg[:-8]).decode("utf-8"))
    print("#### Message Decrypted Successfully ####")
    print("Message : "+str(dec_msg))



if __name__ == "__main__":
    filename=str(input("Enter name of image to decrypt message(ex:enc_nature.png):"))
    while(filename[-4:]!='.png'):
        print("Only png files are decrypted")
        filename=str(input("Enter name of image to decrypt message(ex:enc_nature.png):"))
    dec(filename)    
import binascii
#Function to convert from hexadecimal to decimal
def decimal(s):
    i = int(s, 16)
    return str(i)
#code to open the image file
file = open("C:\Users\Chythanya\Desktop\Image.img", "rb")
#reading image file
image_file = file.read()
#conversion of the image into hex
hex_string = binascii.hexlify(image_file)
#writing the hex string into file
output_file = open("C:\Users\Chythanya\Desktop\output.txt", "wb")
output_file.write(hex_string)
#closing the file
output_file.close()

#boot sector, which is located at the first logical sector of each partition 1 sector = 512 bytes according to step 2
print('1 Number of bytes boot block occupy : 512')
b = decimal(hex_string[24:26] + hex_string[22:24])
print('2 Number of bytes per sector : ' + b) #step 2
c = decimal(hex_string[26:28])
print('3 Number of sectors per cluster : ' + c)
d = decimal(hex_string[30:32] + hex_string[28:30])
print('4 Number of reserved sectors : ' + d)
e = decimal(hex_string[32:34])
print('5 Number of FAT copies : ' + e)
f = decimal(hex_string[36:38] + hex_string[34:36])
print('6 Number of root directory entries : ' + f)
g = decimal(hex_string[46:48] + hex_string[44:46])
print('7 Number of sectors per FAT : ' + g)
#byte offset of FAT = no. of reserved setcors * no. of bytes per sector
h = int(d)*int(b)
print('8 byte offset of the first File Allocation Table: ' + str(h))
#byte offset of secon fat = byte offset of first fat + no. of sectors per fat * no. of bytes per sector
i = int(h) + int(g) * int(b)
print('9 byte offset of the second FAT table: ' + str(i))
#first root directiry byte offset = byte offset of first fat + Number of FAT copies * no. of sectors per fat * no. of bytes per sector
j = int(h) + int(e) * int(g) * int(b)
print('10 byte offset of the first Root Directory entry: ' + str(j))
#byte offset of first data block = byte offset of the first Root Directory entry + byte offset of the first File Allocation Table * 32
k = int(j) + int(f) * 32
print('11 byte offset of the first Data Block : ' + str(k))
#total number of bytes - byte offset of the first Data Block
print('12 Total size of the data region: '+str(len(hex_string)/2 - k))


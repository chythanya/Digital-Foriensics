import PIL
import Image
import binascii

#code to get charecters
def get_chars(f_name, string_color):
    file=open(f_name,'w')
    str = string_color
    message = ""
    while str != "":
        i = chr(int(str[:8], 2))
        message = message + i
        str = str[8:] 
    file.write(message)
    file.close()
    return 0;

myimage='Image1.png' 
im=Image.open(myimage).convert('RGB')
pix=im.load()
r, g, b = im.split()
w=im.size[0]
h=im.size[1]
r_pixel_array = []
g_pixel_array = []
b_pixel_array = []

# Code to get the pixel arrays for red, green and blue
for x in range(h):
    for y in range(w):
        r,g,b = im.getpixel( (y,x) )
        r_pixel_array.append(r)
        g_pixel_array.append(g)
        b_pixel_array.append(b)

# Code to get all least significant bits(lsb) for red, green and blue

lsb_r_array = []
lsb_g_array = []
lsb_b_array = []
# Code to get all least significant bits(lsb) array for red
for p in range(len(r_pixel_array)):
    lsb = r_pixel_array[p]%2
    lsb_r_array.append(lsb)
# Code to get all least significant bits(lsb) array for green
for q in range(len(g_pixel_array)):
    lsb = g_pixel_array[q]%2
    lsb_g_array.append(lsb)
# Code to get all least significant bits(lsb) array for blue
for r in range(len(b_pixel_array)):
    lsb = b_pixel_array[r]%2
    lsb_b_array.append(lsb)    

#code to get bits stream for red in a string
string_r = ''
for y in range(len(lsb_r_array)):
    string_r = string_r + str(lsb_r_array[y])
  
#code to get bits stream for green in a string
string_g = ''
for y in range(len(lsb_g_array)):
    string_g = string_g + str(lsb_g_array[y])

#code to get bits stream for blue in a string
string_b = ''
for y in range(len(lsb_b_array)):
    string_b = string_b + str(lsb_b_array[y])


get_chars('chars_red.txt', string_r)
get_chars('chars_green.txt', string_g)
get_chars('chars_blue.txt', string_b)

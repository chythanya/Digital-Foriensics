import PIL
import Image
myimage='Image1.png' 
im=Image.open(myimage).convert('RGB')
pix=im.load()
r, g, b = im.split()
w=im.size[0]
h=im.size[1]
r_pixel_array = []
g_pixel_array = []
b_pixel_array = []
for x in range(w):
    for y in range(h):
        r,g,b = im.getpixel( (x,y) )
        r_pixel_array.append(r)
        g_pixel_array.append(g)
        b_pixel_array.append(b)

print len(r_pixel_array)
print len(g_pixel_array)
print len(b_pixel_array)


# code to get all least significant bits(lsb)

lsb_r_array = []
lsb_g_array = []
lsb_b_array = []

for p in range(len(r_pixel_array)):
    lsb = r_pixel_array[p]%2
    lsb_r_array.append(lsb)

for q in range(len(g_pixel_array)):
    lsb = g_pixel_array[q]%2
    lsb_g_array.append(lsb)

for r in range(len(b_pixel_array)):
    lsb = b_pixel_array[r]%2
    lsb_b_array.append(lsb)    

print len(lsb_r_array)    
print len(lsb_g_array)
print len(lsb_b_array)

#code to get charecters of red
k=0
char_array_r = []
for t in range(len(lsb_r_array)/8):
    char_bits=''
    for s in range(0,7):    
        char_bits=char_bits+str(lsb_r_array[k])
        k=k+1
    #print '\n' + char_bits 
    char_array_r.append(chr(int(char_bits, 2)))
filename="red.txt"
file=open(filename,'w')
for l in range(0,len(char_array_r)):
    file.write(char_array_r[l])
file.close()

#code to get charecters of red
k=0
char_array_g = []
for t in range(len(lsb_g_array)/8):
    char_bits=''
    for s in range(0,7):    
        char_bits=char_bits+str(lsb_g_array[k])
        k=k+1
    #print '\n' + char_bits 
    char_array_g.append(chr(int(char_bits, 2)))
filename="green.txt"
file=open(filename,'w')
for l in range(0,len(char_array_g)):
    file.write(char_array_g[l])
file.close()

#code to get charecters of red
k=0
char_array_b = []
for t in range(len(lsb_b_array)/8):
    char_bits=''
    for s in range(0,7):    
        char_bits=char_bits+str(lsb_r_array[k])
        k=k+1
    #print '\n' + char_bits 
    char_array_b.append(chr(int(char_bits, 2)))
filename="blue.txt"
file=open(filename,'w')
for l in range(0,len(char_array_b)):
    file.write(char_array_b[l])
file.close()

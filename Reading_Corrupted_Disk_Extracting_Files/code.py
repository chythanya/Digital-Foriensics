import hashlib
import base64
import binascii

def trim_file(deco_string, header, footer):
    initialindex=int(deco_string.find(header))
    finalindex=int(deco_string.find(footer)) 
    tail_length=len(footer)
    trimmed_file=deco_string[initialindex:finalindex+tail_length]
    return trimmed_file;

def md5_checksum(byte_string):
    m = hashlib.md5()
    m.update(byte_string)
    return m.hexdigest();
    
m = hashlib.md5()
for line in open('C:\Users\Chythanya\Desktop\cc.docx', 'rb'):
    m.update(line)
print "Md5 checksum value for the original corrupted file:", m.hexdigest() 

file = open("C:\Users\Chythanya\Desktop\cc.docx", "r")
corupted_file = file.read()
base64_decoded=base64.b64decode(corupted_file)

decoded_string=binascii.b2a_hex(bytearray(base64_decoded))

# -- JPEG file MD5
final_string = trim_file(decoded_string,"ffd8","ffd9")
ascii_string=binascii.unhexlify(final_string)
md5value = md5_checksum(ascii_string)
print "Md5 checksum value for the JPEG file:", md5value 

output_file = open("C:\Users\Chythanya\Desktop\output.jpeg", "wb")
output_file.write(ascii_string)
output_file.close()

# # -- PDF file MD5
final_string = trim_file(decoded_string,"25504446","0a2525454f460a")
ascii_string=binascii.unhexlify(final_string)
md5value = md5_checksum(ascii_string)
print "Md5 checksum value for the PDF file:", md5value 

output_file = open("C:\Users\Chythanya\Desktop\output.pdf", "wb")
output_file.write(ascii_string)
output_file.close()

# # -- GIF file MD5
head_index=int(decoded_string.find("474946383961"))
length=len(decoded_string)

decoded_string=decoded_string[head_index:length]
final_string = trim_file(decoded_string,"474946383961","003b")
ascii_string=binascii.unhexlify(final_string)
md5value = md5_checksum(ascii_string)
print "Md5 checksum value for the GIF file:", md5value 

output_file = open("C:\Users\Chythanya\Desktop\output.gif", "wb")
output_file.write(ascii_string)
output_file.close()

# # -- PNG file MD5
final_string = trim_file(decoded_string,"89504e470d0a1a0","49454e44ae426082")
ascii_string=binascii.unhexlify(final_string)
md5value = md5_checksum(ascii_string)
print "Md5 checksum value for the PNG file:", md5value 

output_file = open("C:\Users\Chythanya\Desktop\output.png", "wb")
output_file.write(ascii_string)
output_file.close()

# # -- DOCX file MD5
final_string = trim_file(decoded_string,"504b0304","504b0506")
ascii_string=binascii.unhexlify(final_string)
md5value = md5_checksum(ascii_string)
print "Md5 checksum value for the XML file:", md5value 

output_file = open("C:\Users\Chythanya\Desktop\output.docx", "wb")
output_file.write(ascii_string)
output_file.close()

file.close()
import hashlib
char_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

randm_pass = []
#first letter
for p in char_array:
    #second letter
    for q in char_array:
        #third letter
        for r in char_array:
            #fourth letter
            for s in char_array:
                #fifth letter
                for t in char_array:
                    string = p+q+r+s+t
                    randm_pass.append(string)
for password_string in randm_pass:
    hex_password_string = hashlib.md5(password_string).hexdigest()
    if hex_password_string == '9aeaed51f2b0f6680c4ed4b07fb1a83c'  :
        print 'File --> Jkirk.zip   Password --> '+ password_string
    elif hex_password_string == '172346606e1d24062e891d537e917a90'  :
        print 'File --> Lmccoy.zip   Password --> '+ password_string
    elif hex_password_string == 'fa5caf54a500bad246188a8769cb9947'  :
        print 'File --> Cchapel.zip   Password --> '+ password_string

# PROBLEM 2 - DECRYPTION

def decrypt_string(encrypted_string):
    str_dict = {'*':'a', '&':'e', '#':'i', '+':'o', '!':'u'}
    decrypted_str = ''
    for i in encrypted_string:
        if i in str_dict:
            decrypted_str += str_dict[i]
        else:
            decrypted_str += i
    return decrypted_str
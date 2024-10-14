def generator(g, x, p):
  return pow(g, x) % p

def decrypt(cipher, key):
  decrypted_text = ""
  for number in cipher:
      decrypted_num = number // (key * 311)
      decrypted_text += chr(decrypted_num)
  return decrypted_text

def dynamic_xor_decrypt(ciphertext, text_key):
  decrypted_text = ""
  key_length = len(text_key)
  for i, char in enumerate(ciphertext):
    key_char = text_key[i % key_length]
    decrypted_char = chr(ord(char) ^ ord(key_char))
    decrypted_text += decrypted_char
  return decrypted_text


p = 97
g = 31

a = 89
b = 27
cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]




u = generator(g, a, p)
v = generator(g, b, p)
shared_key = generator(v, a, p)
ciphertext = decrypt(cipher, shared_key)
print(dynamic_xor_decrypt(ciphertext, "trudeau"))
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:43:37 2022

@author: mthak
"""
First_Name = "Munjal"
Last_Name = "Thakkar"
UID = 117530445

def caesar_str_enc(ptext,key):
    ptext = ptext.upper()
    ptext = ptext.replace(" ","")
    ciphertext=""
    for i in range(len(ptext)):
        m = ord(ptext[i]) - 65 + key
        m = m%26
        ciphertext = ciphertext+chr(m+65)
    return ciphertext
    
def caesar_str_dec(ctext,key):
    ctext = ctext.upper()
    plaintext= ""
    for i in range(len(ctext)):
        m = ord(ctext[i]) - 65 - key
        m=m%26
        plaintext = plaintext + chr(m+65)
    return plaintext

if __name__=="__main__":
  #your test code comes here
  ctext = caesar_str_enc('A TEST SENTENCE', 2)
  print (ctext)
  ptext = caesar_str_dec(ctext, 2)
  print (ptext)
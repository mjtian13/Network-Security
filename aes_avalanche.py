# -*- coding: utf-8 -*-
"""Hw4_AES_Avalanche_Munjal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SICkWVvD3k-iG5vdSMopjOlMLMG1PmL2
"""

#!pip install pycryptodome
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

UID = 117530445
Last_name = "Thakkar"
First_name = "Munjal"
# inputblock and key are 16 byte long bytes values each
# bitlist is a list of integers that define the position of the
# bit in the inputblock that needs to be inverted, one at a time, for example
# [0, 3, 6, 25, 78, 127]

def aes_input_av_test(inputblock, key, bitlist):
    #The block size & key size is constant so setting them to 16.
    block_size = 16
    key_size = 16
    
    diff_list = []
    #Improper key size handling using padding (Handling key sizes other than 16 bytes key).
    if (len(key)<16):
      print ("Key size is too small, so padding has been applied.")
      key = pad(key,key_size)
    elif (len(key)>16):
      key = key[0:16]
      print ("Key size is too large, and we need fixed 16 bytes (128 bit) key, so taking the first 16 bytes.")
      
    #Encryption code
    cipher = AES.new(key, AES.MODE_ECB)
      #Improper input size handling using padding.
    if (len(inputblock)%16==0):
      originalcipher = cipher.encrypt(inputblock)
    else:
      originalcipher = cipher.encrypt(pad(inputblock, block_size))  
    originalcipherinputlist = list(originalcipher)
    
    for b in bitlist:
      inputlist = list(inputblock)
      test = 0
      #Selecting the value to be changed
      if b<8:
        byte_selected = 0
      else:
        byte_selected = b / 8
        byte_selected = math.ceil(byte_selected) - 1
        #Inverting the bit 
        #selecting xor value to change that particular bit
      inversion_value = int(math.pow(2,8-(b%8)-1))
      #print (inversion_value)
        #Inverting that bit.
      try:
        xor = inputlist[byte_selected] ^ inversion_value
        inputlist[byte_selected] = xor
        new_input_block = bytearray(inputlist)
        #print (byte_selected)
        #Encryption code
        cipher = AES.new(key, AES.MODE_ECB)
          #Improper input size handling using padding.
        if (len(inputblock)%16==0):
          newcipher = cipher.encrypt(new_input_block)
        else:
          newcipher = cipher.encrypt(pad(new_input_block, block_size))
        #Comparing the changed bits
        newcipherinputlist = list(newcipher)
        diff_count = 0
        for i in range (0,block_size):
          temp = newcipherinputlist[i] ^ originalcipherinputlist[i]
          diff_count = diff_count + bin(temp).count("1")
        diff_list.append(diff_count)
      except:
        print ("Bit change value '" + str(b) + "' is too high. Use a smaller bit change value or larger input")
        diff_list.append("Bad value")
    # return the list of numbers
    return diff_list


# We also perform similar experiment by keeping the inputblock fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    block_size = 16
    key_size = 16
    diff_list = []

    #Improper key size handling using padding (Handling key sizes other than 16 bytes key).
    if (len(key)<16):
      print ("Key size is too small, so padding has been applied.")
      key = pad(key,key_size)
    elif (len(key)>16):
      key = key[0:16]
      print ("Key size is too large, and we need fixed 16 bytes (128 bit) key, so taking the first 16 bytes.")

    #Encryption code
    cipher = AES.new(key, AES.MODE_ECB)
      #Improper input size handling using padding.
    if (len(inputblock)%16==0):
      originalcipher = cipher.encrypt(inputblock)
    else:
      originalcipher = cipher.encrypt(pad(inputblock, block_size))
    originalcipherinputlist = list(originalcipher)
    
    for b in bitlist:
      keylist = list(key)
      #Selecting the value to be changed
      if b<8:
        byte_selected = 0
      else:
        byte_selected = b / 8
        byte_selected = math.ceil(byte_selected) - 1
      #Inverting the bit 
        #selecting xor value to change that particular bit
      inversion_value = int(math.pow(2,8-(b%8)-1))
        #Inverting that bit.
      xor = keylist[byte_selected] ^ inversion_value
      keylist[byte_selected] = xor
      newkey = bytearray(keylist)
      #Encryption code
      cipher = AES.new(newkey, AES.MODE_ECB)
        #Improper input size handling using padding.
      if (len(inputblock)%16==0):
        newcipher = cipher.encrypt(inputblock)
      else:
        newcipher = cipher.encrypt(pad(inputblock, block_size))
      #Comparing the changed bits
      newcipherinputlist = list(newcipher)
      diff_count = 0
      for i in range (0,block_size):
        temp = newcipherinputlist[i] ^ originalcipherinputlist[i]
        diff_count = diff_count + bin(temp).count("1")
      diff_list.append(diff_count)
    # return the list of numbers
    return diff_list

if __name__=="__main__":
    inputblock = b'isthis16bytes?'
    key = b'veryverylongkey!'
    bitlist = [5, 29, 38]
    avalanche_plaintext= aes_input_av_test(inputblock, key, bitlist)
    print (avalanche_plaintext)
    avalanche_key = aes_key_av_test(inputblock, key, bitlist)
    print(avalanche_key)
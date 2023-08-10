# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:19:17 2022

@author: mthak
"""
import pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

First_Name = "Munjal"
Last_Name = "Thakkar"
UID = 117530445


def aes_input_av_test(inputblock, key, bitlist):
    block_size = 16
    # inputblock and key are 16 byte long bytes values each
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    cipher = AES.new(key, AES.mode_ECB)
    originalcipher = cipher.encrypt(pad(inputblock, block_size))
    print (len(originalcipher))
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption on the new input with one inverted bit at position b
        newcipher = aes_enc(newinput, key)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list


# We also perform similar experiment by keeping the inputblock fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    originalcipher = aes_enc(inputblock, key)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        newkey = invertbit(key, b)
        
        # perform encryption with the new key with one inverted bit at position b
        newcipher = aes_enc(inputblock, newkey)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        numbitdifferences = findbitdiff(originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list

if __name__=="__main__":
    print ("Hello")
    inputblock = b'isthis16bytes?'
    key = b'veryverylongkey!'
    bitlist = [5, 29, 38]
    avalanche_plaintext= aes_input_av_test(inputblock, key, bitlist)
    print (avalanche_plaintext)
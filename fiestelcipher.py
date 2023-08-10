# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:42:44 2022

@author: mthak
"""

#scope is to limit 

import hmac
import hashlib
import random

UID = 117530445
Last_name = "Thakkar"
First_name = "Munjal"

def xor(byteseq1, byteseq2):
  #print(byteseq1)
  #print(byteseq2)
  # Python already provides the ^ operator to do xor on interger values
  # but first we need to break our input byte sequences into byte size integers
  l1 = [b for b in byteseq1]
  l2 = [b for b in byteseq2]
  
  l1attachl2 = zip(l1,l2)
  # zip(l1,l2) is actually a list as [(b'\xaa',b'\xcc), (b'\x33', b'\x55')]

  l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in l1attachl2]

  result = b''.join(l1xorl2)

  return result
    
def gen_keylist(keylenbytes, numkeys, seed):
    # We need to generate numkeys keys each being keylen bytes long
    random.seed(seed)
    keylist = []
    for i in range(numkeys):
      bytelist = [bytes([random.randint(0,255)]) for x in range(keylenbytes)]
      keylist.append(bytelist)
    return keylist


def F(byteseq, k, outputlen):
  # we use the hmac hash (don't worry about the meaning for now)
  h = hmac.new(k, byteseq, hashlib.sha1)
  # return the first outputlen bytes of the hash value
  return h.digest()[:outputlen]


def fiestel_block(LE_in, RE_in, key):
    LE_out = RE_in
    output_func = F(RE_in, key, 8)
    RE_out = xor(LE_in, output_func)    
    return LE_out, RE_out
    
def fiestel_enc(plaintext: str, rounds: int, seed: int):
    if (len(plaintext) % 16) !=0:
        temp = 16 - len(plaintext) % 16
        for i in range(temp):
            plaintext = plaintext + bytes(b'\x20')
            
    numkeys = rounds
    keylist = gen_keylist(8, numkeys, seed)
    LE_in = plaintext[0:8]
    RE_in = plaintext[8:16]
    for i in range(0, rounds):
        key = b''.join(keylist[i])
        LE_in, RE_in = fiestel_block(LE_in, RE_in, key)
            
    ciphertext = RE_in + LE_in
    return ciphertext

def fiestel_dec(ciphertext: str, rounds: int, seed: int):
    numkeys = rounds
    keylist = gen_keylist(8, numkeys, seed)
    LD_in = ciphertext[0:8]
    RD_in = ciphertext[8:16]
    for i in range (rounds-1,-1,-1):
        key = b''.join(keylist[i])
        LD_in, RD_in = fiestel_block(LD_in, RD_in, key)
    plaintext = RD_in + LD_in
    return plaintext

if __name__=="__main__":
    plaintext = b'isthis16bytes?'
    rounds = 16
    seed = 50
    # pt_test = b'isthis16bytes?  '
    # xor_test2 = b'\xaa\xa1\xb2\xc4\x56\x68\x9d\xff'
    ciphertext = fiestel_enc(plaintext, rounds, seed)
    print (ciphertext)
    plaintext = fiestel_dec(ciphertext, rounds, seed)
    print (plaintext)
    
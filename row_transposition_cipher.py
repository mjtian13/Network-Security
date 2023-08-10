# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:11:12 2022

@author: mthak
"""
import numpy

First_Name = "Munjal"
Last_Name = "Thakkar"
UID = 117530445

def row_trans_enc(plaintext, key):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ","")
    keylist = list(key)
    keyint = [int(x) for x in keylist]
    keylength = len(keyint)
# Let's find the padding length
    pad = len(keyint) - (len(plaintext) % keylength)
    if pad != 7:
        plaintext = plaintext + pad*'X'
    #print(plaintext)
# The columns sorting based on the numbers.    
    orderedlist = numpy.argsort(keylist)
    #print (orderedlist)
# Now creating the 2d-list/matrix in a normal manner
    rows = len(plaintext)/keylength
    rows = int(rows)
    #print(rows)
    matrixlist = []
    for row in range (0,rows):
          templist = []
          for col in range (0,len(keyint)):
            templist.append(plaintext[col+(row*keylength)])
          matrixlist.append(templist)
#    print(matrixlist)
# Now adding the ciphertext in the proper format specified in ordered list.
    ciphertext = ""
    for col in orderedlist:
        for row in range(0,rows):
            ciphertext = ciphertext + matrixlist[row][col]
    return ciphertext
    
def row_trans_dec(ciphertext, key):
    keylist = list(key)
    keyint = [int(x) for x in keylist]
    keylength = len(keyint)
    # rows= len(plaintext)/keylength
    # rows = int(rows)
    # cols = len(keyint)
    # mylist = []
    # for rows in range (0,rows):
    #     templist =[]
    #     for cols in range (0,cols):
    #         templist.append(ciphertext[(rows*keylength) + cols])
    #     mylist.append(templist)
    # print(mylist)
    columnlength = len(ciphertext)/keylength
    columnlength = int(columnlength)
    rowlength = len(keyint)
    mylist = []
    counter=0
    for row in range (0,rowlength):
        templist=[]
        for column in range (0,columnlength):
            templist.append(ciphertext[counter])
            counter = counter+1
        mylist.append(templist)
    # print(mylist)
    # print (keyint)
    plaintext=""
    for column in range (0,columnlength):
        for position in keyint:
            plaintext = plaintext + mylist[position-1][column]
    return plaintext
    
    # plaintext =""
    # for char in range (0,len(ciphertext)):
    #     plaintext = plaintext + ciphertext[]
    
if __name__=="__main__":
    #your test code comes here
    key = '7341625'
    plaintext = "CAnyouFINDtHeMiSSINGVAlue"
    ciphertext = row_trans_enc(plaintext, key)
    print(ciphertext)
    decoded_plaintext = row_trans_dec(ciphertext, key)
    print (decoded_plaintext)

    
    
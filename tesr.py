import numpy as np

divisor = "1001"
cipher_matrix = np.array([[-3, -3, -4], [1,1,1], [4,3,4]])

# cipher_matrix_inverse = np.array([[1,0,1], [4,4,3], [-4, -3, -3]])

def xor(a,b):
    res = ""
    for i in range(1, len(b)):
        if(a[i]==b[i]):
            res+="0"
        else:
            res+="1"
    return res

def get_remainder(data, divisor):
    selected_data_len = len(divisor)
    temp_data = data[:selected_data_len]

    while selected_data_len<len(data):
        if temp_data[0]=="0":
            dummy = "0" * selected_data_len
            temp_data = xor(dummy, temp_data) + data[selected_data_len]
        else:
            temp_data = xor(divisor, temp_data)+data[selected_data_len]

        selected_data_len+=1

    if temp_data[0]=='1':
        temp_data = xor(divisor, temp_data)
    else:
        dummy = "0" * selected_data_len
        temp_data = xor(dummy, temp_data)

    return temp_data[:-(selected_data_len-1)]


ascii_a = ord('a')

def convertData(data):
    res = ""
    plaintext_matrix = []
    row = []
    for char in data:
        if char==' ':
            res+= format(27, 'b')
            row.append(27)
        else:
            ascii_val = ord(char)
            new_ascii = ascii_val-ascii_a+1
            row.append(new_ascii)
            res+= format(new_ascii, 'b')

        if len(row)==3:
            plaintext_matrix.append(row)
            row=[]

    size_of_matrix = len(plaintext_matrix)

    if len(row) !=0 :
        while(len(row)%3 != 0):
            row.append(27)
        plaintext_matrix.append(row)

    return res, plaintext_matrix

# def convertData(data):

s="ab cdw"
bin_data, data_matrix = convertData(s)
data_matrix = np.array(data_matrix)
key = "1001"
appended_data = bin_data + '0'*(len(key)-1)
remainder = get_remainder(appended_data, divisor)

encoded_data = np.dot(cipher_matrix, data_matrix.T)
print (bin_data)
print (len(data_matrix))
print (data_matrix)
print (appended_data)
print ("encoded data : ", encoded_data)

encoded_data_str = encoded_data.tostring()
print (encoded_data_str)
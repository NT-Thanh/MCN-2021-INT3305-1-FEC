import os

i = 0
array = bytes("", encoding="utf8")
for filename in os.listdir("split_output"):
    with open("split_output/" + filename, "r", encoding="utf8") as in_file:
        bytesIn = in_file.read()
        if(i == 0):
            array = bytesIn
        else:
            # array = bytes(a ^ b for (a, b) in zip(array, bytesIn))
            array = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(array,bytesIn))
        i += 1

with open("split_output/redundant-out-file", 'w', encoding="utf8") as output:
    output.write(array)  # viet phan data

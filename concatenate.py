import os

def recover():
    i = 0
    array = bytes("", encoding="utf8")
    for filename in os.listdir("split_output"):
        with open("split_output/" + filename, "rb") as in_file:
            bytesIn = in_file.read()
            if(i == 0):
                array = bytesIn
            else:
                array = bytes(a ^ b for (a, b) in zip(array, bytesIn))
            i += 1
    return array


array = bytearray("", encoding="utf8")
blocks = [bytearray("", encoding="utf8")] * len(os.listdir("split_output"))
for filename in os.listdir("split_output"):
    with open("split_output/" + filename, "rb") as in_file:
        bytesIn = in_file.read()
        headerparams = bytesIn[:16].split(bytes('.', encoding="utf8"))
        if(int(headerparams[1]) != 0 and int(headerparams[0]) == 0):
            continue
        elif(-1*int(headerparams[1]) != 0):
            blocks[int(headerparams[0])] = bytearray(bytesIn)
        else:
            blocks[int(headerparams[0])] = bytearray(bytesIn)

i = 0
for block in blocks:
    if(i == len(blocks)):
        continue
    if(len(block) == 0):
        temp = bytearray(recover())
        headerparams = temp[:16].split(bytes('.', encoding="utf8"))
        print(headerparams)
        if(-1*int(headerparams[1]) != 0):
            array += temp[16:-1*int(headerparams[1])]
        else:
            array += temp[16:]
        i += 1
        continue
    headerparams = block[:16].split(bytes('.', encoding="utf8"))
    print(headerparams)
    if(-1*int(headerparams[1]) != 0):
        array += block[16:-1*int(headerparams[1])]
    else:
        array += block[16:]
    i += 1
with open("concatenate_output/concatenate-file", 'wb') as output:
    output.write(array)  # viet phan data


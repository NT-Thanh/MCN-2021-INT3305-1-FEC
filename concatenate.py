import os

array = bytearray("", encoding="utf8")
blocks = [bytearray("", encoding="utf8")] * len(os.listdir("split_output"))
for filename in os.listdir("split_output"):
    with open("split_output/" + filename, "rb") as in_file:
        bytesIn = in_file.read()
        headerparams = bytesIn[:16].split(bytes('.', encoding="utf8"))
        # print(-1*int(headerparams[1]) != 0)
        if(-1*int(headerparams[1]) != 0):
            blocks[int(headerparams[0])] = bytearray(bytesIn)[16:-1*int(headerparams[1])]
            # array += bytearray(bytes, encoding="utf8")[16:-1*int(headerparams[1])]
        # array.append(bytearray(bytes, encoding="utf8"), self=array)
        else:
            blocks[int(headerparams[0])] = bytearray(bytesIn)[16:]
            # array += bytearray(bytes, encoding="utf8")[16:]
for block in blocks:
    array += block
with open("concatenate_output/concatenate-out-file-" + filename, 'wb') as output:
    output.write(array)  # viet phan data

import os

array = bytearray("", encoding="utf8")
blocks = [bytearray("", encoding="utf8")] * len(os.listdir("split_output"))
for filename in os.listdir("split_output"):
    with open("split_output/" + filename, "r", encoding="utf8") as in_file:
        bytes = in_file.read()
        headerparams = bytes[:16].split('.')
        # print(-1*int(headerparams[1]) != 0)
        if(-1*int(headerparams[1]) != 0):
            print(headerparams[1])
            blocks[int(headerparams[0])] = bytearray(bytes, encoding="utf8")[16:-1*int(headerparams[1])]
            # array += bytearray(bytes, encoding="utf8")[16:-1*int(headerparams[1])]
        # array.append(bytearray(bytes, encoding="utf8"), self=array)
        else:
            print(headerparams[1])
            blocks[int(headerparams[0])] = bytearray(bytes, encoding="utf8")[16:]
            # array += bytearray(bytes, encoding="utf8")[16:]
for block in blocks:
    array += block
with open("concatenate_output/concatenate-out-file-" + filename, 'w', encoding="utf8") as output:
    output.write(str(array)[12:-2])  # viet phan data

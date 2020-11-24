import os

array = bytearray("", encoding="utf8")
for filename in os.listdir("split_output"):
    with open("split_output/" + filename, "r", encoding="utf8") as in_file:
        bytes = in_file.read()
        headerparams = bytes[:16].split('.')
        if(-1*headerparams[1] != 0):
            array += bytearray(bytes, encoding="utf8")[16:]
        # array.append(bytearray(bytes, encoding="utf8"), self=array)

with open("concatenate_output/concatenate-out-file-" + filename, 'w', encoding="utf8") as output:
    output.write(str(array)[12:-2])  # viet phan data

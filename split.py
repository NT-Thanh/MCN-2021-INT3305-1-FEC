i = 0
readSize = 1000
with open("sample.txt", "r", encoding="utf8") as in_file:
    bytes = in_file.read(readSize)  # read 5000 bytes
    while bytes:
        number = str(i)

        # tinh toan them phan header cho du 16 bytes stt.sobytedonthem....
        header = number + "." + str(readSize - len(bytes))
        if(len(header) < 16):
            header += "." * (16 - len(header))
        print(header)
        
        with open("split_output/out-file-" + number, 'w', encoding="utf8") as output:
            output.write(header) # viet phan header
            output.write(bytes) # viet phan data
            output.write("." * (readSize - len(bytes))) # viet phan don them cho du readSize bytes
        bytes = in_file.read(readSize)
        i += 1

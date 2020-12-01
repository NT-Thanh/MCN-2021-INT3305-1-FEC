i = 0
readSize = 300
with open("sample.png", "rb") as in_file:
    bytesIn = in_file.read(readSize)  # read 5000 bytes
    while bytesIn:
        number = str(i)

        # tinh toan them phan header cho du 16 bytes stt.sobytedonthem....
        header = number + "." + str(readSize - len(bytesIn))
        if(len(header) < 16):
            header += "." * (16 - len(header))
        print(header)
        
        with open("split_output/out-file-" + number, 'wb') as output:
            output.write(bytes(header, encoding="utf8")) # viet phan header
            output.write(bytesIn) # viet phan data
            output.write(bytes("." * (readSize - len(bytesIn)), encoding="utf8")) # viet phan don them cho du readSize bytes
        bytesIn = in_file.read(readSize)
        i += 1

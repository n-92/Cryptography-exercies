stringFormattedHex = "00:c0:7e:1f:2c:cc:16:c0:bf:30:d3:40:a5:f0:88:a3:d3:c2:2b:13:72:37:85:f8:24:06:f4:37:ec:15:18:eb:e0:02:a1:c5:4d:2b:54:28:4f:ac:75:1a:04:0a:13:93:78:01:f4:75:56:87:40:4f:11:f1:64:01:5f:58:31:94:29"
stringRawHex = "0x"+"".join(stringFormattedHex.split(":"))
print(int(stringRawHex,0))

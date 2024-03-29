# Helen Li
# February 11, 2015
# Assignment #2: Problem #3: Data Size Converter

# prompt user for file size
size = int(input("Enter a file size, in kilobytes (KB): "))
print ()
print (size, "KB ...")
print ()

# convert KB to bits, bytes, MB, GB
bits = size*1024*8
byte = size*1024
megabytes = float(size/1024)
gigabytes = float((size/1024)/1024)

# print conversions with alignment
print (format("... in bits", "<25s"), format(bits, ">20,.2f"), format("bits", "<10s"))
print (format("... in bytes", "<25s"), format(byte, ">20,.2f"), format("bytes", "<10s"))
print (format("... in megabytes", "<25s"), format(megabytes, ">20,.2f"), format("MB", "<10s"))
print (format("... in gigabytes", "<25s"), format(gigabytes, ">20,.2f"), format("GB", "<10s"))

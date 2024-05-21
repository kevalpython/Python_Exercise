string = "PQRQRQRQ"
substring = "QRQ"
len1 = len(string)
len2 = len(substring)
j = 0
count = 0
while(j < len1):
    if(string[j] == substring[0]):
        if(string[j:j+len2] == substring):
            count += 1
    j += 1
print(count)
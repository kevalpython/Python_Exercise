string = "PQRQRQRQ"
substring = "PQR"
string_len = len(string)
substring_len = len(substring)
j = 0
count = 0
while(j < string_len):
    if(string[j] == substring[0]):
        if(string[j:j+substring_len] == substring):
            count += 1
    j += 1
print(count)
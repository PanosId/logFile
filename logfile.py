
infile = r"C:\Users\paioa\Desktop\testlog.log"

logs = []
key_word = ["real time"]

with open(infile) as f:
    f = f.readlines()

for line in f:
    for word in key_word:
        if word in line:
            logs.append(line)
            break
       
print(logs[-1])

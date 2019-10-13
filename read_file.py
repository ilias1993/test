fp = open("friends.txt", "r")

print(fp.readable())
#print(fp.read())
#print(fp.readline())
#print(fp.readline())
#print(fp.readlines())
#print(fp.readlines()[2])

# for line in fp:
#     print(line)

# for line in fp.readlines():
#     print(line)

for line in fp.readlines()[2]:
    print(line)

fp.close()
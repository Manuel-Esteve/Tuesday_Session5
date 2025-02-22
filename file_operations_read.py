fp = open("text.txt") # this is open from reading
print(fp.read()) # read() method gets entire file content
fp.close() # this is good practice

# same thing as using context manager!
# this is more pythonic!
with open("text.txt", "r") as  f:
    print(f.read())
# no need to close

# read the file line by line
print("Now we read it line by line")
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        print(line)
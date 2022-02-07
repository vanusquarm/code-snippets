
with open("index.js","r") as f:
    lines = f.read()


with open("classes.txt","w") as f:
    count = 0
    start_count = 0
    end_count = 0
    
    for x in lines:
        if (x == "=" and lines[(count+1)] == '"'):
            start_count = count
            print(f"= at {start_count}")
        if (x == ">" and lines[(count-1)] == '"'):
            end_count = count
            print(f"> at {end_count}")

        if (end_count > start_count):    
            f.writelines(lines[start_count+2: end_count-1])
            f.write("\n")

        count += 1    
    print(count)   

with open("classes.txt","r") as f:
    mylist = f.readlines()
    mylist = list(dict.fromkeys(mylist))
    
with open("classes.txt","w") as f:
    f.writelines(mylist)
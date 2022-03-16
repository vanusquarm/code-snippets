
#Read and write classes from react javascript file

with open("index.js","r") as f:
    lines = f.read()


with open("classes.txt","w") as f:
    ''' count the characters in each class
        use the startpoint and endpoint to write to a new file
    '''
    count = 0
    start_count = 0
    end_count = 0

    for x in lines:
        if (x == "=" and lines[(count+1)] == '"'):
            start_count = count
            # print(f"= at {start_count}")
        if (x == ">" and lines[(count-1)] == '"'):
            end_count = count
            # print(f"> at {end_count}")

        if (end_count > start_count):    
            f.writelines(lines[start_count+2: end_count-1])
            f.write("\n")

        count += 1    
    # print(count)
    f.close()      

# Seperate joined classes and write them to new lines

with open("classes.txt","r") as f:
    mylist = f.read()
    
with open("classes.txt","w") as f:
    for x in mylist:
        f.write(x)
        if(x == " "):
            f.write("\n")
    f.close()

# Remove extra spaces in the file

with open("classes.txt","r") as f:
    mylist = f.readlines() # read lines in the file and store in a list
    mylist2 = []        
    for x in mylist: # for each line in the file 
        for y in x: # get all strings in the line
            mylist2.append(y.replace(" ","")) # remove every space in the string and store the results in a new list
    # print(mylist2) # result is list of characters without space

with open("classes.txt","w") as f:
    f.writelines(mylist2)
    f.close()    

# Remove duplicate classes in the file

with open("classes.txt","r") as f:
    mylist = f.readlines()
    mylist = list(dict.fromkeys(mylist))
    print(mylist)
    
with open("classes.txt","w") as f:
    f.writelines(mylist)
    f.close()

# remove newlines
with open("classes.txt","r") as f:
    mylist = f.readlines()
    mylist.remove("\n")
    print(mylist)
    
with open("classes.txt","w") as f:
    f.writelines(mylist)
    f.close()

# Search for the implementation of the classes in a min.js file and write them into a new file.
# with open("classes.txt","r") as f:
#     mylist = f.read()
#     txt  = mylist.split("}")
#     txt = [x+"}" for x in txt]
#     txt2 =[]
	
#     for i,_ in enumerate(txt):    
#         result = txt[i].find(".text")
#         print(result)
#         if(result > 0): 
#             txt2.append(txt[i])


# with open("classes.txt","w") as f:
#     f.writelines(txt2)
#     f.close()


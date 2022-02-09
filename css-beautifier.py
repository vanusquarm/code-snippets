codelist = []
#material-dashboard.min.css
with open("material-dashboard.css","r") as f:
    codelist = f.read()

with open("codelist.css","w") as f:
    for x in codelist:
        if x != "}": # it means do not write '}'
            f.write(x)
            if x == ";" or x == "{":
                f.write("\n \t")
        if x == "}":
            f.write("\n } \n ")

# with open("codelist.css","w") as f:
#     for x in codelist:
#         f.write(x)
#         if x == ";":
#             f.write("\n")
#         if x == "}":
#             f.write("\n ")

# with open("codelist.css","w") as f:
#     for x in codelist:
#         if x != "}": # it means do not write '}'
#             f.write(x)
#             if x == ";":
#                 f.write("\n \t")
#             if x == "{":
#                 f.write("\n \t \t")
#         if x == "}":
#             f.write("\n } \n ")

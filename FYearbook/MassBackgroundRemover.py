import os
#parses through a file and removes the background
def HEICtoJPG(filename):
    if filename.endswith(".HEIC"):
        jpgVer = filename.split(".HEIC")[0] + ".jpg"
        #print(jpgVer)
    elif filename.endswith(".heic"):
        jpgVer = filename.split(".heic")[0] + ".jpg"
        #print(jpgVer)
    commd = "magick " + filename + " " + jpgVer
    #print(commd)
    os.system(commd)

arr = os.listdir()
for entry in arr:
    if entry.endswith("HEIC") or entry.endswith("heic"):
        HEICtoJPG(entry)
    if entry.endswith("png"):
        jpgVer = entry.split(".png")[0] + ".jpg"
        commd = "magick " + entry + " " + jpgVer
        os.system(commd)
    if entry.endswith("JPEG"):
        print("hi")
        jpgVer = entry.split(".JPEG")[0] + ".jpg"
        commd = "magick " + entry + " " + jpgVer
        print(commd)
        os.system(commd)
    cmd = "rm "+ entry

arr = os.listdir()
for entry in arr:
    if entry.endswith("jpg") or entry.endswith("JPG"):
        commad = "backgroundremover -i "+ entry + " -m u2net -a -ae 15 -o " + entry.split(".")[0] + "1.png"
        os.system(commad)
        commad = "backgroundremover -i "+ entry + " -m u2netp -a -ae 15 -o " + entry.split(".")[0] + "2.png"
        os.system(commad)
        commad = "backgroundremover -i "+ entry + " -m u2net_human_seg -a -ae 15 -o " + entry.split(".")[0] + "3.png"
        os.system(commad)
        os.system("rm %s" %entry)



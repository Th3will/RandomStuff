import os

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
         jpgVer = entry.split(".JPEG")[0] + ".jpg"
        commd = "magick " + entry + " " + jpgVer
        os.system(commd)
    cmd = "rm "+ entry

arr = os.listdir()
for entry in arr:
    if entry.endswith("png") or entry.endswith("jpg") or entry.endswith("JPEG") or entry.endswith("JPG"):
        commad = "backgroundremover -i " + entry +" -o " + entry.split(".")[0] + ".png"
        os.system(commad)
        os.system("rm %s" %entry)



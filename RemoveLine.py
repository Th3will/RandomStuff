import re

lines = open("text.txt", encoding="utf8").readlines()

spaced = []
for line in lines:
    spaced.append(line.split(" "))


spaced = list(filter(lambda i: '\n' not in i, spaced))

print(spaced)

cleaned_lines = []
for phrase in spaced:
    for i in phrase:
        if i.isdigit():
            if "\n" in i:
                cleaned_lines.append(i.replace("\n", ""))
                cleaned_lines.append("\n")
            else:
                cleaned_lines.append(i)
        else:
            cleaned_lines.append("\n")

for i in range(len(cleaned_lines)-1):
    if not (cleaned_lines[i+1] == "\n" or cleaned_lines[i] == "\n"):
        cleaned_lines.insert(i,cleaned_lines.pop(i) + " ")

print(cleaned_lines)
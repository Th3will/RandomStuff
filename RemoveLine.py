lines = open("yeet.txt").readlines()
spaced = []
for line in lines:
    spaced.append(line.split(" "))
nums = ['0','1','2','3','4','5','6','7','8','9']
cleaned_lines = []
def check_for_nums(phrase):
    for i in nums:
        if i in phrase:
            return False
    else:
        return True
for phrase in spaced:
    for i in phrase:
        if check_for_nums(i):
            if "\n" in i:
                cleaned_lines.append(i.replace("\n", ""))
                cleaned_lines.append("\n")
            else:
                cleaned_lines.append(i)
        else:
            cleaned_lines.append("\n")
for i in range(len(cleaned_lines)-2):
    if not (cleaned_lines[i+1] == "\n" or cleaned_lines[i] == "\n"):
        cleaned_lines.insert(i,cleaned_lines.pop(i) + " ")
Formatted = ""
for i in cleaned_lines:
    Formatted += i
print(Formatted)

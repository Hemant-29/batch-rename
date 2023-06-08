import os

filename_first = input("First file name: ")
filename_last = input("Last file name: ")
decreasing = input("Want to rename in decreasing order? : ")

if decreasing != None:
    if decreasing.lower() in ["yes", "y"]:
        changed_first = input("enter ending number: ")
    else:
        changed_first = input("enter starting number: ")
else:
    changed_first = input("enter starting number: ")

textfile = open("_cmd.cmd", 'w')
textfile.write("")
textfile.close()
numlength = 0


def get_extension(filename):
    extension = ""
    for n, i in enumerate(filename):
        if i == ".":
            extension = filename[n:]
    return extension


def extract_string(filename, number=""):
    string = ""
    for i in filename:
        if i != ".":
            if not i.isnumeric():
                string += i
            else:
                string += f"{number}"
                break
        else:
            break
    return string


def extract_num(filename):
    global numlength
    filenumber = ""
    for i in filename:
        if i.isnumeric():
            filenumber += i
    numlength = len(filenumber)
    return int(filenumber)


def generate_command(filename_first, filename_last):
    global numlength, changed_first
    input_list = []
    output_list = []
    if extract_num(filename_first) > extract_num(filename_last):
        print("wrong input!\nThe second number must be larger")

    for i in range(extract_num(filename_first), extract_num(filename_last)+1):
        input_list.append(str(i).zfill(numlength))

    changed_first = str(changed_first) + get_extension(filename_first)
    changed_last = f"{len(input_list)+extract_num(changed_first)}" + \
        get_extension(filename_first)

    if decreasing in ["no", "NO", "No", "n", "N", None]:
        for i in range(extract_num(changed_first), extract_num(changed_last)+1):
            output_list.append(str(i))
    if decreasing.lower() in ["yes", 'y']:
        for i in range(extract_num(changed_last), extract_num(changed_first)-1, -1):
            output_list.append(str(i))

    for n, i in enumerate(input_list):
        text_file = open("_cmd.cmd", 'a')
        text_file.write("rename"+" " + extract_string(filename_first, i) +
                        get_extension(filename_first) + " " + output_list[n] + get_extension(filename_first)+"\n")
    text_file.close()


generate_command(filename_first, filename_last)

os.system("_cmd.cmd")

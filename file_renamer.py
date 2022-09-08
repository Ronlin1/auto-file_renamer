import os

folder = "C:\\Users\\Ronnie Atuhaire\\Downloads\\Test\\"
# folder = "C:/Users/Ronnie Atuhaire/Downloads/Test"

text_to_remove = "y2mate.com - "
filenames = list()

for count, file in enumerate(os.listdir(folder)):
    # print(count, file)
    if text_to_remove in file:
        # print(file)
        filenames.append(folder + file)
        # pass

for count, file in enumerate(filenames):
    old_name = file
    new_name = file.replace(text_to_remove, "")
    print("Renamed ", count, "files successfully")
    os.rename(old_name, new_name)

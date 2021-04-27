import os

# The task of this script is to rename over 300 files I have on my machine that I downloaded from Youtube
# via Y2Mate . So My goal is to remove "y2mate.com-" that automatically adds while downloading

folder_paths = ["C:/Users/Ronnie Atuhaire/Downloads/", "C:/Users/Ronnie Atuhaire/Downloads/weeks b4/",
                "C:/Users/Ronnie Atuhaire/Downloads/Last week/", "C:/Users/Ronnie Atuhaire/Downloads/Today/",
                "E:/", "E:/New folder/", "E:/New folder (2)/", "E:New folder (3)/", "E:/old/", "E:/Today/",
                "C:/Users/Ronnie Atuhaire/Downloads/week b4/"
                ]

filenames = []
text_to_remove = "y2mate.com - ".strip('')
for folder in folder_paths:
    # print(folder)
    for count, filename in enumerate(os.listdir(folder)):
        # print(count, filename)
        if text_to_remove in filename:
            filenames.append(folder + filename)
print(len(filenames))

for count, new_file in enumerate(filenames):
    # print(count, new_file)
    old_name = new_file
    new_name = new_file.replace(text_to_remove, '')
    print(count, new_name)
    os.rename(old_name, new_name)


# Yeah it worked!! Thanks to Python ---> saved me 300 Min's in just seconds assuming
# If I had to use 1 min per renaming


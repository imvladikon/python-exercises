

data = ["first.c", "first.cpp", "first.cs", "second.c"]
base_filename = "file_00.txt"
writer_switcher = {".c": open("c_" + base_filename, "w"),
          ".cs": open("cs_" + base_filename, "w"),
          ".cpp": open("cpp_" + base_filename, "w")}
for line in data:
    extension = line[line.rindex("."):]
    writer = writer_switcher[extension]
    writer.write(line+"\n")

for k, writer in writer_switcher.items():
    writer.close()






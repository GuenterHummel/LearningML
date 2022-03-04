import sys
import os
import regex

file = open("setjava.bat", "w")
file.write("SET JAVA_HOME=" + sys.argv[1] + "\n")
file.write("SET JAVACMD=" + sys.argv[1] + "\\bin\\java.exe\n")

path = os.environ['PATH']
# print("old path:", path)
# print("sys.argv[1]:",sys.argv[1])

if regex.search(r"(c|C)\:\\Program Files(\(x86\))?\\Java\\openjdk-[0-9]+", path, flags=regex.IGNORECASE):
    path = regex.sub(r'(c|C)\:\\Program Files(\(x86\))?\\Java\\openjdk-[0-9]+', sys.argv[1], path, flags=regex.IGNORECASE)
#    path = regex.sub(r'(c|C)\:\\Program Files(\(x86\))?\\Java\\openjdk-[0-9]+', "C:\Program Files\Java\\\graalvm-11", path)
#    path = regex.sub(r'(c|C)\:\\Program Files(\(x86\))?\\Java\\graalvm-[0-9]+', sys.argv[1], path,flags=regex.IGNORECASE)

elif regex.search(r"(c|C)\:\\Program Files(\(x86\))?\\Java\\graalvm-[0-9]+", path, flags=regex.IGNORECASE):
    path = regex.sub(r'(c|C)\:\\Program Files(\(x86\))?\\Java\\graalvm-[0-9]+', sys.argv[1], path, flags=regex.IGNORECASE)
else:
    print("VM type to be switched from could not be found")

# print("new path:", path)

file.write("SET PATH=" + path + "\n")
file.close()


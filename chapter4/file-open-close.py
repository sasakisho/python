# a_file = open("mt7_7.txt",encoding="sjis")
#
# s=a_file.read()
#
# a_file.close()
#
# print(s)

a_file = open("mt7_7.txt",mode="w",encoding="sjis")

a_file.write("おはよう\n")
a_file.write("good morning\n")
a_file.write("おやすみ\ngood night")

a_file.close()

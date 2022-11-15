import string


# mskkanangka = int(input())
# print("Hasil :")
# for i in range(mskkanangka+1):
#     string =''
#     if i % 3 == 0:
#         string += "Fizz"
#     elif i % 5 == 0:
#         string ="Buzz"
#     elif i % 3 == 0 and i % 5 == 0:
#         string += str (i)
#     print (string)

mskkanangka = int(input())
print ('Hasil : ')
for i in range(1, mskkanangka+1):

  string = ""
  if i % 3 == 0:
    string += "Fizz"
  if i % 5 == 0:
    string += "Buzz"
  if i % 5 != 0 and i % 3 != 0:
    string += str(i)
  print (string)
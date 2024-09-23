# task 16
str1= "Максим"
try:
    str1[0]="Б"
except TypeError as k:
    print(f"{k}")
    
str2= "Орос"
comb= str1+str2
print(comb)

mult= str2 * 10
print(mult)

new=str1[:3] + "№" + str1[3:]
print(new)
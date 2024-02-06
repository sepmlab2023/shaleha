string = "Hello My Dear Friends"
print("Enter \n1.To display characters present in the string\n 2.To reverse the string \n 3.To display string in upper case \n 4.To display string in swap case \n 5.To count  no of vowels in the string") 
a = int (input("Enter your choice"))
if(a==1):
     I=[]
     for i in string:
        I.append(i)
     print(I)
elif(a==2):
      s=string.split()[::-1]
      I=[]
      for i in s:
            I.append(i)
      print("".join(I))
elif(a==3):
      print(string.upper())
elif(a==4):
      print(string.swapcase())
elif(a==5):
      vowels = "aeiouAEIOU"
      count = sum(string.count(vowel) for vowel in vowels)
      print(count)
else:
      print("Invalid choice")

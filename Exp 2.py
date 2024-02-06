print ("Enter\n 1.To put even and odd elements into two different lists. \n 2. Merge and sort two lists in 3. Update list and delete middle element \n 4. Find Max and Min element in 5. To check given word is present in the list ")
a=int(input("Enter your choice"))
if(a==1):
     mix = [2, 5, 13, 17, 51, 62, 73, 84, 95]
     ev_li = [ele for ele in mix if ele% 2 == 0 ]
     od_li = [ele for ele in mix if ele% 2 != 0] 
     print("Elements in the list are:",mix)
     print("Even lists:", ev_li)
     print("Odd lists:", od_li)
elif(a==2):
     test_list1=[1, 5, 6, 9, 11]
     test_list2 [3, 4, 7, 8, 10]
     print ("The original list 1 is: " + str(test_list1)) 
     print ("The original list 2 is: " + str(test_list2))
     res=sorted(test_list1 + test_list2)
     print ("The combined sorted list is: "+str(res))
elif(a==3):
     list1=[1, 9, 8, 4, 9.2, 9]
     print ("original list: "+ str(list1))
     remove=9
     if remove in list1:
      list1.pop(list1.index(remove))
     print ("List after element removal is"+str(list1))
elif(a==4):
     list1= [8, 1, 7, 10, 5]
     min_ele, max_ele=list1[0], list1[0]
     for i in range(1, len(list1)):
           if list1[i] < min_ele:
                   min_ele=list1[1]
           if list1[i] > max_ele:
                   max_ele = list1[i]
     print('Minimum Element in the list', list1, 'is', min_ele)
     print('Masimum Element in the list', list1, 'is', max_ele)
elif(a==5):
     test_string = "There are 2 apples for 4 persons"
     test_list = ['apples','oranges']
     print("The original string:"+test_string) 
     print("The original list: "+str(test_list))
     res=[ele for ele in test_list if(ele in test_string)]
     print("Does string contain any list element:" + str(bool(res)))
else:
     print("Invalid choice")

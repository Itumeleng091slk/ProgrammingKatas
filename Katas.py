def combine():
      list1 = []
      list2 = []
      

      list_1 = input("enter your first set of numbers: ") .split(" ")
      list1 = list_1

      list_2 = input("enter your second set of numbers: ").split(" ")
      list2 = list_2
      

      n = len(list1)
      store_list = []
      for i in range(n):
          store_list.append(list1[i])
          store_list.append(list2[i])
      print(store_list)
      
combine()

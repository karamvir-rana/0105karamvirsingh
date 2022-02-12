list = []
num = int(input("Enter range: "))
for i in range(0, num):
    ele = int(input("Enter Element: "))
    list.append(ele)
    
print(list)

for x in list:
    if x == int(x):
          print("List contains numeric elements only")
          break
    else:
          print("List contains another elements as well")
          break
    
                    
    

    

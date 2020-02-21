n1 = int(input('請輸入數字：'))
print("")
input_list = []
for i in range(n1):
    number1 = int(input("first number"))
    number2 = int(input("second number"))
    input_list.append([number1,number2])
    print("")
for i in input_list:
    for j in  range(i[1]):
        for k in range(1,i[0]+1):
            print(str(k)*k)
        for k in range(i[0]-1,0,-1):
            print(str(k)*k)
        print("")

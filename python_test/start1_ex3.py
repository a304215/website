output_list = []

while(True):
    input_str = input("please input")
    if(input_str=="0:00"):
        break
    split_list = input_str.split(":")
    single_h = float(360/12)*int(split_list[0])
    single_m = 360/60*int(split_list[1])
    n1 = abs(single_h-single_m)
    n2 = 360-single_h+single_m
    if(n1>n2):
        print(n2)
    else:
        print(n1)

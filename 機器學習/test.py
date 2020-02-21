array_test = []
def input_data(n,array1):
    input_name = input()
    input_score = int(input())
    input_number = int(input())
    input_s = input_score*input_number
    array1.append([input_name,input_score,input_number,input_s])
def check(name, array1):
    for i in array1:
        if(i[0]==name):
            
            return i
        
    return("不存在")
def main():
    input_n = int(input())
    input_data(input_n,array_test)
    n = input()
    print(check(n,array_test))
main(-)
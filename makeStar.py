print("예제 1 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.")
N = (int)(input("N의 값 : "))
print()
for i in range(0,N):
    print("*" * (i+1))

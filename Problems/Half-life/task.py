N,R=int(input()),int(input())
num_of_days=0
while(N>R):
    num_of_days+=12
    N//=2
print(num_of_days)

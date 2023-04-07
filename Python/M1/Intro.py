a = 5
print("The value is given is", isinstance(a, int))


n=int(input()) # Taking User Input
k=2 # Looping variable starting from 2
While k<=n:# Loop will check all numbers till n
    d=2 # The inner loop also checks all numbers starting from 2
    isPrime = False
    While d<k:
        if(k%d==0):
            isPrime = True
        d=d+1
    if(not(isPrime)):
        print(k)
    k=k+1

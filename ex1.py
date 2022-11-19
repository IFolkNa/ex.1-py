h = int(input("height: "))
print(" ")
for i in range(h):
    print(" " * (h - i), "*" * (2*i + 1))
for i in range(h - 2, -1, -1):
    print(" " * (h - i), "*" * (2*i + 1))
    
limit = int(input(" limit of function: "))
def function(i):
    if i == 0:
        return 0
    else :
        return 1 / i + function(i - 1)
for n in range(limit):
    print("Limit = {}, Value = {:.2f}".format(n+1,function(n+1)))

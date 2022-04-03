print("""
Written in Python 3.9.6
List of prime numbers to test with:
825733
354829
912559
970583
113731
85147
920377
46187
422479
469397
"""
)
import math

def returnE(w):
    # we do not want cases of e = d, that's why w-2 instead of w-1
    for i in range(w-2,3,-1):
        if math.gcd(w,i) == 1:
            return i
        else:
            continue
        return "Number too small"


p = int(input("Enter at least a two digit prime number P: "))
q = int(input("Enter at least a two digit prime number Q: "))
n = p*q
w = (p-1) * (q-1)
e = returnE(w)
d = pow(e,-1,w)

print("Public  Keys (n,e): ({:d}, {:d})".format(n,e))
print("Private Keys (n,d): ({:d}, {:d})".format(n,d))

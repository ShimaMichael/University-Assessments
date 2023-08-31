import random

def gcd(x, y): #calculates gcd
    if y == 0:
        return x
    return gcd(y, x%y)

def is_prime():  
    random_number = random.randrange(10, 100) #generates random between 10-100
    for i in range (2, random_number):
        if random_number % i == 0:
            return is_prime() #checks if it is a prime and if not calls function again
        return random_number
    
p = is_prime()
q = is_prime()
n = p*q
phi = (p-1)*(q-1)

public_key = [] #create empty list for public and private keys
private_key = []

for i in range (2, phi): #checks for co-primes between phi and n
    if gcd(i, phi) == 1 and gcd(i, n) ==1:
        public_key.append(i)
    if len(public_key) == 100:
        break

e = random.choice(public_key) #makes a random choice of public key
del(public_key)

i = 2
while len(private_key) < 5:
    if i*e % phi == 1:
        private_key.append(i)
    i+=1

D = random.choice(private_key)
del(private_key)

print("public key:",(e, n),"\nprivate key:",(D, n))

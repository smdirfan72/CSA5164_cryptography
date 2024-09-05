from sympy import mod_inverse

# Function to factorize n into p and q
def find_p_q(n):
    # Trial division to find factors of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None, None

# Given public key components
e = 31
n = 3599

# Step 1: Find p and q
p, q = find_p_q(n)
if p is None or q is None:
    raise ValueError("Failed to factorize n into p and q.")

print(f"Found factors: p = {p}, q = {q}")

# Step 2: Compute Euler's totient function φ(n)
phi_n = (p - 1) * (q - 1)
print(f"Euler's totient function φ(n) = {phi_n}")

# Step 3: Find the private key d using the modular inverse
d = mod_inverse(e, phi_n)
if d is None:
    raise ValueError("Failed to compute the modular inverse.")

print(f"Private key d = {d}")

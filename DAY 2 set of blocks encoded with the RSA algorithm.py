from math import gcd
from sympy import mod_inverse

def find_factors(n, common_factor):
    """
    Given a number n and a common factor, return the factors of n.
    """
    if common_factor <= 1 or n % common_factor != 0:
        raise ValueError("Invalid common factor.")
    other_factor = n // common_factor
    return common_factor, other_factor

def rsa_private_key(n, e, common_factor):
    """
    Compute the private key for RSA given n, e, and a common factor of a plaintext block.
    """
    # Find p and q from the common factor
    p, q = find_factors(n, common_factor)
    print(f"Factors of n: p = {p}, q = {q}")

    # Compute Euler's totient function φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"Euler's totient function φ(n) = {phi_n}")

    # Compute the private key d using the modular inverse of e modulo φ(n)
    d = mod_inverse(e, phi_n)
    if d is None:
        raise ValueError("Failed to compute the modular inverse.")
    
    return d

# Example usage
n = 3233  # Example modulus, should be set to the actual n value
e = 17    # Example public exponent, should be set to the actual e value
common_factor = 29  # Known common factor of a plaintext block with n

# Compute private key
private_key = rsa_private_key(n, e, common_factor)
print(f"Private key d = {private_key}")

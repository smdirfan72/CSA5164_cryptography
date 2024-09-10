import random

def mod_exp(base, exp, mod):
    """ Perform modular exponentiation. """
    return pow(base, exp, mod)

def diffie_hellman(p, g, secret_a, secret_b):
    """ Perform Diffie-Hellman key exchange. """
    # Alice's side
    A = mod_exp(g, secret_a, p)
    
    # Bob's side
    B = mod_exp(g, secret_b, p)
    
    # Alice computes the shared key
    shared_key_a = mod_exp(B, secret_a, p)
    
    # Bob computes the shared key
    shared_key_b = mod_exp(A, secret_b, p)
    
    return A, B, shared_key_a, shared_key_b

def main():
    # Public parameters
    p = 23  # A prime number
    g = 5   # A base (generator)
    
    # Alice's secret number
    secret_a = random.randint(1, p-1)
    
    # Bob's secret number
    secret_b = random.randint(1, p-1)
    
    # Perform the Diffie-Hellman key exchange
    A, B, shared_key_a, shared_key_b = diffie_hellman(p, g, secret_a, secret_b)
    
    # Output results
    print("Public parameters:")
    print(f"p (prime): {p}")
    print(f"g (base): {g}")
    print("\nAlice's secret number: ", secret_a)
    print("Bob's secret number: ", secret_b)
    print("\nAlice sends: ", A)
    print("Bob sends: ", B)
    print("\nAlice computes shared key: ", shared_key_a)
    print("Bob computes shared key: ", shared_key_b)
    
    # Check if both shared keys match
    if shared_key_a == shared_key_b:
        print("The shared keys match! Key established.")
    else:
        print("The shared keys do not match. Something went wrong.")

if __name__ == "__main__":
    main()

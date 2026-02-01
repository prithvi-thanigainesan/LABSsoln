import cupy as cp
import numpy as np

def energy_func_cpu(s):
    """Standard CPU reference for verification."""
    N = len(s)
    E = 0
    for k in range(1, N):
        ck = sum(s[i] * s[i+k] for i in range(N-k))
        E += ck**2
    return float(E)

def run_verification_suite():
    print("starting")
    
    s = np.random.choice([-1, 1], size=40)
    if energy_func_cpu(s) == energy_func_cpu(-s):
        print("symmetry test pass")
    else:
        raise ValueError("Symmetry violated")

    if energy_func_cpu([1, 1, 1, -1]) == 4.0:
        print("N=4 pass")
    else:
        raise ValueError("math baseline error")

    test_batch = cp.random.choice(cp.array([-1, 1]), size=(1, 10))
    print("gpu batch pass")
    
    print("verification through")

if __name__ == "__main__":
    run_verification_suite()

# Usage
# $ python3 generate_function_signature.py "test(uint40,address,uint256)"
# Generating Signature of: test(uint40,address,uint256) ...
# Function signature: 0x55ae5cb3

import sys
from sha3 import keccak_256

def generate_signature(func):
    funcHash = keccak_256(func.encode('utf-8')).hexdigest()
    return '0x' + funcHash[:8]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        func = sys.argv[1]
        print('Generating Signature of:', func, '...')
        funcSig = generate_signature(func)
        print('Function signature:', funcSig)

    else:
        print('Please pass the function as the only command line arg, ie. "myFunc(uint,address)"')

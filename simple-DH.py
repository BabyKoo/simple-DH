import argparse
import secrets

def calculate_public_key(base, private_key, modulus):
    return pow(base, private_key, modulus)

def calculate_shared_key(opposite_public_key, private_key, modulus):
    return pow(opposite_public_key, private_key, modulus)

def main():
    parser = argparse.ArgumentParser(description='Diffie-Hellman Key Exchange')
    parser.add_argument('-g', '--base', type=int,
                        help='Base g of the cyclic group')
    parser.add_argument('-p', '--modulus', type=int,
                        help='Modulus p of the cyclic group')
    parser.add_argument('-k', '--privatekey', type=int,
                        required=False, help='[Optional]Private key')

    args = parser.parse_args()
    parser.print_help()
    try:
        if args.base:
            base = int(args.base)
        else:
            base = secrets.randbelow(999999)
        if args.modulus:
            modulus = int(args.modulus)
        else:
            modulus = secrets.randbelow(999999)
        if args.privatekey:
            private_key = int(args.privatekey)
        else:
            private_key = secrets.randbelow(modulus)
        public_key = calculate_public_key(
            int(base), private_key, int(modulus))
        print('-- Base g --\n', str(base).zfill(6))
        print('-- Modulus p --\n', str(modulus).zfill(6))
        print('-- Private Key (Keep this) --\n', str(private_key).zfill(6))
        print('-- Public Key --\n', str(public_key).zfill(6))

        op_pub_key = int(input('-- Opposite Public Key --\n:'))
        shared_key = calculate_shared_key(
            op_pub_key, private_key, int(modulus))
        print('-- Shared Key (Keep this) --\n', str(shared_key).zfill(6))
    except ValueError:
        print('Invalid opposite public key entered.')

if __name__ == '__main__':
    main()

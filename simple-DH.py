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

    if args.base and args.modulus:
        try:
            if args.privatekey:
                private_key = int(args.privatekey)
            else:
                private_key = secrets.randbelow(args.modulus)
            public_key = calculate_public_key(
                int(args.base), private_key, int(args.modulus))
            print('-- Private Key --\n', private_key)
            print('-- Public Key --\n', public_key)

            op_pub_key = int(input('-- Opposite Public Key --\n:'))
            shared_key = calculate_shared_key(
                op_pub_key, private_key, int(args.modulus))
            print('-- Shared Key --\n', shared_key)
        except ValueError:
            print('Invalid opposite public key entered.')
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

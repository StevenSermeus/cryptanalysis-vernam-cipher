import argparse


def cli():
    parser = argparse.ArgumentParser(description='Cryptanalysis cli')
    parser.add_argument("--encrypt", "-e",help="Encrypt a message", action="store_true")
    parser.add_argument("--decrypt", "-d",help="Decrypt a message", action="store_true")
    parser.add_argument("--attack","-a", help="Attack a message", action="store_true")
    parser.add_argument("--sanitized", "-s", help="Sanitize the input", action="store_true")
    parser.add_argument("--in", "-i", help="Input file", type=str, required=True, dest="input")
    parser.add_argument("--out", "-o",help="Output file", type=str, required=True)
    parser.add_argument("--key", "-k",help="Key file", type=str)
    parser.add_argument("--most_frequent_letter", "-m",help="Most frequent letter", type=str, default="e")
    parser.add_argument("--ngram_size", "-n",help="Ngram size", type=int, default=3)
    parser.add_argument("--depth", "-dp",help="Depth", type=int, default=100)
    args = parser.parse_args()
    if not args.encrypt and not args.decrypt and not args.attack and not args.sanitized:
        parser.error("Please specify an action")
    if (args.encrypt or args.decrypt) and not args.key:
        parser.error("Please specify a key, when encrypting and decrypting, -k <key>")
    if args.attack and args.key:
        parser.error("Please do not specify a key, when attacking")
    return args

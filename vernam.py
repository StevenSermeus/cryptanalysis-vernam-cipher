from cli import cli
from encrypt import encrypt
from decrypt import decrypt
from encrypt import sanitize
from analyse import attack
if __name__ == "__main__":
    args = cli()
    if args.key:
        sanitized_key = sanitize(args.key)
    if args.encrypt:
        text = open(args.input).read()
        encrypt(text, args.out, sanitized_key)
    if args.decrypt:
        text = open(args.input, "rb").read()
        decrypt(text, args.out, sanitized_key)

    if args.sanitized:
        text = open(args.input).read()
        sanitized_text = sanitize(text)
        with open(args.out, "w") as f:
            f.write(sanitized_text)

    if args.attack:
        attack(args.input, args.out, most_frequent_letter=args.most_frequent_letter, ngram_size=args.ngram_size, depth=args.depth)
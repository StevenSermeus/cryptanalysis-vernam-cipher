from cli import cli
from encrypt import encrypt
from decrypt import decrypt
from encrypt import sanitize
if __name__ == "__main__":
    args = cli()
    if args.encrypt:
        text = open(args.input).read()
        encrypt(text, args.out, args.key)
    if args.decrypt:
        text = open(args.input, "rb").read()
        decrypt(text, args.out, args.key)
    if args.sanitized:
        text = open(args.input).read()
        sanitized_text = sanitize(text)
        with open(args.out, "w") as f:
            f.write(sanitized_text)
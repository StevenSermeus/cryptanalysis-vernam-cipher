# Cryptanalyse Unamur

## Team members

- **Frippiat Gabriel** : etu55347
- **Sermeus Steven**: etu44050

## How to run the project

A script is provided to install the needed package

### Using the script

```bash
chmod +x install.sh
./install.sh
```

or run the following commands

```bash
sudo apt install python3.10-venv

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

## How to use the project

```bash
#Before running the script, you need to activate the virtual environment

source .venv/bin/activate

# Need help ?

python3 vernam.py -h

# Encrypt a file

python3 vernam.py --encrypt --in <input_file> --out <output_file> --key <key_file>
```

```bash
# Decrypt a file

python3 vernam.py --decrypt --in <input_file> --out <output_file> --key <key_file>
```

```bash
# Crack a file
python3 vernam.py --attack --in <input_file> --out <output_file>
```

## Attack

If the value of the key found is not correct, you can try to change the depth (The size of the text read from the file) with the --depth option (Default is 100).

```bash
python3 vernam.py -a -i <input_file> -o <output_file> --depth <depth>
```

Or you can change the size of the n-grams with the -n option (Default is 3) used of the kasiski method.

```bash
python3 vernam.py -a -i <input_file> -o <output_file> -n <n>
```

# Cryptanalyse Unamur

## Team members

- **Frippiat Gabriel**
- **Sermeus Steven**

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
# Encrypt a file

python vernam.py  -e -i <input_file> -o <output_file> -k <key_file>
```

```bash
# Decrypt a file

python vernam.py-d -i <input_file> -o <output_file> -k <key_file>
```

```bash
# Crack a file
python vernam.py -a -i <input_file> -o <output_file>
```

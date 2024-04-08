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
#Before running the script, you need to activate the virtual environment

source .venv/bin/activate

# Encrypt a file

python3 vernam.py  -e -i <input_file> -o <output_file> -k <key_file>
```

```bash
# Decrypt a file

python3 vernam.py -d -i <input_file> -o <output_file> -k <key_file>
```

```bash
# Crack a file
python3 vernam.py -a -i <input_file> -o <output_file>
```

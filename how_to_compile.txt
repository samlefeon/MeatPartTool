MeatPartTool
====

## How to compile

Use Python 3.5

```sh
git clone https://github.com/samlefeon/MeatPartToolTest
cd MeatPartToolTest

# Create a virtual environment in the current directory
python -m venv venv

# Activate the virtual environment

# On Mac/Linux:
source venv/bin/activate
# On Windows:
call venv\scripts\activate.bat

# Install the dependencies
pip install -r requirements.txt

```

## Start the project

```sh
fbs run
```


## Compile an executable

```sh
fbs freeze
```


## Generate an installer

```sh
fbs installer
```

On Windows you might need to install extra libraries https://github.com/mherrmann/fbs-tutorial/blob/master/README.md#windows-installer

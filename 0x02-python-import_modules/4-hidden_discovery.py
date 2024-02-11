#!/usr/bin/python3
import dis

def print_names(filename):
    with open(filename, 'rb') as f:
        code = f.read()

    # Disassemble the bytecode
    instructions = dis.get_instructions(code)

    # Extract names not starting with '__'
    names = {instruction.argval for instruction in instructions
             if instruction.opname == 'LOAD_NAME' and not instruction.argval.startswith('__')}

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_names("hidden_4.pyc")


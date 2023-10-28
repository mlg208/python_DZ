import sys

def parse_command_line_arguments(arguments):
    parsed_args = {}
    i = 1
    while i < len(arguments):
        arg = arguments[i]
        if arg.startswith('--') or arg.startswith('-'):
            key = arg.lstrip('-')
            if i + 1 < len(arguments) and not arguments[i + 1].startswith('--') and not arguments[i + 1].startswith('-'):
                value = arguments[i + 1]
                parsed_args[key] = value
                i += 1
            else:
                parsed_args[key] = None
        i += 1
    return parsed_args

if __name__ == "__main__":
    command_line_arguments = sys.argv
    parsed_args = parse_command_line_arguments(command_line_arguments)
    print(parsed_args)

#python 1.py --text filename.txt --debuglevel warning --mode delayed --output stdout

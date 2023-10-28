import argparse
import json


default_config = {'text': 'filename.txt', 'debuglevel': 'warning', 'mode': 'delayed', 'output': 'stdout'}

def load_config_from_file(file_path):
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {}  
    except json.JSONDecodeError:
        return {}  

def merge_configs(config, file_config, command_line_config):
    config.update(file_config) 
    config.update(command_line_config)  
    return config

def main():
    parser = argparse.ArgumentParser(description='Объединить конфигурации из файла и командной строки')
    parser.add_argument('--text', help='параметры текста')
    parser.add_argument('--debuglevel', help='Debug level parameter')
    parser.add_argument('--mode', help='Mode parameter')
    parser.add_argument('--output', help='Output parameter')

    args = parser.parse_args()

    file_config = load_config_from_file('1.json')

    final_config = merge_configs(default_config, file_config, vars(args))

    print(final_config)

if __name__ == '__main__':
    main()

#задача работает немного неккоректно, почему не работает json файл
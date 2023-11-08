from src.spell_check import spell_check
from src.text_processing import process_text

def get_input():
    file_name = input("Enter file name, please include relative or absolute address if needed:\n")

    return file_name

def get_file_contents(file_name):
    with open(f'{file_name}', 'r') as file: 
       file_content = file.read()

    return file_content

if __name__ == '__main__': 
    file_name = get_input()
    file_content = get_file_contents(file_name)

    processed_file = process_text(file_content, spell_check)

    print(processed_file)

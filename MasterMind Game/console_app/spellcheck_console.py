import sys
from spell_check import spell_check

def main():
    if len(sys.argv) != 2:
        print("Usage: python spellcheck_console.py <file_name>")
        sys.exit(1) #exit if used incorrectly 
    
    file_name = sys.argv[1]
        
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    
    spell_checked_text = spell_check(text)
    
    print("Original text:\n", text, "Spell-checked text:\n", spell_checked_text, sep="")
    
    #spell_checked_text = spell_check(text)
    
   # print(spell_checked_text)
    

    if __name__ == '__main__':
        main()
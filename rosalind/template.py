import os
import argparse
from pathlib import Path



def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("name", type=str)
    args = argparser.parse_args()
    Path(args.name).mkdir(parents=True, exist_ok=True)
    os.system(f'touch {args.name}/{args.name}.txt')
    tpl = f"""\nif __name__ == '__main__':\n\twith open('{args.name}.txt', 'r') as f:\n\t\tinp = f.read()"""
    with open(f'{args.name}/{args.name}.py', 'w') as f:
        f.write(tpl.replace("\t", "    "))
        
main()
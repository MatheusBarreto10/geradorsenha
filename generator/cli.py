import argparse
import sys
from .generator import generate_password

def parse_args():
    p = argparse.ArgumentParser(description="Gerador de senhas seguras")
    p.add_argument("-l", "--length", type=int, default=16)
    p.add_argument("--no-lower", action="store_true")
    p.add_argument("--no-upper", action="store_true")
    p.add_argument("--no-digits", action="store_true")
    p.add_argument("--no-symbols", action="store_true")
    p.add_argument("--no-ambiguous", action="store_true")
    p.add_argument("--no-ensure", action="store_true")
    p.add_argument("--copy", action="store_true")
    return p.parse_args()

def main():
    args = parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            include_lower=not args.no_lower,
            include_upper=not args.no_upper,
            include_digits=not args.no_digits,
            include_symbols=not args.no_symbols,
            exclude_ambiguous=args.no_ambiguous,
            ensure_each_group=not args.no_ensure
        )
    except Exception as e:
        print("Erro:", e)
        sys.exit(1)

    print(pwd)

    if args.copy:
        try:
            import pyperclip
            pyperclip.copy(pwd)
            print("(Senha copiada!)")
        except:
            print("Não foi possível copiar. Instale pyperclip.")

if __name__ == "__main__":
    main()

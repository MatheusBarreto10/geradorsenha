import secrets
import string

AMBIGUOUS = {'l', 'I', '1', 'O', '0'}

def build_charset(include_lower=True, include_upper=True, include_digits=True,
                  include_symbols=True, exclude_ambiguous=False):
    chars = []
    if include_lower:
        chars.append(string.ascii_lowercase)
    if include_upper:
        chars.append(string.ascii_uppercase)
    if include_digits:
        chars.append(string.digits)
    if include_symbols:
        chars.append("!@#$%^&*()-_=+[]{};:,.<>/?")

    charset = ''.join(chars)

    if exclude_ambiguous:
        charset = ''.join(ch for ch in charset if ch not in AMBIGUOUS)

    if not charset:
        raise ValueError("Nenhum grupo de caracteres habilitado.")

    return charset


def generate_password(length=16,
                      include_lower=True,
                      include_upper=True,
                      include_digits=True,
                      include_symbols=True,
                      exclude_ambiguous=False,
                      ensure_each_group=True):

    if length <= 0:
        raise ValueError("O tamanho da senha deve ser > 0")

    charset = build_charset(include_lower, include_upper, include_digits,
                            include_symbols, exclude_ambiguous)

    password_chars = []
    groups = []

    if ensure_each_group:
        if include_lower:
            groups.append(string.ascii_lowercase)
        if include_upper:
            groups.append(string.ascii_uppercase)
        if include_digits:
            groups.append(string.digits)
        if include_symbols:
            groups.append("!@#$%^&*()-_=+[]{};:,.<>/?")

        if exclude_ambiguous:
            groups = [''.join(ch for ch in g if ch not in AMBIGUOUS) for g in groups]

        if len(groups) > length:
            raise ValueError("Tamanho insuficiente para incluir todos os grupos.")

        for g in groups:
            password_chars.append(secrets.choice(g))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(charset))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

import re
from generator.generator import generate_password

def test_length():
    pwd = generate_password(length=20)
    assert len(pwd) == 20

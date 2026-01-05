# -*- coding: utf-8 -*-
# SPDX-License-Identifier: 0BSD

from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from math import floor, log
from secrets import choice

def make_password(
    chars: tuple, length: int, passphrase: bool, separator: str
) -> str:
    if passphrase:
        prefix = choice(digits[2:])
    else:
        prefix = ""
    password = prefix + separator.join(choice(chars) for _ in range(length))
    return password

def contains(items: tuple, sub_items: str) -> bool:
    result = any(_ in items for _ in sub_items)
    return result

def make_complex_password(chars: tuple, length: int) -> str:
    """Make a password containing all char types."""
    while True:
        password = make_password(chars, length, False, "")
        required_chars = 0
        password_chars = 0
        if contains(chars, ascii_uppercase):
            required_chars += 2**0
        if contains(chars, ascii_lowercase):
            required_chars += 2**1
        if contains(chars, digits):
            required_chars += 2**2
        if contains(chars, punctuation):
            required_chars += 2**3

        if contains(password, ascii_uppercase):
            password_chars += 2**0
        if contains(password, ascii_lowercase):
            password_chars += 2**1
        if contains(password, digits):
            password_chars += 2**2
        if contains(password, punctuation):
            password_chars += 2**3

        if required_chars == 0 or password_chars == 0:
            raise ValueError("Invalid chars")
        elif required_chars == password_chars:
            break
    return password

def calculate_entropy(chars: tuple, length: int) -> int:
    """Calculate the entropy in bits.
    https://en.wikipedia.org/wiki/Password_strength#Random_passwords
    """
    count = len(set(chars))
    entropy = floor(length*log(count)/log(2))
    return entropy

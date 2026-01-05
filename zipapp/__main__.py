#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: 0BSD

from get_wordlist import get_wordlist
from argparse import ArgumentParser
from make_password import *

def main() -> None:
    epilog = "https://en.wikipedia.org/wiki/Universally_unique_identifier"
    parser = ArgumentParser(description="make a password",
                            epilog=epilog)
    parser.add_argument("-l", "--lower", action="store_true",
                        help="use lowercase")
    parser.add_argument("-u", "--upper", action="store_true",
                        help="use uppercase")
    parser.add_argument("-d", "--digit", action="store_true",
                        help="use digits")
    parser.add_argument("-p", "--punct", action="store_true",
                        help="use punctuation symbols")
    parser.add_argument("-o", "--custom", type=set,
                        help="specify custom chars")
    parser.add_argument("-w", "--passphrase", action="store_true",
                        help="make a passphrase")
    parser.add_argument("-s", "--separator", type=str, default=".",
                        help="specify the word separator")
    parser.add_argument("-n", "--length", type=int, help="specify the length")
    parser.add_argument("-e", "--entropy", action="store_true",
                        help="calculate the entropy in bits")
    args = parser.parse_args()

    passphrase = args.passphrase
    if passphrase:
        chars = get_wordlist()
    else:
        chars = ""
        if args.upper:
            chars += ascii_uppercase
        if args.lower:
            chars += ascii_lowercase
        if args.digit:
            chars += digits
        if args.punct:
            chars += punctuation
        if args.custom:
            chars += "".join(args.custom)
        if not chars:
            chars += ascii_uppercase + ascii_lowercase + digits + punctuation
        chars = tuple(chars)

    length = args.length or (14 if passphrase else 40)
    if args.entropy:
        print(calculate_entropy(chars, length))
    elif length < 4:
        parser.error("Too short length")
    elif passphrase:
        print(make_password(chars, length, True, args.separator))
    else:
        print(make_complex_password(chars, length))

if __name__ == "__main__":
    main()

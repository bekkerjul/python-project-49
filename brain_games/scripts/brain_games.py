#!/usr/bin/env python3
from ..cly import welcome_user


def welcome_game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def main():
    welcome_game()


if __name__ == '__main__':
    main()

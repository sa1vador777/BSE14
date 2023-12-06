#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def plus() -> int:
    def helper(k: int) -> int:
        return k+3
    return helper


if __name__ == "__main__":
    cnt = plus()
    print(cnt(int(input("Введите любое целое число: "))))

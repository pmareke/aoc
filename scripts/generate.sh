#!/bin/bash
set -e

number_to_word() {
  python3 -c "from num2words import num2words; print(num2words(0o$1))"
}

touch inputs/$1.example
touch inputs/$1.in
day=$(number_to_word $1)
touch tests/test_day_$day.py
touch src/day_$day.py

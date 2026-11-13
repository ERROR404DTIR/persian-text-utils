# persian-text-utils

<p align="center"><img src="assets/readme-banner.svg" alt="Animated Persian Text Utils banner" width="100%"></p>

Lightweight, dependency-free Persian (Farsi) text utilities for Python 3.8+.

## Features

- `normalize()` — convert Arabic ي/ك to Persian ی/ک, unify characters
- `to_persian_digits()` / `to_english_digits()` / `to_arabic_digits()`
- `strip_diacritics()` — remove harakat (فتحه، کسره، ضمه، ...)
- `fix_zwnj()` — fix half-spaces after prefixes/suffixes (می‌روم، کتاب‌ها)
- `remove_tatweel()` — remove kashida (ـ)
- `slugify()` — URL-safe slugs that keep Persian letters
- `clean()` — all-in-one pipeline

## Install

```bash
pip install .
```

## Usage

```python
from persian_text_utils import normalize, to_persian_digits, fix_zwnj, clean

normalize("كتاب يك")          # 'کتاب یک'
to_persian_digits("Order 1234")  # 'Order ۱۲۳۴'
fix_zwnj("می روم")             # 'می‌روم'
fix_zwnj("کتاب ها")            # 'کتاب‌ها'
clean("  كتــاب   ها  ")        # 'کتاب‌ها'
```

## Tests

```bash
python -m unittest discover tests
```

## License

MIT
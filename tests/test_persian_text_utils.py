import unittest

from persian_text_utils import (
    ZWNJ,
    clean,
    fix_zwnj,
    normalize,
    slugify,
    strip_diacritics,
    to_arabic_digits,
    to_english_digits,
    to_persian_digits,
)


class TestPersianTextUtils(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("\u0643\u062a\u0627\u0628 \u064a\u0643"), "\u06a9\u062a\u0627\u0628 \u06cc\u06a9")

    def test_digits(self):
        self.assertEqual(to_persian_digits("1234"), "\u06f1\u06f2\u06f3\u06f4")
        self.assertEqual(to_persian_digits("\u0661\u0662"), "\u06f1\u06f2")
        self.assertEqual(to_english_digits("\u06f1\u06f2\u0663"), "123")
        self.assertEqual(to_arabic_digits("12"), "\u0661\u0662")

    def test_strip_diacritics(self):
        self.assertEqual(strip_diacritics("\u0645\u064f\u062d\u064e\u0645\u0651\u064e\u062f"), "\u0645\u062d\u0645\u062f")

    def test_fix_zwnj(self):
        self.assertEqual(fix_zwnj("\u0645\u06cc \u0631\u0648\u0645"), "\u0645\u06cc" + ZWNJ + "\u0631\u0648\u0645")
        self.assertEqual(fix_zwnj("\u0646\u0645\u06cc \u0631\u0648\u0645"), "\u0646\u0645\u06cc" + ZWNJ + "\u0631\u0648\u0645")
        self.assertEqual(fix_zwnj("\u06a9\u062a\u0627\u0628 \u0647\u0627"), "\u06a9\u062a\u0627\u0628" + ZWNJ + "\u0647\u0627")
        self.assertEqual(fix_zwnj("\u0628\u0632\u0631\u06af \u062a\u0631\u06cc\u0646"), "\u0628\u0632\u0631\u06af" + ZWNJ + "\u062a\u0631\u06cc\u0646")

    def test_clean(self):
        self.assertEqual(
            clean("  \u0643\u062a\u0640\u0640\u0627\u0628   \u0647\u0627  "),
            "\u06a9\u062a\u0627\u0628" + ZWNJ + "\u0647\u0627",
        )

    def test_slugify(self):
        self.assertEqual(slugify("\u0633\u0644\u0627\u0645 \u062f\u0646\u06cc\u0627 \u06f1\u06f2\u06f3"), "\u0633\u0644\u0627\u0645-\u062f\u0646\u06cc\u0627-123")


if __name__ == "__main__":
    unittest.main()

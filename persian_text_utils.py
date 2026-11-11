"""persian_text_utils: small, dependency-free helpers for Persian (Farsi) text."""
import re

__version__ = "1.0.0"

ZWNJ = "\u200c"

_CHAR_MAP = str.maketrans({
    "\u064a": "\u06cc",  # Arabic Yeh -> Persian Yeh
    "\u0649": "\u06cc",  # Alef Maksura -> Persian Yeh
    "\u0643": "\u06a9",  # Arabic Kaf -> Persian Kaf
    "\u0629": "\u0647",  # Teh Marbuta -> Heh
    "\u0623": "\u0627",  # Alef with Hamza above -> Alef
    "\u0625": "\u0627",  # Alef with Hamza below -> Alef
    "\u0671": "\u0627",  # Alef Wasla -> Alef
})

_PERSIAN_DIGITS = "\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9"
_ARABIC_DIGITS = "\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669"
_ENGLISH_DIGITS = "0123456789"

_TO_PERSIAN = str.maketrans(_ENGLISH_DIGITS + _ARABIC_DIGITS, _PERSIAN_DIGITS * 2)
_TO_ARABIC = str.maketrans(_ENGLISH_DIGITS + _PERSIAN_DIGITS, _ARABIC_DIGITS * 2)
_TO_ENGLISH = str.maketrans(_PERSIAN_DIGITS + _ARABIC_DIGITS, _ENGLISH_DIGITS * 2)

_DIACRITICS = re.compile("[\u064b-\u065f\u0670]")
_PREFIX = re.compile("\\b(\u0646?\u0645\u06cc)[ \u00a0]+(?=[\u0600-\u06ff])")
_SUFFIX = re.compile(
    "(?<=[\u0600-\u06ff])[ \u00a0]+(\u0647\u0627\u06cc\u06cc|\u0647\u0627\u06cc|\u0647\u0627|\u062a\u0631\u06cc\u0646|\u062a\u0631)\\b"
)


def normalize(text):
    """Convert Arabic letter variants (ي, ك, ة, ...) to their Persian forms."""
    return text.translate(_CHAR_MAP)


def to_persian_digits(text):
    """Convert English and Arabic-Indic digits to Persian digits."""
    return text.translate(_TO_PERSIAN)


def to_arabic_digits(text):
    """Convert English and Persian digits to Arabic-Indic digits."""
    return text.translate(_TO_ARABIC)


def to_english_digits(text):
    """Convert Persian and Arabic-Indic digits to English digits."""
    return text.translate(_TO_ENGLISH)


def strip_diacritics(text):
    """Remove harakat (fatha, kasra, damma, shadda, sukun, ...)."""
    return _DIACRITICS.sub("", text)


def remove_tatweel(text):
    """Remove kashida / tatweel (ـ)."""
    return text.replace("\u0640", "")


def fix_zwnj(text):
    """Insert half-spaces (ZWNJ) after the می/نمی prefixes and before ها/های/تر/ترین."""
    text = _PREFIX.sub("\\1" + ZWNJ, text)
    text = _SUFFIX.sub(ZWNJ + "\\1", text)
    return text


def collapse_spaces(text):
    """Collapse repeated spaces/tabs and strip the ends."""
    return re.sub(r"[ \t\u00a0]+", " ", text).strip()


def clean(text):
    """Full pipeline: normalize, remove tatweel and diacritics, tidy spaces, fix ZWNJ."""
    text = normalize(text)
    text = remove_tatweel(text)
    text = strip_diacritics(text)
    text = collapse_spaces(text)
    text = re.sub(ZWNJ + "{2,}", ZWNJ, text)
    return fix_zwnj(text)


def slugify(text):
    """Make a URL-safe slug that keeps Persian letters and converts digits to English."""
    text = to_english_digits(clean(text)).replace(ZWNJ, "-")
    text = re.sub(r"[\W_]+", "-", text.lower())
    return text.strip("-")

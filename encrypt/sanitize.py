from unidecode import unidecode
import re
def sanitize(text: str) -> str:
    text_unidecoded = unidecode(text)
    text_sanitized = re.sub(r'[^a-z]', '', text_unidecoded.lower())
    return text_sanitized

def removeDiacritics(text):
    """
    Remove diacritics.
    Only the diacritics are removed, not the whole character.
    The character 'à' becomes 'a'.
    """
    return unidecode(text)

def sanitizeToAlpha(text):
    """
    Sanitize the given string to only lowercase alphabetic characters.

    All characters are converted to lowercase.
    Characters with diacritics are converted to the corresponding
    alphabetic character.
    All remaining non-alphabetic characters are removed.
    """
    return re.sub(r'[^a-z]', '', removeDiacritics(text).lower())

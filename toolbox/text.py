"""Text helpers. The worked example every contribution is modelled on."""


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix

def clamp(value, low, high):
    """Return value limited to the range [low, high].

    >>> clamp(15, 0, 10)
    10
    """
    for name, number in (("value", value), ("low", low), ("high", high)):
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError(f"{name} must be a number")
    if low > high:
        raise ValueError("low must not be greater than high")
    return max(low, min(value, high))

def chunked(items, size):
    """Split items into consecutive lists of at most size elements.

    >>> chunked([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 1:
        raise ValueError("size must be at least 1")
    items = list(items)
    return [items[i:i + size] for i in range(0, len(items), size)]

def flatten(items):
    """Spread out one level of lists and tuples inside items.

    >>> flatten([1, [2, 3], (4,), 5])
    [1, 2, 3, 4, 5]
    """
    if not isinstance(items, (list, tuple)):
        raise TypeError("items must be a list or tuple")
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(item)
        else:
            result.append(item)
    return result

def unique_in_order(items):
    """Return the unique items of a list or tuple, in first-seen order.

    >>> unique_in_order([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    if isinstance(items, str) or not isinstance(items, (list, tuple)):
        raise TypeError("items must be a list or tuple, not a string")
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def safe_divide(numerator, denominator, default=None):
    """Divide numerator by denominator, returning default if it is zero.

    >>> safe_divide(10, 4)
    2.5
    """
    for name, number in (("numerator", numerator), ("denominator", denominator)):
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError(f"{name} must be a number")
    if denominator == 0:
        return default
    return numerator / denominator

def percentage(part, whole, digits=2):
    """Return part as a percentage of whole, rounded to digits places.

    >>> percentage(1, 4)
    25.0
    """
    for name, number in (("part", part), ("whole", whole)):
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError(f"{name} must be a number")
    if isinstance(digits, bool) or not isinstance(digits, int):
        raise TypeError("digits must be an integer")
    if digits < 0:
        raise ValueError("digits must not be negative")
    if whole == 0:
        raise ValueError("whole must not be zero")
    return round(part / whole * 100, digits)

def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Case, spaces and punctuation are ignored.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    letters = [ch.lower() for ch in text if ch.isalnum()]
    return letters == letters[::-1]

def median(numbers):
    """Return the median of a non-empty collection of numbers.

    >>> median([4, 1, 3, 2])
    2.5
    """
    values = list(numbers)
    if not values:
        raise ValueError("numbers must not be empty")
    for number in values:
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError("all values must be numbers")
    values.sort()
    mid = len(values) // 2
    if len(values) % 2:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2

def count_vowels(text):
    """Count the vowels a, e, i, o, u in text, ignoring case.

    >>> count_vowels("Hello World")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return sum(1 for ch in text.lower() if ch in "aeiou")

# puzzle 2
# enhanced version
def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    total = num_one + num_two
    if total < 50:
        return total
    return None

print(sum_if_less_than_fifty(20, 20))


# puzzle 3

def sum_even(input_nums: list[int]) -> int:
    # avoid shadowing the builtin `sum` and use a generator for clarity
    return sum(x for x in input_nums if x % 2 == 0)

print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# puzzle 4

# use a module-level translation table for best performance
_TRANS_REMOVE_VOWELS = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(input_str: str) -> str:
    return input_str.translate(_TRANS_REMOVE_VOWELS)

print(remove_vowels("Hello, World!"))


# puzzle 5

def get_longest_string(input_strs: list[str]) -> str:
    # safe for empty lists
    return max(input_strs, key=len) if input_strs else ""

print(get_longest_string(["cat", "dog", "bird", "lizard"]))


# puzzle 6

def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    return [s for s in input_strs if len(s) % 2 == 0]

print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))


# puzzle 7

def reverse_elements(input_nums: list[int]) -> list[int]:
    return input_nums[::-1]

print(reverse_elements([1, 2, 3, 4, 5]))


# puzzle 8

def filter_type_str(input_list: list[str | int]) -> list[str]:
    return [item for item in input_list if isinstance(item, str)]

print(filter_type_str(["hello", 1, 2, "www"]))


# puzzle 9

MORSE_DICT = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-."
}

def string_to_morse_code(input_str: str) -> str:
    words = input_str.split()
    morse_per_word = []
    for word in words:
        lw = word.lower()
        codes = [MORSE_DICT[ch] for ch in lw if ch in MORSE_DICT]
        morse_per_word.append(" ".join(codes))
    return " / ".join(morse_per_word)

print(string_to_morse_code("HELLO, WORLD!"))


# puzzle 10

def get_second_largest_number(input_nums: list[int]) -> int | None:
    # do not mutate the caller's list and handle duplicates
    uniq = sorted(set(input_nums))
    if len(uniq) < 2:
        return None
    return uniq[-2]

print(get_second_largest_number([14, 2, 3, 44, 5]))


# puzzle 11

def format_number_with_commas(input_num: int) -> str:
    return f"{input_num:,}"

print(format_number_with_commas(1000000))


# puzzle 12
def string_to_ascii(input_str: str) -> list[int]:
    return [ord(char) for char in input_str]

print(string_to_ascii("Programming puzzles!"))


# puzzle 12.1 [bonus]
def ascii_to_string(input_ascii_codes: list[int]) -> str:
    return "".join(chr(code) for code in input_ascii_codes)

print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105,
110, 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]))


# puzzle 13
def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    vowels = set('aeiou')
    result = []

    for word in input_strs:
        lw = word.lower()
        if any(ch in vowels for ch in lw):
            result.append(word)
    return result

print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))


# puzzle 14

def reverse_first_five_positions(input_nums: list[int]) -> list[int]:
    return input_nums[:5][::-1] + input_nums[5:]

print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# puzzle 15
def filter_palindromes(input_strs: list[str]) -> list[str]:
    return [w for w in input_strs if w == w[::-1]]

print(filter_palindromes(["level", "world", "civic", "python"]))
# puzzle 2

def sum_if_less_than_fifty(num_one: int, num_two: int)-> int | None:

    total = num_one + num_two
    
    if total < 50:
        return total
    return None 

print(sum_if_less_than_fifty(20, 20))


# puzzle 3

def sum_even(input_nums: list[int]) -> int:
    sum = 0
    for i in input_nums:
        if i % 2 == 0:
            sum += i
    return sum

print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# puzzle 4

def remove_vowels(input_str: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
    new_str = "" 
    
    for char in input_str:  
        if char not in vowels:  
            new_str += char     

    return new_str


print(remove_vowels("Hello, World!"))  


# puzzle 5

def get_longest_string(input_strs: list[str]) -> str:
    longest = ""
    for animal in input_strs:
        if len(animal) > len(longest):
            longest = animal
    return longest
print(get_longest_string(["cat", "dog", "bird", "lizard"]))\

# puzzle 6

def filter_even_length_strings(input_strs: list[str])-> list[str]:
    name = []
    for animal in input_strs:
        if len(animal) % 2 == 0:
            name.append(animal)
    return name


print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))

# puzzle 7

def reverse_elements(input_nums: list[int]) -> list[int]:
    return input_nums[::-1]
print(reverse_elements([1, 2, 3, 4, 5]))


# puzzle 8 

def filter_type_str(input_list: list[str | int]) -> list[str]:
    result = []
    for item in input_list:
        if isinstance(item, str):
            result.append(item)
    return result

print(filter_type_str(["hello", 1, 2, "www"]))


# puzzle 9

def string_to_morse_code(input_str: str) -> str:
    morse_dict = { "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                   "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                   "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                   "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                   "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
                   "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
                   ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
                   "$": "...-..-", "@": ".--.-." }

    words = input_str.split(" ")
    morse_per_word = [
        " ".join(morse_dict.get(ch.lower(), "") for ch in word if ch.lower() in morse_dict)
        for word in words
    ]
    morse_sentence = " / ".join(morse_per_word)
    return morse_sentence


print(string_to_morse_code("HELLO, WORLD!"))

# puzzle 10

def get_second_largest_number(input_nums: list[int])-> int | None: 
    
    if len(input_nums) < 2:
        return None 
    input_nums.sort()
    return input_nums[-2]

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
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []  

    for word in input_strs:
        for char in word:
            if char in vowels:
                result.append(word)
                break  
    return result

print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))

# puzzle 14 

def reverse_first_five_positions(input_nums: list[int]) -> list[int]:
    return input_nums[:5][::-1] + input_nums[5:]
print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# puzzle 15
def filter_palindromes(input_strs: list[str]) -> list[str]:
    result = []
    for word in input_strs:
        if word == word[::-1]:
            result.append(word)
    return result
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


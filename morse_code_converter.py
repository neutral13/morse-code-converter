morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

reverse_morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '   ': ' '
}

query = input("Do you want to translate from\n(1)Morse to English\n or \n(2)English to Morse: ")
if query == "2":
    user_string = input("Enter text: ")
    def translation(text):
        text = text.upper()
        morse = ''
        for char in text:
            if char == ' ':
                morse += '  '
            else:
                morse += morse_code_dict[char] + ' '
        return morse

    print(translation(user_string))
else:
    morse_code_input = input("Enter text: ")
    def morse_translation(code):
        morse_code_list = code.split(' ')
        english_translation = ""
        is_word_separator = False

        for morse_code in morse_code_list:
            if morse_code:
                english_character = reverse_morse_code_dict.get(morse_code, '')
                if is_word_separator:
                    english_translation += ' '
                    is_word_separator = False
                english_translation += english_character
            else:
                is_word_separator = True

        return english_translation.strip()

    print(morse_translation(morse_code_input))
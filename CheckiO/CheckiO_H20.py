"""
Your task is to decrypt the secret message using the [Morse code](https://en.wikipedia.org/wiki/Morse_code)
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input : The secret message.
Output : The decrypted text.

Example:

morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

Precondition : 0 < len(message) < 100
The message will consists of numbers and English letters only.
"""


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

MORSE["!"] = " "
def morse_decoder(code):
    k = [MORSE[i] for i in code.replace('   ',' ! ').split(' ') if i in MORSE]
    morse = ''.join(k)
    return morse[0].upper() + morse[1:]

print(morse_decoder("..--- ----- .---- ---.."))
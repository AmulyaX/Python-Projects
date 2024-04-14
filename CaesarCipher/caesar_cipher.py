import caesar_cipher_art
import caesar_alphabet_list


def caesar_fun(input_text, input_shift, input_direction):
    out_text = ""
    for char in input_text:
        if char not in caesar_alphabet_list.alphabet:
            out_text += char
            continue
        else:
            pos = caesar_alphabet_list.alphabet.index(char)
        if input_direction == "encode":
            shifted_pos = pos + input_shift
        else:
            shifted_pos = pos - input_shift
        #  Modulo Operator (%) with the length of the alphabet list to ensure the new index stays within the valid range
        #  (0 to 25 for lowercase letters).
        final_shift = shifted_pos % len(caesar_alphabet_list.alphabet)
        out_text += caesar_alphabet_list.alphabet[final_shift]
    print(f"The {input_direction}d text is: ", out_text)


print(caesar_cipher_art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ("encode", "decode"):
        print("ERROR: Invalid direction: ", direction)
        continue

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    if shift > len(caesar_alphabet_list.alphabet):
        print("ERROR: Invalid shift:", shift)
        continue

    caesar_fun(text, shift, direction)

    restart = input("Do you want to restart the Cipher Program? Type 'yes' or 'no'\n").lower()
    if restart == "yes":
        continue
    if restart == "no":
        break

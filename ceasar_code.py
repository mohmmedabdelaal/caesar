def caesar_cipher(text, shift, direction):
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    #             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('a') if char.islower() else ord('A')
            index = (ord(char) - start + shift) % 26
            result_text += chr(start + index)
        else:
            result_text += char  # Keep non-alphabetic characters unchanged
    return result_text
    # if char in alphabet:
    #     index = alphabet.index(char)
    #     if direction == 'encode':
    #         index = (index + shift) % 26
    #     elif direction == 'decode':
    #         index = (index - shift) % 26
    #     result_text += alphabet[index]
    # else:
    #     result_text += char


def main():
    while True:

        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to exiting:\n")

        if direction == 'exit':
            print('Exiting...')
            break
        text = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Invalid shift number, Exiting...")
            continue
        if direction not in ['encode', 'decode']:
            print('Invalid direction')
            continue

        result = caesar_cipher(text, shift, direction)
        print(f'The {direction}d text is: {result}')


if __name__ == '__main__':
    main()

import pyfiglet


def caesar(start_text, shift_amount, cipher_direction):
    """
    Encode or decode a given text using the Caesar cipher method.

    Args:
    - start_text (str): The text to be encoded or decoded.
    - shift_amount (int): The number of positions to shift each character in the text.
    - cipher_direction (str): Either "encode" for encoding or "decode" for decoding.

    Returns:
    - str: The encoded or decoded text.
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
            continue
        position = alphabet.index(char)
        new_position = (position + shift_amount) % 26  # Ensure it wraps around correctly
        end_text += alphabet[new_position]

    # Convert the end_text using pyfiglet
    formatted_end_text = pyfiglet.figlet_format(end_text, font="digital")
    return formatted_end_text


def main():
    """
    The main function to run the Caesar cipher program.
    """
    logo = pyfiglet.figlet_format("Caesar Cipher")
    print(logo)

    while True:
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if again == "no":
            print("Goodbye")
            break
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ["encode", "decode"]:
            print("Invalid choice. Please choose 'encode' or 'decode'.")
            continue
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26  # Ensure the shift is within 0-25 range
        result = caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        print(result)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
    main()

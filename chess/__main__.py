import numpy as np


def print_decipher_remove_column_letters(grid_list, final):
    print(">>>>>> printing decipher after removing column letters")
    final_as_set = set(final)
    for i in range(0, 8):
        column = set([str(grid_list[j]) for j in range(i, grid_list.size, 8)])
        remaining = final_as_set.difference(column)
        print(f"remaining values: {remaining}")

        for value in remaining:
            # get distance from 'A' and reduce by one file (column on a chess board)
            val_ord = ord(value) - 65
            new_letter = get_new_cipher_value(val_ord, 1)
            print(f"old letter: {value}, new letter: {new_letter}")


def print_decipher(final, shift):
    print(">>>>>> printing decipher without removal:")
    new_value = []
    for value in final:
        cur_val = ord(value) - 65
        new_letter = get_new_cipher_value(cur_val, shift)
        print(f"old letter: {value}, new letter: {new_letter}")
        new_value.append(new_letter)

    return "".join(new_value)


def get_new_cipher_value(ord_val, shift_count):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return letters[(ord_val + (26 - shift_count)) % len(letters)]


# name of file filled in chess board from left to right, top to bottom
# grid_string = "FHXJQVZTFIUSUVXRLHOSQQVITCOQTHLDNEUAUOJZVHDEOSOQYLZJHELEDJIEPZAP"
# name of file filled in chess board grid via a1-h1, a2-h2... order
grid_string = "DJIEPZAPYLZJHELEVHDEOSOQNEUAUOJZTCOQTHLDLHOSQQVIFIUSUVXRFHXJQVZT"
# response with algebraic notation
coordinate_string = "B8C6E5G6H4F5H6G4F6H5F4E6G5"
# full response
# coordinate_string = "B8C6C6E5E5G6G6H4H4F5F5H6H6G4G4F6F6H5H5F4F4E6E6G5G5F3F3D2D2B3B3A1A1C2C2B4"


grid_list = np.array(list(grid_string))
grid = np.reshape(grid_list, (8, 8))
print(grid)

coord_list = np.array(list(coordinate_string))
X_coords = coord_list[::2]
X_ascii = [ord(x)-65 for x in X_coords]
Y_coords = coord_list[1::2]
Y_coords = [int(y)-1 for y in Y_coords]
coords = zip(X_ascii, Y_coords)
final = []
for coord in coords:
    print(f"coord: {coord}")
    final.append(str(grid[coord]))

final_as_string = "".join(final)
print(f"final: {final} -> as string: {final_as_string}")


# print_decipher_remove_column_letters(grid_list, final)
# for i in range(0, 26):
#    print_decipher(final, i)
result = print_decipher(final, 0)
print(f"result: {result}")
sorted = sorted(list(result))
print(f"sorted result: {sorted}")


def vigenere_cipher(text, keyword):
    keyword_length = len(keyword)
    return ''.join(
        chr((ord(t) - 65 + ord(keyword[i % keyword_length]) - 65) % 26 + 65)
        for i, t in enumerate(text)
    )


keyword = "GREUZE"  # Keyword related to the artist
ciphertext = "HDULDOELSHUJ"
decrypted_text = vigenere_cipher(final_as_string, keyword)
ai_decrypted_text = vigenere_cipher(ciphertext, keyword)
try_three_text = vigenere_cipher(result, keyword)
try_four = vigenere_cipher("XVQQZQQZQQZQ", keyword)
print(f"Decrypted with keyword '{keyword}': {decrypted_text}")
print(f"Decrypted with keyword (AI answer) '{keyword}' : {ai_decrypted_text}")
print(f"Decrypted with keyword try four '{keyword}' : {try_four}")
print(
    f"Decrypted with keyword (shifted answer) '{keyword}' : {try_three_text}")

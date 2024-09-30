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


def print_decipher(final, shift):
    new_value = []
    for value in final:
        cur_val = ord(value) - 65
        new_letter = get_new_cipher_value(cur_val, shift)
        new_value.append(new_letter)

    return "".join(new_value)


def get_new_cipher_value(ord_val, shift_count):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return letters[(ord_val + (26 - shift_count)) % len(letters)]


# name of file filled in chess board from left to right, top to bottom
#grid_string = "FHXJQVZTFIUSUVXRLHOSQQVITCOQTHLDNEUAUOJZVHDEOSOQYLZJHELEDJIEPZAP"

# name of file filled in chess board grid via a1-h1, a2-h2... order
#grid_string = "DJIEPZAPYLZJHELEVHDEOSOQNEUAUOJZTCOQTHLDLHOSQQVIFIUSUVXRFHXJQVZT"
grid_string = "TRIDZQEPZXVLJOLAVVQHOSEZQUQTUOHPJSSQAEJEXUOOUDZIHIHCEHLJFFLTNVYD"
# response with algebraic notationa
coordinate_string = "B8C6E5G6H4F5H6G4F6H5F4E6G5"
# full response
# coordinate_string = "B8C6C6E5E5G6G6H4H4F5F5H6H6G4G4F6F6H5H5F4F4E6E6G5G5F3F3D2D2B3B3A1A1C2C2B4"
deciphered_gridstring = print_decipher(list(grid_string), 1)
print(f"deciphered grid_string: {deciphered_gridstring}")

grid_list = np.array(list(grid_string))
grid = np.reshape(grid_list, (8, 8))
print(grid)

coord_list = np.array(list(coordinate_string))
X_coords = coord_list[::2]
X_ascii = [(ord(x) - 65) for x in X_coords]
Y_coords = coord_list[1::2]
Y_coords = [(8-int(y)) for y in Y_coords]
coords = zip(Y_coords, X_ascii)
final = []
for coord in coords:
    final.append(str(grid[coord]))

final_as_string = "".join(final)
print(f"final: {final} -> as string: {final_as_string}")

result = print_decipher(final, 1)
print(f"result: {result}")
sorted = sorted(list(result))
print(f"sorted result: {sorted}")


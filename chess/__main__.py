import numpy as np


def print_decipher_remove_column_letters(grid_list, final):
    print(">>>>>> printing decipher after removing column letters")
    final_as_set = set(final)
    for i in range(0, 8):
        column = set([str(grid_list[j]) for j in range(i, grid_list.size, 8)])
        remaining = final_as_set.difference(column)
        print(f"remaining values: {remaining}")

        for value in remaining:
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


# grid_string = "FHXJQVZT-FIUSUVXR-LHOSQQVI-TCOQTHLD-NEUAUOJZ-VHDEOSOQ-YLZJHELE-DJIEPZAP"
grid_string = "DJIEPZAPYLZJHELEVHDEOSOQNEUAUOJZTCOQTHLDLHOSQQVIFIUSUVXRFHXJQVZT"
coordinate_string = "B8C6E5G6H4F5H6G4F6H5F4E6G5"

grid_list = np.array(list(grid_string))
grid = np.reshape(grid_list, (8, 8))
print(grid)

coord_list = np.array(list(coordinate_string))
X_coords = coord_list[::2]
X_ascii = [ord(x)-65-1 for x in X_coords]
Y_coords = coord_list[1::2]
Y_coords = [int(y)-2 for y in Y_coords]
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
result = print_decipher(final, 1)
print(f"result: {result}")

import requests
import string
import numpy
# -----------------
# Step 1
# hippo holding an ear          -- caterpillar in front of apple -- llama holding an eggplant
# beaver holding a rose         -- fox on an anvil               -- dapper crocodile with a ball(orange?)
# koala eating ramen            -- dolphin holding a lightbulb   -- giraffe playing guitar in a tophat
# elephant with a record player -- iguana on a toaster           -- leopard holding an umbrella
letters_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_letters = set(letters_string)

def pretty_print(st, name):
    result = sorted(list(st))
    print(f"{name}: {result}")

def print_letters_from_numbers(nums):
    result = []
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for num in nums:
        value = int(num)
        result.append(letters[value-1])

    return result

animals = set("HCLBFAKDGEIJ")
items = set("EAERABNLGMTU")

combined = animals.union(items)

minus_both = all_letters.difference(combined)
# pretty_print(animals, "animals")
# pretty_print(items, "items")
# pretty_print(minus_both, "missing letters")
# BRALRAGETUNE
# BRALRAGETUNA
# ORALRAGETUNA
# ORALRAGETUNE
# ORALPAGETUNA
# ORALPAGETUNE (!!)
# -----------------

# -----------------
# Step 2
# top-down, left then right
# numbers_string = "08-19-05-07-01-03-15-23-16-09-20-25"
# clockwise
numbers_string = "03-01-07-05-19-08-15-23-16-09-20-25"
# left-to-right, top to bottom
# numbers_string = "08-15-19-23-05-16-07-09-01-20-03-25"
# circular pattern - arcing from center left to center right, top then bottom (crystal ball pattern? idk)
# numbers_string = "04-05-19-08-15-23-07-01-03-25-20-09"

# CAGESHOWPITY (!!)


number_list = numbers_string.split("-")
print(f"numbers-list: {number_list}")

step_2_result = print_letters_from_numbers(number_list)
print(f"result: {step_2_result}")
print("".join(step_2_result))

# -----------------
#  Step 3
# first letter (roygbiv) -> second letter -> shape (s=square, c=circle, h=hex, t=triangle)
# rs + rs = rs (rs = 0)
# os + os = ys
# os + ys = gs
# ys + ys = bs
# gs + gs = vs
# ys + gs = is
# vs + os = rc
# yc + rc = yt
# ic + rt = ih
# gt + rt = gs
# vh + os = rs
# gt + it = oc
# oh + bc = is
# gh + ic + bt = ih

# ih - ic = gs - rt
# gs = ih + rt - ic
# gt = ih - ic

# gt = 3 - rt
# rt = gs - gt
# rt = ih - ic
# ih - ic = 3 - gt
# ih + gt = 3 + ic

# derived
# rt = gh + bt
# rt = ih - ic
# ih = gh + bt + ic
# oh + bc = ys + gs
# oh + bc = 5
# 3(os) = gs
# 4(os) = bs
# 5(os) = is
# 6(os) = vs
# 7(os) = rc
# 7(os) + yc = yt
# oh = 5(os) - bc
# bc = 5(os) - oh
# gt + rt = 3(os)
# gt = 3 - rt
# gt = oc - it

# rt = ih - ic
# rt = gs - gt

# ih - ic = gs - gt

# yt - yc = 7
# yt

# unique potion types
# red => square, circle, triangle
# orange => square, circle, hex
# yellow => square, circle, triangle
# green => square, triangle, hex
# blue => square, circle, triangle
# indigo => square, circle, hex, triangle
# violet => square, hex



# bottom seems like a cipher key so mod 28 -> 7 colors, 4 shapes. seems to fit 
# plugged the values in after all of the coincidences to verify -- success!

def get_value(num):
    cipher_values = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ?!")
    return cipher_values[num % 28]

def print_cipher_row(lst, index):
    row = []
    for square in lst:
        next_val = sum(square)
        row.append(get_value(next_val))
    print(f"row[{index}] {row}")

# squares =>   r=0,  o=1,   y=2,   g=3,   b=4,  i=5,  v=6
# circles =>   r=7,  o=8,   y=9,   g=10,  b=11, i=12, v=13
# triangles => r=14, o=15,  y=16,  g=17,  b=18, i=19, v=20
# hex =>       r=21, o=22,  y=23,  g=24,  b=25, i=26, v=27

value_dict = { 
              "rs": 0,
              "os": 1,
              "ys": 2,
              "gs": 3,
              "bs": 4,
              "is": 5,
              "vs": 6,

              "rc": 7,
              "oc": 8,
              "yc": 9,
              "gc": 10,
              "bc": 11,
              "ic": 12,
              "vc": 13,

              "rt": 14,
              "ot": 15,
              "yt": 16,
              "gt": 17,
              "bt": 18,
              "it": 19,
              "vt": 20,

              "rh": 21,
              "oh": 22,
              "yh": 23,
              "gh": 24,
              "bh": 25,
              "ih": 26,
              "vh": 27,
              }


def convert_to_values(lst):
    return [value_dict[val] for val in lst]


def rotated_values(lst):
    flattened = flatten_list(lst)
    print(f"flattened: {flattened}")
    rotated = numpy.roll(flattened, -1)
    print(f"rotated: {rotated}")
    return regroup_values(rotated)


def flatten_list(lst):
    return [x for xs in lst for x in xs]


def regroup_values(lst):
    if len(lst) != 12:
        return []
    result = [[], [], [], []]
    for val in range(0, 3):
        result[0].append(lst[val])
    for val in range(3, 6):
        result[1].append(lst[val])
    for val in range(6, 9):
        result[2].append(lst[val])
    for val in range(9, 12):
        result[3].append(lst[val])

    return result


row_1_flasks = [["yh", "gc", "ic"], ["oc", "oc", "ih"], ["ot", "ih", "vs"], ["gh", "gt", "rt"]]
row_2_flasks = [["yc", "yh", "rc"], ["bt", "bc", "gs"], ["oh", "rc", "bs"], ["it", "bh", "gs"]]
row_3_flasks = [["vh", "is", "vh"], ["vc", "os", "gs"], ["rc", "yh", "ic"], ["ic", "rc", "gh"]]
row_4_flasks = [["vh", "bh", "ot"], ["vt", "ic", "gh"], ["gh", "vh", "yh"], ["gh", "rs", "yh"]]

row_1_values = [convert_to_values(val) for val in row_1_flasks]
row_2_values = [convert_to_values(val) for val in row_2_flasks]
row_3_values = [convert_to_values(val) for val in row_3_flasks]
row_4_values = [convert_to_values(val) for val in row_4_flasks]

print("------------ phase 1 -------------")
print_cipher_row(row_1_values, 1)
print_cipher_row(row_2_values, 2)
print_cipher_row(row_3_values, 3)
print_cipher_row(row_4_values, 4)

row_1_values_rotated = rotated_values(row_1_flasks)
row_2_values_rotated = rotated_values(row_2_flasks)
row_3_values_rotated = rotated_values(row_3_flasks)
row_4_values_rotated = rotated_values(row_4_flasks)
print("----------------- rotated values ----------------")
print(row_1_values_rotated)
print(row_2_values_rotated)
print(row_3_values_rotated)
print(row_4_values_rotated)

row_1_values_converted = [convert_to_values(val) for val in row_1_values_rotated]
row_2_values_converted = [convert_to_values(val) for val in row_2_values_rotated]
row_3_values_converted = [convert_to_values(val) for val in row_3_values_rotated]
row_4_values_converted = [convert_to_values(val) for val in row_4_values_rotated]

print("------------ phase 1 rotated left -------------")
print_cipher_row(row_1_values_converted, 1)
print_cipher_row(row_2_values_converted, 2)
print_cipher_row(row_3_values_converted, 3)
print_cipher_row(row_4_values_converted, 4)

# CUREVILEACTS!!

# ------------------------
# JAPAN/NeedleMouse => Hedgehog
# France/Milk Chicken => EggNog 
# China/Dragon Shrimp? => Lobster  
# Iran/ tiny elephant fart? => Popcorn
# Sweden/Butter goose? => Sandwich
# SouthAfrica/Muddy Pig?Earth Pig => Aardvark 
# China/snow cake? => refrigerator
# Russia/ god's cow => Ladybird
# Hungary/ Foam girl => Mermaid
# Germany/Sick car => Ambulance
# Sweden/frog with a shield => Tortoise
# Finland/Stairs-slide => Escalator
# ------------------------
# Orbital => Oral + bit
# Passage => Page + ass
# Tribune => Tune + rib
# Courage => Cage + our
# Shallow => Show + all
# ??? => Pity + ???
# Capture => Cure + apt
# Village => Vile + lag
# Actions => Acts + ion
# Mandate => Mate + and

# Shallow => Show + all
# Mandate => Mate + and
# Capture => Cure + apt
# Passage => Page + ass
# Orbital => Oral + bit
# Actions => Acts + ion
# Village => Vile + lag
# Courage => Cage + our
# Tribune => Tune + rib
# ??? => Pity + ???
# ??? => Help + ???
# ??? => Sail + ???
#741BA0982653
letter_values = [7, 4, 1, 11, 10, 0, 9, 8, 2, 6, 5, 3]

key = list('pityhelpsail')
converted = [key[x] for x in letter_values]
print(f"result not sorted: {converted}")

# PhilipAstley 
# Final Answer: CaughtByPress


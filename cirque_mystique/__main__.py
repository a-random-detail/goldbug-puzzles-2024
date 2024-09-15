
# hippo holding an ear          -- caterpillar in front of apple -- llama holding an eggplant
# beaver holding a rose         -- fox on an anvil               -- dapper crocodile with a ball
# koala eating ramen            -- dolphin holding a lightbulb   -- giraffe playing guitar in a tophat
# elephant with a record player -- iguana on a toaster           -- leopard holding an umbrella

def pretty_print(st, name):
    result = sorted(list(st))
    print(f"{name}: {result}")


all_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
animals = set("HCLBFAKDGEIJ")
items = set("EAERABNLGMTU")


combined = animals.union(items)

minus_both = all_letters.difference(combined)
pretty_print(animals, "animals")
pretty_print(items, "items")
pretty_print(minus_both, "missing letters")

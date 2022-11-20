# ProjectEuler - Problem 31.
# Anders Imenes

# Hvor mange kombinasjoner av 1, 2, 5, 10, 20, 50, 100 og 200 gir totalt 200?

# 1 - mynt (1 * 200)
# 2 - mynt (2 * 100)
# 3 - mynt (1x 100, 2x 50)

combos = {}


def combinations(currentValue, upperLimit=200):
    # Reset counter
    numbOfCombos = 0

    # If we reach leaf
    if currentValue == 0:
        return 1

    # If the value is already known, return it
    elif (currentValue, upperLimit) in combos:
        return combos[currentValue, upperLimit]

    # Else recurse through the tree
    else:
        if currentValue >= 200 and upperLimit >= 200:
            numbOfCombos = numbOfCombos + combinations(currentValue - 200, 200)
        if currentValue >= 100 and upperLimit >= 100:
            numbOfCombos = numbOfCombos + combinations(currentValue - 100, 100)
        if currentValue >= 50 and upperLimit >= 50:
            numbOfCombos = numbOfCombos + combinations(currentValue - 50, 50)
        if currentValue >= 20 and upperLimit >= 20:
            numbOfCombos = numbOfCombos + combinations(currentValue - 20, 20)
        if currentValue >= 10 and upperLimit >= 10:
            numbOfCombos = numbOfCombos + combinations(currentValue - 10, 10)
        if currentValue >= 5 and upperLimit >= 5:
            numbOfCombos = numbOfCombos + combinations(currentValue - 5, 5)
        if currentValue >= 2 and upperLimit >= 2:
            numbOfCombos = numbOfCombos + combinations(currentValue - 2, 2)
        if currentValue >= 1 and upperLimit >= 1:
            numbOfCombos = numbOfCombos + combinations(currentValue - 1, 1)

        combos[currentValue, upperLimit] = numbOfCombos
        return numbOfCombos

print(combinations(10))
print(combos)
def character_count(word):
    character_statistic = {}
    for element in word:
        character_statistic[element] = character_statistic.get(element, 0) + 1
    return character_statistic


if __name__ == "__main__":
    print(character_count('Happiness'))
    print(character_count('smiles'))

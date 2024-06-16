# Exercise 2:
def count_chars(string):
    character_statistic = {}
    for char in string:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    sorted_character_statistic = dict(sorted(character_statistic.items()))
    return sorted_character_statistic

string = 'Happiness'
print(count_chars(string))
# Third try
full_dot = '●'
empty_dot = '○'

def name_validation(name):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

def stats_validation(strength, intelligence, charisma):
    for stat in (strength, intelligence, charisma):
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

def stats_points(stat):
    return full_dot*stat + empty_dot*(10-stat)

def create_character(name, strength, intelligence, charisma):
    name_error = name_validation(name)
    if name_error:
        return name_error
    stats_error = stats_validation(strength, intelligence, charisma)
    if stats_error:
        return stats_error
    
    return (f'{name}\n'
            f'STR {stats_points(strength)}\n'
            f'INT {stats_points(intelligence)}\n'
            f'CHA {stats_points(charisma)}\n')

print(create_character('ren', 4, 2, 1))
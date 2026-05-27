# First try
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Name validation
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    # Stats validation
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    # Return string creation
    strength_points = ''
    intelligence_points = ''
    charisma_points = ''
    while True:
        if len(strength_points) < strength:
            strength_points += '●'
        elif len(strength_points) < 10:
            strength_points += '○'
        if len(intelligence_points) < intelligence:
            intelligence_points += '●'
        elif len(intelligence_points) < 10:
            intelligence_points += '○'
        if len(charisma_points) < charisma:
            charisma_points += '●'
        elif len(charisma_points) < 10:
            charisma_points += '○'
        
        if len(strength_points) == 10 and len(intelligence_points) == 10 and len(charisma_points) == 10:
            break
    
    return f'{name}\nSTR {strength_points}\nINT {intelligence_points}\n CHA {charisma_points}'

print(create_character('ren', 4, 2, 1))
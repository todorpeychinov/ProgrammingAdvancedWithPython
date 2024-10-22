def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for card_name, card_type in args:
        if card_type == 'monster':
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)

    for k, v in kwargs.items():
        if v == 'monster':
            monster_cards.append(k)
        else:
            spell_cards.append(k)

    monster_cards = sorted(monster_cards, reverse=True)
    spell_cards = sorted(spell_cards)

    result = ""

    if monster_cards:
        result += "Monster cards:\n"
        for card in monster_cards:
            result += f"  ***{card}\n"

    if spell_cards:
        result += "Spell cards:\n"
        for card in spell_cards:
            result += f"  $$${card}\n"

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print()
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print()
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))


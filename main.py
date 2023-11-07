import dankcrypt

engine = dankcrypt.Engine('dankcrypt')
print(engine.title)

greatsword = dankcrypt.Object('greatsword')
greatsword.equippable = True
greatsword.equippableSlots += ['leftarm', 'rightarm']

herb = dankcrypt.Object('herb')
herb.consumable = True

user = dankcrypt.Character('Guts')
user.addToInventory(greatsword)
user.equipItem(greatsword, 'leftarm')

greatsword2 = user.getItemFromInventory(greatsword.id)
print(str(greatsword2.id))

user.addToInventory(herb)
print(user.inventory)
user.consumeItem(herb)
print(user.inventory)

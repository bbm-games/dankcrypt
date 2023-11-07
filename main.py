import dankcrypt

engine = dankcrypt.Engine("dankcrypt")
print(engine.title)

greatsword = dankcrypt.Object('greatsword')
greatsword.equippableSlots += ['leftarm', 'rightarm']

user = dankcrypt.Character('Guts')
user.addToInventory(greatsword)
user.equipItem(greatsword,'leftarm')

greatsword2 = user.getItemFromInventory(greatsword.id)
print(str(greatsword2.id))

print(user.slots)




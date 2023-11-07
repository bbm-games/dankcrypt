import dankcrypt
import dankcrypt.consumables.potions

engine = dankcrypt.Engine('dankcrypt')
print(engine.title)

greatsword = dankcrypt.Object('greatsword')
greatsword.equippable = True
greatsword.equippableSlots += ['leftarm', 'rightarm']

herbpotion = dankcrypt.consumables.potions.HealthPotion('herbpotion')

user = dankcrypt.Character('Guts')
user.addToInventory(greatsword)
user.equipItem(greatsword, 'leftarm')

greatsword2 = user.getItemFromInventory(greatsword.id)
print(str(greatsword2.id))

user.unequip('leftarm')

user.addToInventory(herbpotion)
print(user.inventory)
user.consumeItem(herbpotion)
print(user.inventory)

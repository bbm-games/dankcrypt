import dankcrypt
import dankcrypt.consumables.potions
import dankcrypt.weapons.greatswords

engine = dankcrypt.Engine('dankcrypt')
print(engine.title)

greatsword = dankcrypt.weapons.greatswords.FireGreatSword('gutssword')
greatsword.equippable = True
greatsword.equippableSlots += ['leftarm', 'rightarm']

greatsword2 = dankcrypt.weapons.greatswords.FireGreatSword('griffithsword')
greatsword2.equippable = True
greatsword2.equippableSlots += ['leftarm', 'rightarm']

herbpotion = dankcrypt.consumables.potions.HealthPotion('herbpotion')

user = dankcrypt.Character('Guts')
user.addToInventory(greatsword)
user.equipItem(greatsword, 'leftarm')

enemy = dankcrypt.Character('Griffith')
enemy.addToInventory(greatsword2)
enemy.equipItem(greatsword2, 'leftarm')

# have griffith attack
print(user.statuses.values())
for i in range(10):
  enemy.meleeAttack('leftarm', user)
print(user.statuses.values())

user.nextTick()

# heal the user
user.addToInventory(herbpotion)
user.consumeItem(herbpotion)


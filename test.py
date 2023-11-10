import dankcrypt
import dankcrypt.consumables.potions
import dankcrypt.equippables.weapon
import inquirer

#Testing the other classes
greatsword = dankcrypt.equippables.weapon.Weapon('gutssword')
greatsword.equippable = True
greatsword.equippableSlots += ['leftarm', 'rightarm']

greatsword2 = dankcrypt.equippables.weapon.Weapon('griffithsword')
greatsword2.equippable = True
greatsword2.equippableSlots += ['leftarm', 'rightarm']

herbpotion = dankcrypt.consumables.potions.HealthPotion('herbpotion')

user = dankcrypt.Character('Guts')
user.addToInventory(greatsword)
user.equipItem(greatsword, 'leftarm')

enemy = dankcrypt.Character('Griffith')
enemy.addToInventory(greatsword2)
enemy.equipItem(greatsword2, 'leftarm')

# have griffith attack 10 times
for i in range(20):
  print("Gut's current health: " + str(user.currentHealth))
  print("Gut's current statuses: " + str(user.statuses))
  enemy.meleeAttack('leftarm', user)
  # after each combat move, a next tick should be performed
  user.nextTick()
  enemy.nextTick()

# heal the user
user.addToInventory(herbpotion)
user.consumeItem(herbpotion)

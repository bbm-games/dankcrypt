import dankcrypt
import dankcrypt.consumables.potions
import dankcrypt.equippables.weapon
import inquirer


engine = dankcrypt.Engine('dankcrypt')

inp = input('Enter player name: ')

questions = [
  inquirer.List('vocation',
                message="Pick a starting vocation",
                choices= [doc['class_name'] for doc in engine.loreData['vocations']],
            ),
]
answers = inquirer.prompt(questions)

engine.newGame(inp, answers["vocation"])

# rudimentary game loop
while(not engine.playerChar.isDead):
    # collect input, in this case we're getting really raw input lmao
    inp = input('$ ')
    exec(inp)

    # next tick should always be called on all game objects
    engine.playerChar.nextTick()


""" Testing the other classes 
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

# have griffith attack 10 times
print(user.statuses.values())
for i in range(10):
  enemy.meleeAttack('leftarm', user)
print(user.statuses.values())

user.nextTick()

# heal the user
user.addToInventory(herbpotion)
user.consumeItem(herbpotion)

"""
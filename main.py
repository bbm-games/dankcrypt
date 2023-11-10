import dankcrypt
import dankcrypt.consumables.potions
import dankcrypt.equippables.weapon
import inquirer

engine = dankcrypt.Engine('dankcrypt')

inp = input('Enter player name: ')

questions = [
    inquirer.List(
        'vocation',
        message="Pick a starting vocation",
        choices=[doc['class_name'] for doc in engine.loreData['vocations']],
    ),
]
answers = inquirer.prompt(questions)

engine.newGame(inp, answers["vocation"])

# rudimentary game loop
while (not engine.playerChar.isDead):
  # collect input, in this case we're getting really raw input lmao
  inp = input('$ ')
  exec(inp)

  # next tick should always be called on all game objects
  engine.playerChar.nextTick()

import dankcrypt
import dankcrypt.consumables.potions
import dankcrypt.equippables.weapon
import inquirer
import curses

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

# start curses
stdscr = curses.initscr()
# In this program, we don't want keystrokes echoed to the console,
# so we run this to disable that
curses.noecho()

# Additionally, we want to make it so that the user does not have to press
# enter to send keys to our program, so here is how we get keys instantly
curses.cbreak()

# Hide the cursor
curses.curs_set(0)

# Lastly, keys such as the arrow keys are sent as funny escape sequences to
# our program. We can make curses give us nicer values (such as curses.KEY_LEFT)
# so it is easier on us.
stdscr.keypad(True)

# First, clear the screen
stdscr.erase()

stdscr.nodelay(True)

# rudimentary game loop
while (not engine.playerChar.isDead):

  # collect input, in this case we're getting really raw input lmao
  # Wait for a keystroke
  key = stdscr.getch()

  # Process the keystroke
  if key == ord('q'):
    break
  elif key == curses.KEY_LEFT:
    # First, clear the screen
    stdscr.erase()
    engine.playerChar.moveLeft()
  elif key == curses.KEY_RIGHT:
    # First, clear the screen
    stdscr.erase()
    engine.playerChar.moveRight()
  elif key == curses.KEY_UP:
    # First, clear the screen
    stdscr.erase()
    engine.playerChar.moveUp()
  elif key == curses.KEY_DOWN:
    # First, clear the screen
    stdscr.erase()
    engine.playerChar.moveDown()

  # Draw HUD
  stdscr.addstr(
      curses.LINES - 1, 0, engine.playerChar.title + ' | Level ' +
      str(engine.playerChar.level) + ' ' + engine.playerChar.vocation,
      curses.A_STANDOUT)
  if (key != -1):
    stdscr.addstr(curses.LINES - 1, int(curses.COLS / 2),
                  "You pressed " + chr(key), curses.A_STANDOUT)

  # draw user character
  stdscr.addstr(engine.playerChar.posY, engine.playerChar.posX, 'O',
                curses.A_BLINK)

  # next tick should always be called on all game objects
  engine.playerChar.nextTick()

  # Draw the screen
  stdscr.refresh()

  #curses.napms(100)

# shut down curses
curses.curs_set(1)
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

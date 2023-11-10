# dankcrypt
rpg engine

## OOP Structure
There are 3 parent classes. All other things in the game are subclasses.

1. Engine - contains code for rudimentary game loop, game loading, game saving, loading map

2. Character - any human or AI controlled entity
   - Humanoids - AI controlled NPC
   - Monsters - AI controlled NPC

3. Object - any non human or AI controlled entity
   - HealthPotion
   - ManaPotion
   - Armor
   - Weapon
   - Item
   - QuestItem
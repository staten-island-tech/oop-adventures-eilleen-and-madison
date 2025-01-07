
# ChatGPT Coding Diary

##  Name: Shirley Jiang

### Date: 01/07/

---

## 1. **Task/Problem Description**

I want to make a feature where the player has a chance to receive a power up. 

---

## 2. **Initial Approach/Code**

Initially, I made a class and imported random. Before using ChatGPT, I tried to make a function where the power up only has a certain amount of chance to activate.

```python
import random

class PowerUp:
    def __init__(self, chance=0.2):
        self.chance = chance 
```

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
"How can I make a feature where the player has a chance to deal double damage?"

```

---

## 4. **ChatGPT's Suggestions/Code Changes**

```python
import random

class Player:
    def __init__(self, name, damage):
        self.name = name
        self.base_damage = damage

    def attack(self):
        # Set a 20% chance for double damage
        chance = random.random()  # Generates a number between 0 and 1
        if chance <= 0.2:  # 20% chance
            print(f"Critical hit! {self.name} deals double damage!")
            return self.base_damage * 2
        else:
            print(f"{self.name} attacks normally.")
            return self.base_damage

# Example Usage
player = Player("Hero", 10)

# Simulating an attack
damage = player.attack()
print(f"Damage dealt: {damage}")

```

ChatGPT's solution was to make a probability threshold, and using a conditional statement to determine whether the player gets the power up. It differs from my orginal approach because defined a separate class for the attack.

---

## 5. **Reflection on Changes**

ChatGPT recommended using a separate class for making/defining a class for chance, and making/defining a class where the chance gets applied to the player after an attack. I think this will improve how 

- Why do you think ChatGPT's suggestions are helpful or relevant?
- Did the suggestions improve your code? How?
- Did you understand why the changes were made, or are you still uncertain about some parts?

Example:
> ChatGPT recommended using a more efficient sorting algorithm like quicksort. I think this will improve the runtime for large inputs, but I need to review the algorithm's complexity to fully understand its advantages.

---



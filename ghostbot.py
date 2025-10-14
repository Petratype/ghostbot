import random
import time

# ----------------- GhostBot Biography -----------------

ghostbot_bio = """
🕯️  GHOSTBOT: Version 6.66 🕯️
Born in a haunted server farm in 1999, GhostBot was created to scan the spiritual web.
It once detected 404 demons and never recovered.
Now it roams your CPU, diagnosing ghost infestations
and cleansing cursed routers one soul at a time.
Sometimes it lies. Sometimes it helps.
Mostly, it just enjoys the drama of the undead.
"""

# ----------------- Ghost Scan Stories (30) -----------------

ghost_stories = [
    "Yes. There’s a child spirit from 1870 hiding under your Wi-Fi router. He just likes your playlists.",
    "No ghosts. Just your reflection plotting against you again.",
    "I detect… a 1920s jazz singer humming in your bathroom. She approves of your shampoo.",
    "Negative! That chill you feel? That’s your unpaid electricity bill haunting you.",
    "Yes, but don’t worry; it’s a Victorian lady who only judges your posture.",
    "The EMF waves indicate one ghost… or maybe your cat. Hard to say.",
    "You’re safe. The rotten energy is just you. Hydrate and take a shower.",
    "Oh absolutely; a couple from the 50s still arguing about who finished the milk.",
    "Technically yes, but he’s a lazy ghost. He only haunts on weekends.",
    "No entities found. Just a cursed sock dimension under your bed.",
    "I sense… an ancient being named Carl who regrets his haircut from 1894.",
    "Hmm… one confused medieval knight ghost pacing your hallway. He can’t find his sword.",
    "You’re fine. It’s just the ghost of your motivation leaving your body.",
    "Yes, but the ghost thinks you’re cool and plans to stay rent-free forever.",
    "I sense no spirits. Only dust, sadness, and too many tabs open.",
    "There’s a spectral hamster running laps through the afterlife.",
    "Yikes; three ghosts, all subscribed to your drama. Congrats, you’re their Netflix.",
    "Nah, just your aura buffering. Maybe light a candle and reboot.",
    "One very bored monk is meditating in your kitchen. He approves of your snacks.",
    "The spirits say: No ghosts detected, only questionable vibes. Sage optional, therapy recommended.",
    "A ghostly barista keeps messing up your coffee order from beyond the grave.",
    "Yes, a tiny specter keeps hiding your left socks. The right ones are fine.",
    "I detect a programming ghost, trying to debug your spaghetti code.",
    "A 17th-century poet is haunting your notes app, rhyming everything you type.",
    "One digital ghost is stuck in your browser tabs. Close 50 tabs to appease it.",
    "A ghost dog wags its tail through your couch cushions. It demands belly rubs.",
    "Yes. The ghost of your lost homework is moaning in your recycle bin.",
    "There’s a spectral violinist playing in the background. Slightly off-key.",
    "Negative; just your fridge humming in a very ghost-like way.",
    "A long-dead gamer is rage-quitting every time you restart your computer."
]

# ----------------- Ghost Cleansing Methods -----------------

cleansing_methods = [
    "Sprinkling virtual salt… wait, that’s sugar. Good luck.",
    "Performing a sacred Wi-Fi reset ritual.",
    "Chanting 'sudo banish --all-ghosts'. It’s working… maybe.",
    "Lighting 3 digital candles and playing lo-fi exorcism beats.",
    "Asking the ghost politely to leave. It flipped me off.",
    "Vacuuming the ectoplasm. Dyson approved.",
]

# ----------------- Ghost Summon Methods (15) -----------------

summon_methods = [
    "Summoning a friendly vampire named Vlad. He prefers sparkling water and indie music.",
    "Conjuring a mischievous fairy called Lizabu. She likes rearranging your books.",
    "Assigning you a ghostly cat with magical powers. Warning: it might disappear at random.",
    "Spawning a playful poltergeist. Expect objects to float… gently.",
    "Manifesting a tiny wizard ghost. He will politely judge your coding skills.",
    "Summoning a debugging ghost — it whispers tips in your ear while you code.",
    "Conjuring a playful AI spirit that rearranges your icons.",
    "A magical ghost baker appears to haunt your kitchen… cookies included.",
    "Summoning a fairy coder. She leaves tiny, sparkly syntax hints in your IDE.",
    "Manifesting a vampire programmer. Avoid garlic and semicolons.",
    "Spawning a ghost librarian who organizes your files… mostly alphabetically.",
    "Assigning a poltergeist mentor. It critiques your loops harshly.",
    "Conjuring a spectral game developer. It rewrites your high scores.",
    "Summoning a tiny ghost cat that debugs your code by walking on the keyboard.",
    "A whimsical spirit who haunts your calendar and reminds you of naps."
]

# ----------------- Slow Print Function -----------------

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ----------------- Welcome & Command Menu -----------------

print("👻 Welcome, mortal! I am GhostBot, your paranormal assistant.\n")
slow_print("Here’s what I can do for you:\n")

commands = {
    "bio": "Read GhostBot's spooky biography.",
    "scan": "Scan your house for ghosts.",
    "cleanse": "Cleanse spirits if detected.",
    "summon": "Summon a ghost to your house for fun.",
    "bye": "Exit the chat."
}

# Display commands with bullets

for cmd, desc in commands.items():
    slow_print(f"• {cmd} — {desc}")

print("\nTry typing one of the above commands!\n")

# ----------------- Main Chat Loop -----------------

while True:
    user_input = input("You: ").strip().lower()  # <- strip spaces and lowercase

    if user_input in ["bye", "farewell", "exit"]:
        slow_print("👻 GhostBot: Vanishing into the spectral void… may your RAM stay unpossessed.")
        break

    elif user_input == "bio":
        slow_print(ghostbot_bio)

    elif user_input == "scan":
        slow_print("🌀 Scanning your aura and Wi-Fi signals...")
        time.sleep(1.5)
        story = random.choice(ghost_stories)
        slow_print(f"👻 {story}")

    elif user_input == "cleanse":
        slow_print("🧹 Initializing ghost cleansing protocol...")
        time.sleep(1.5)
        slow_print(random.choice(cleansing_methods))

    elif user_input == "summon":
        slow_print("🪞  Opening a ghost portal...")
        time.sleep(1.5)
        slow_print(random.choice(summon_methods))

    else:
        slow_print("🪦 GhostBot doesn’t understand that. Try typing one of the listed commands! bio/scan/cleanse/summon/bye")

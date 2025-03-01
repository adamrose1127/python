import time

# Dictionary of predefined responses
responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi there!",
    "bye": "Goodbye, see you later!",
    "how are you": "I'm great, thanks for asking!",
    "what’s up": "Not much, just here to chat!",
    "lol": "Haha, that's funny!",
    "rofl": "Wow, that must have been hilarious!",
    "lmk": "Sure, I'll let you know as soon as I find out!",
    "tbh": "To be honest, I feel the same way.",
    "idk": "No worries, we can figure it out together!",
    "smh": "I know, right? Some things just don't make sense.",
    "btw": "Oh, by the way, thanks for mentioning that!",
    "imo": "In my opinion, that's a great point!",
    "nvm": "Okay, no problem! Let me know if you need anything else.",
    "wyd": "Not much, just here to help you out!",
    "ily": "Aww, I appreciate that! You're awesome too!",
    "omg": "I know, right? That's crazy!",
    "ttyl": "Alright, talk to you later!",
    "brb": "Sure, take your time! I'll be here.",
    "gtg": "Okay, catch you later!",
    "idc": "Fair enough, sometimes it's better not to worry about it.",
    "fyi": "Thanks for the heads-up!",
    "jk": "Haha, you got me for a second!",
    "np": "No problem at all, happy to help!",
    "thx": "You're welcome! Anytime.",
    "yw": "No problem, glad I could help!",
    "gg": "Good game! You did great!",
    "glhf": "Good luck, have fun! You've got this!",
    "afk": "No worries, I'll be here when you get back!",
    "irl": "That sounds like a real-life adventure!",
    "ama": "Ask me anything, I'm here to help!",
    "tmi": "Haha, maybe a little too much information!",
    "hmu": "Sure, hit me up anytime!",
    "wdym": "What do you mean? Can you explain a bit more?",
    "rn": "Right now? Got it, I'm on it!",
    "fr": "For real? That's wild!",
    "lowkey": "Lowkey, I feel the same way.",
    "highkey": "Highkey, that's so true!",
    "sksksk": "Haha, I love the energy!",
    "periodt": "Periodt. No further explanation needed!",
    "slay": "Slay! You're killing it!",
    "bet": "Bet. I'm with you on that.",
    "cap": "No cap, that's the truth!",
    "sus": "That does seem a little sus...",
    "yeet": "Yeet! Let's do this!",
    "oof": "Oof, that's rough. Hang in there!",
    "simp": "Haha, no simping here!",
    "vibe": "I'm totally vibing with that!",
    "clout": "Chasing clout, huh? I see you!",
    "stan": "I stan that! You're a legend!",
    "ghost": "Did they ghost you? That's not cool.",
    "flex": "Flex on them! You deserve it!",
    "snack": "You're a whole snack! Looking good!",
    "tea": "Spill the tea! I'm all ears.",
    "woke": "Stay woke! You're ahead of the game.",
    "cancel": "Cancel culture is real. Be careful!",
    "ship": "I ship it! They're perfect together.",
    "mood": "Big mood. I feel that.",
    "receipts": "Where are the receipts? Proof or it didn't happen!",
    "clapback": "That clapback was fire! Well done.",
    "gucci": "Everything's Gucci! No worries.",
    "lit": "That's lit! Sounds like a great time.",
    "salty": "Don't be salty! It's all good.",
    "shade": "Throwing shade, huh? I see you.",
    "savage": "That was savage! I love it.",
    "wack": "That's wack. I don't agree with that.",
    "yikes": "Yikes! That's not good.",
    "zodiac": "What's your zodiac sign? I'm curious!",
    "astrology": "I love astrology! What's your sign?",
    "manifest": "Manifest it! You got this.",
    "vibe check": "Vibe check passed! You're good.",
    "huh": "let me think lol",  # Response to "huh"
    "unknown": "fab"  # Fallback response
}

# Function to read the latest text from input.txt
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines[-1].strip() if lines else ""
    except FileNotFoundError:
        return ""

# Function to write the AI's response to output.txt
def write_response(file_path, response):
    with open(file_path, 'a') as file:
        file.write(response + "\n")

# Main loop to monitor and respond
input_file = "input.txt"
output_file = "output.txt"

print("AI Agent is running. Write to input.txt to talk to me!")
last_input = ""

while True:
    current_input = read_input(input_file)
    if current_input and current_input != last_input:  # Only respond to new input
        last_input = current_input
        # Get the response or fallback to "fab" if the input is not recognized
        response = responses.get(current_input.lower(), responses["unknown"])
        print(f"You said: {current_input}")
        print(f"AI says: {response}")
        write_response(output_file, response)
    time.sleep(1)  # Wait 1 second before checking again

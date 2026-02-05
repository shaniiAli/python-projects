emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "sad": "😢",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍔",
}

message = input("Enter your message :")

updated_words = []

for word in message.split():
    cleaned_word = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned_word,"")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("Updated message:", updated_message)
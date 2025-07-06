from datetime import datetime

# Simple sentiment keywords
positive_words = ['happy', 'good', 'great', 'awesome', 'nice', 'love']
negative_words = ['sad', 'bad', 'terrible', 'hate', 'angry', 'upset']

# Get input from user
entry = input("How was your day? Write in one line:\n")

# Sentiment logic
entry_lower = entry.lower()
score = 0
for word in positive_words:
    if word in entry_lower:
        score += 1
for word in negative_words:
    if word in entry_lower:
        score -= 1

# Emoji + Quote suggestion
if score > 0:
    mood = "😊 Positive"
    quote = "Keep smiling, you're doing great!"
elif score < 0:
    mood = "😞 Negative"
    quote = "It’s okay to have a bad day. Tomorrow is a new chance."
else:
    mood = "😐 Neutral"
    quote = "Stay steady, breathe deeply."

# ✅ Save to file with UTF-8 to support emoji
with open("mood_journal.txt", "a", encoding="utf-8") as file:
    file.write(f"{datetime.now()} - Mood: {mood} | Entry: {entry}\n")

# Output
print(f"\nDetected Mood: {mood}")
print(f"Quote for you: \"{quote}\"")

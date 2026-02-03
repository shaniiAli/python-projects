import textwrap
name = input('Enter your name: ').strip()
profession = input('Enter your profession: ').strip()
passion = input('Enter your passion: ').strip()
emoji = input('Enter your favorite emoji: ').strip()
website = input('Enter your website URL: ').strip()

print("\nChoose your style : ")
print("1. Simple Lines")
print("2. Vertical Flair")
print("3. Emoji Sandwitch")

style = input('Enter 1,2 or 3 :').strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion}\n {website}" 
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"
    
bio = generate_bio(style)
     
print("\nHere is your generated bio:\n")
print("*" * 40)
print(textwrap.dedent(bio))
print("*" * 40)

save = input("Do you want to save this bio to a file? (yes/no): ").strip().lower()
if save == "yes":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(bio)
    print(f"Bio saved to {filename}")
else:
    print("Bio not saved.")
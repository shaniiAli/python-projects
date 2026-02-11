def friendship_score(name1,name2):
    name1,name2 = name1.lower(),name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')
    
    score += len(shared_letters) * 5
    score += len(shared_letters & vowels) * 10
    
    return min(score,100)

def run_friendship_calculator():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    score = friendship_score(name1, name2)
    if score >= 80:
        print(f"{name1} and {name2} are best friends! (Score: {score})")
    elif score >= 50:
        print(f"{name1} and {name2} are good friends. (Score: {score})")
    else:
        print(f"{name1} and {name2} are just acquaintances. (Score: {score})")

run_friendship_calculator()
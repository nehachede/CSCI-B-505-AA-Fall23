from collections import Counter

def wordle(guess, secretWord):
    ans = 'B' * len(guess)
    
    # print(guess, secretWord)
    
    h1, h2 = Counter(guess), Counter(secretWord)
    
    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            ans = ans[:i]+'G'+ans[i+1:]
            h1[guess[i]] -= 1
            h2[secretWord[i]] -= 1
    
    for i in range(len(guess)):
        if guess[i] != secretWord[i] and h2[guess[i]] > 0:
            ans = ans[:i] + 'Y' + ans[i+1:]
            h1[guess[i]] -= 1
            h2[secretWord[i]] -= 1

    print(h1, h2)
    return ans

print(wordle("RAMPS", "PROPS"))  # Output: "YBBGG"
print(wordle("APPLE", "PEARS"))  # Output: "YYBBY"
print(wordle("AAAAP", "PEARS"))  # Output: "BBGBY"
#defining values based on Grade 1 Braille
alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇',
 '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
puntuation = [',',';',':','.','?','!', ';','(',')', '/', '-']
puntuationBraille = ['⠂','⠆','⠒','⠲','⠦','⠖','⠐⠣','⠐⠜','⠸⠌','⠤']
character = ['&','*','@','©','®','™','°',]
characterBraille = ['⠈⠯','⠐⠔','⠈⠁','⠘⠉','⠘⠗','⠘⠞','⠘⠚',]

def transtalteToBraille(text):
    inputString = ' '
    if len(text) > 0 : 
        for n in text.lower():
            if n in alphabet:
                inputString += alphaBraille[alphabet.index(n)]
            elif n in nums:
                inputString += numBraille[nums.index(n)]
            elif n in puntuation:
                inputString += puntuationBraille[puntuation.index(n)]
            elif n in character:
                inputString += characterBraille[character.index(n)]
        #print(inputString)
        return inputString

def main():
    string = input("Translate to braille: ")
    print(transtalteToBraille(string))

main()
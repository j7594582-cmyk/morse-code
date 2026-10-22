morse_code = {"A": ".-", 
              "B": "-...", 
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----"}

rev = {" .-": "A",
       " -...": "B",
       " -.-.": "C",
       " -..": "D",
       ".": "E",
       " ..-.": "F",
       " --.": "G", 
       " ....": "H",
       " ..": "I",
       " .---": "J",
       " -.-": "K",
       " .-..": "L",
       " --": "M",
       " -.": "N",
       " ---": "O",
       " .--.": "P",
       " --.-": "Q",
       " .-.": "R",
       " ...": "S",
       "-": "T",
       " ..-": "U",
       " ...-": "V",
       " .--": "W",
       " -..-": "X",
       " -.--": "Y",
       " --..": "Z",
       " .----": "1",
       " ..---": "2",
       " ...--": "3",
       " ....-": "4",
       " .....": "5",
       " -....": "6",
       " --...": "7",
       " ---..": "8",
       " ----.": "9",
       " -----": "0"}

def encode(text):
    words = text.upper().split(" ")
    return " ".join(" ".join((morse_code.get(c, "")) for c in w) for w in words)

def decode(text):
    words = text.split(" ")
    return " ".join("".join(rev.get(s, "") for s in w) for w in words)

while True: 
    choice = input("""
    choose one:
    encode: 1.
    decode: 2.
    exit:   3. 
    choice: """) 
    if choice == "1":
        print(f"encoded morse code: {encode(input("text: "))}")
        input("press enter to go again:")
    elif choice == "2":
        print(f"decoded text: {decode(input("morse code: "))}")
        input("press enter to go again:")
    elif choice =="3":
        print("have a nice day")
        break
    else:
        print("INVALID. try again")
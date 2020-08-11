#Exercise: Frame some text
def frame_code(words):
    size_of_word = len(max(words, key=len))
    print('*' * (size_of_word + 4))
    for word in words:
        a = word
        b = size_of_word
        print(f'* {a:<{b}} *')
    print('*' * (size_of_word + 4))

if __name__ == "__main__":
    text = input("Enter these words(write good code every day) Input: ")
    frame_code(text.split(" "))


def main():
    text=input("how are you doing today buddy? ")
    text=convert(text)
    print(text)

def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")

    return text
main()

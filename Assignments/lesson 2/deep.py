question=input("What is the answer to the Great Question Of Life, the Universe and Everything? ").strip().lower()
match question:
    case "42" | "forty two" |"forty-two":
       print("Yes")
    case _:
       print("No")


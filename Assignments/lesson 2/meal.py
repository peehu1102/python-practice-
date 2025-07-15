def main():
    que=input("What is the time? ").strip()
    if 7<= convert(que)<= 8:
         print("Breakfast time")

    elif 12<=convert(que)<=13:
         print("Lunch time")

    elif 18 <= convert(que) <= 19:
         print("Dinner time")

def convert(que):
    x,y= que.split(":")
    return int(x) + int(y)/60

if __name__ == "__main__":
     main()

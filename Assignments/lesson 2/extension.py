que=input("file name? ").lower().strip()
if que.endswith (".gif") :
     print("image/gif")
elif que.endswith (".jpg"):
    print("image/jpeg")
elif que.endswith (".jpeg"):
    print("image/jpeg")
elif que.endswith (".png") :
    print("image/png")
elif que.endswith (".pdf") :
    print("application/pdf")
elif que.endswith (".txt") :
    print("text/plain")
elif que.endswith (".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

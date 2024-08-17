# 7. Write a program to find out whether a given post is talking about “Gaurav” or not.


post = input("Enter Your Post: ")

if("Gaurav".lower() in post.lower()):
    print("Gaurav is present in the post.")      
else:
    print("Gaurav is not present in the post.")





print("Hello Dog Lovers!")
print("Select the breed to know more about it")
print("1. German Shepherd")
print("2. Bulldog")
print("3. Poodle")
print("4. Golden Retriever")
print("5. Beagle")
x = int(input("Enter Dog of your choice:"))
if x == 1 :
    print("German Shepherds are intelligent, loyal, and versatile working dogs. They excel in roles like police, military, and service work due to their strength and trainability. With proper care and training, they make loving and protective family companions.")
elif x == 2 :
    print("Bulldogs are muscular, wrinkled dogs known for their calm and affectionate nature. They are loyal companions with a distinctive pushed-in nose and a sturdy build. Despite their tough appearance, they are gentle, friendly, and great with families.")
elif x == 3 :
    print("Poodles are intelligent, elegant, and highly trainable dogs known for their curly, hypoallergenic coats. They come in three sizes—Toy, Miniature, and Standard—each with a playful and affectionate personality. Poodles excel in obedience, agility, and make wonderful family pets.")
elif x == 4 :
    print("Golden Retrievers are friendly, intelligent, and loyal dogs known for their beautiful golden coats. They are great family pets, excelling in obedience, therapy work, and outdoor activities. Their affectionate nature and eagerness to please make them wonderful companions.")
elif x == 5 :
    print("Beagles are friendly, curious, and energetic dogs with an excellent sense of smell. They are affectionate and great with families, known for their playful and outgoing nature. Beagles love exploring and require regular exercise to stay happy and healthy.")

print("-"*30)


for x in range (1,6):
    for y in range (1,x+1):
        print(y, end = " ")
    print()

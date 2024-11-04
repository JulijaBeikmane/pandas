class User:
    # pass
    #inicializē atribūtus
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("Jauns lietotājs ir izveidots")

    def follow(self, user):
        self.following += 1 #palielinās skaits, kam mēs sekojam
        user.followers += 1 #palielinās sekotāju skaits

user_1 = User("001", "Šerloks") 
#pievieno atribūts
# user_1.id = "001"
# user_1.username = "Šerloks"

# print(user_1.username)
# print(user_1.id)
# print(user_1.followers)


user_2 = User("002","Lūsija")
# user_2.id = "002"
# user_2.username = "Lūsija"
# print(user_2.username)
# print(user_2.id)

user_3 = User("003","Watsons")

user_1.follow(user_2)
user_2.follow(user_1)
user_3.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)

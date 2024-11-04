class Kino:
    def __init__(self, bilete, filma):
        self.bilete = bilete
        self.film = filma
        self.people = 0
      
    def count(self, user):
        self.people += 1

user_1 = Kino("001", "Šerloks") 
user_2 = Kino("002","Lūsija")
user_3 = Kino("003","Watsons")

kino_1 = Kino("Venom 3")
kino_2 = Kino("Batman")
kino_3 = Kino("Iron man")

 

class Bateau:
    def __init__(self, nom, vitesse):
        self.nom = nom
        self.vitesse = vitesse
        self.distance_parcourue = 0

    def avancer(self):
        self.distance_parcourue += self.vitesse / 120 

    def afficher_position(self):
        return f"# {self.nom},{int(self.distance_parcourue * 500)}"

class Bateau2x(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

    def type_bateau(self):
        return "2x"

class BateauSkiff(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

    def type_bateau(self):
        return "1x"

class Course:
    def __init__(self, type_course):
        self.type_course = type_course
        self.bateaux = []
        self.terminee = False

    def ajout_bateau_ligne_depart(self, bateau):
        if bateau.type_bateau() == self.type_course:
            self.bateaux.append(bateau)
        else:
            print(f"Le bateau {bateau.nom} n'est pas du bon type ({self.type_course}).")

    def depart(self):
        print("La course commence!")

    def en_cours(self):
        return not self.terminee

    def next_loop(self):
        for bateau in self.bateaux:
            bateau.avancer()
            if bateau.distance_parcourue >= 2: 
                self.terminee = True

    def affiche_positions(self):
        return "\n".join([bateau.afficher_position() for bateau in self.bateaux])

    def vainqueur(self):
        vainqueur = max(self.bateaux, key=lambda x: x.distance_parcourue)
        return f"# Le bateau le plus rapide: {vainqueur.nom}"

if __name__ == "__main__":
    course_cadets = Course('2x')
    bateau_1_2x = Bateau2x('mickey', 62)
    bateau_2_2x = Bateau2x('minnie', 70)
    bateau_3_skiff = BateauSkiff('picsou', 15)

    course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)

    course_cadets.depart()

    with open("result.txt", "a") as f:
        while course_cadets.en_cours():
            course_cadets.next_loop()
            positions = course_cadets.affiche_positions()
            print(positions, flush=True)
            f.write(positions + "\n")

        print(course_cadets.vainqueur())


import random

class RowingBoat:
    def __init__(self, boat_name, average_speed):
        self.boat_name = boat_name
        self.average_speed = average_speed
        self.distance_covered = 0

    def row(self):
        self.distance_covered += self.average_speed / 2 

    def distance(self):
        return self.distance_covered

    def name(self):
        return self.boat_name


class DoubleScullBoat(RowingBoat):
    def __init__(self, boat_name, average_speed):
        super().__init__(boat_name, average_speed)


class SingleScullBoat(RowingBoat):
    def __init__(self, boat_name, average_speed):
        super().__init__(boat_name, average_speed)


class RowingRace:
    def __init__(self, boat_type):
        self.boat_type = boat_type
        self.boats = []

    def add_boat_to_start_line(self, boat):
        if isinstance(boat, RowingBoat) and type(boat).__name__ == self.boat_type:
            self.boats.append(boat)
            return True
        else:
            print("Impossible d'ajouter des navires")
            return False

    def commence(self):
        print("C'est parti")

    def in_progress(self):
        return any(boat.distance() < 2000 for boat in self.boats)

    def next_turn(self):
        for boat in self.boats:
            boat.row()

    def display_positions(self):
        positions = [f"{boat.name()},{int(boat.distance())}" for boat in self.boats]
        return '\n'.join(positions)

    def winner(self):
        random.shuffle(self.boats)
        fastest_boat = max(self.boats, key=lambda b: b.average_speed)
        return fastest_boat.name()


cadet_race = RowingRace('DoubleScullBoat')
boat_1_2x = DoubleScullBoat('Mickey', 62)
boat_2_2x = DoubleScullBoat('Minnie', 70)
boat_3_skiff = SingleScullBoat('Scrooge', 120)

cadet_race.add_boat_to_start_line(boat_1_2x)
cadet_race.add_boat_to_start_line(boat_2_2x)
cadet_race.add_boat_to_start_line(boat_3_skiff)

cadet_race.commence()

while cadet_race.in_progress():
    cadet_race.next_turn()
    print(cadet_race.display_positions())

print("Le gagnant est :", cadet_race.winner())


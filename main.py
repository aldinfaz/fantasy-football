teams = []
team_names = []

players = []
player_names = []

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    
    def add_players(self, player):
        if player.name not in self.players:
            self.players.append(player)
            print(f'{player.name} added!')
        else:
            print(f'{player.name} already in team.')
    
    def total_team_szn(self):
        total = 0
        for i in self.players:
            total += i.total
        return total
    
    #not working
    '''def view(self):
        for i in self.players:
            print(f'{i.name}:\nWeekly Points: {i.points}\nSeason Points: {i.total_player_szn}')'''

class Player:
    def __init__(self, name):
        self.name = name
        self.points = []

    #add points for the week
    def add_points(self, points):
        self.points.append(float(points))
    
    #total points
    def total_player_szn(self):
        sum = 0
        for i in self.points:
            sum += float(i)
        
        return sum
    
def main():
    print("Welcome to Aldin's Fantasy Football!")
    choice = int(input("To go to the team menu, press 1.\nTo go to the player menu, press 2."))
    print()

    if choice == 1:
        team_menu()
    elif choice == 2:
        player_menu()

def team_menu():
    print("Welcome to the team menu!")

    while True:
        choice = int(input("To create a new team, press 1.\nTo add players to a team, press 2.\nTo view a team's total seasonal points, press 3."))
        print() 

        if choice == 1:
            t_name = input("Team name: ")
            if t_name not in team_names:
                team = Team(t_name)
                teams.append(team)
                team_names.append(t_name)
                print(f'Welcome to the league, {t_name}!')
            else:
                print("Team name already exists.")
        
        elif choice == 2:
            team = input("Which team would you like to modify: ")
            if team not in team_names:
                print("Team does not exist.")
            else: 
                for i in teams:
                    if i.name == team:
                        p = input("Which player are you adding: ")
                        if p not in player_names:
                            print("Player does not exist.")
                        else:
                            for j in players:
                                if j.name == p:
                                    i.add_players(j)
        elif choice == 3:
            team = input("Team: ")
            if team not in team_names:
                print("Team does not exist.")
            else: 
                for i in teams:
                    if i.name == team:
                        total = i.total_team_szn
                        print(f'{team}\'s total season points: {total}')
        """
        elif choice == 4:
            team = input("Team: ")
            if team not in team_names:
                print("Team does not exist.")
            else: 
                for i in teams:
                    if i.name == team:
                        i.view
                    """

def player_menu():
    print("Welcome to the player menu!")

    while True:
        choice = int(input("To create a new player, press 1.\nTo add weekly points to a player, press 2.\nTo view a players total points for the season, press 3.\nTo go back to main menu, press any other number."))
        print()

        #creating player
        if choice == 1:
            p_name = input("Player name: ")
            if p_name not in player_names:
                player = Player(p_name)
                players.append(player)
                player_names.append(p_name)
                print(f'{p_name} succesfully created')
            else:
                print("Player already exists.")
        
        #adding points to player
        elif choice == 2:
            p = input("Player: ")
            if p not in player_names:
                print("Player does not exist.")
            else:
                for i in players:
                    if p == i.name:
                        pts = float(input("Points for the week: "))
                        i.add_points(pts)
                        print(f'{pts} points added to {p}')
        
        #view total points
        elif choice == 3:
            p = input("Player: ")
            if p not in player_names:
                print("Player does not exist.")
            else:
                for i in players:
                    if p == i.name:
                        print(f'{p}\'s total points: {i.total_player_szn}')
        #to leave
        else:
            main()

#run test
main()
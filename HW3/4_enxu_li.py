import os,csv

class Namebook(object):
    def __init__(self):
        self.player_dict = dict()

    def manually_add_player(self,id,player):
        self.player_dict[id] = player

    def read_csv_dict(filename):
        with open(filename, 'r') as file_handle:
            reader = csv.DictReader(file_handle, delimiter=",")
            csv_list = list(reader)
        return csv_list

    def fill_dict(self):
        data_list = []
        dirs = os.listdir('../')
        count = 0
        for filename in dirs:
            if os.path.splitext(filename)[1] == ".csv":
                print(filename,'is loaded.')
                count += 1
                data_list += Namebook.read_csv_dict(filename)
        print(count,'file(s) in total is loaded.')
        for data in data_list:
            if data['espn_player_id'] in self.player_dict:
                game = Game(data['espn_game_id'],data['won_lost'],data['home_away'],data['total_QBR'],data['action_plays'])
                self.player_dict[data['espn_player_id']].add_game(game)
            else:
                player = Player(data['first_name']+' '+data['last_name'],data['espn_player_id'],data['team_name'])
                game = Game(data['espn_game_id'],data['won_lost'],data['home_away'],data['total_QBR'],data['action_plays'])
                player.add_game(game)
                self.player_dict[data['espn_player_id']] = player

    def get_solution(self):
        #print(self.player_dict['237729'].name,"with",self.player_dict['237729'].highest_action_plays)
        player_id_highest_QBR_in_loss = max(self.player_dict, key = lambda id: self.player_dict[id].highest_QBR_in_loss)
        player_id_lowest_QBR_in_win = min(self.player_dict, key = lambda id: self.player_dict[id].lowest_QBR_in_win)
        player_id_highest_action_plays = max(self.player_dict, key = lambda id: self.player_dict[id].highest_action_plays)
        player_id_highest_average_QBR = max(self.player_dict, key = lambda id: self.player_dict[id].average_QBR())

        tmpdict_without_None = {id:player for id,player in self.player_dict.items() if player.one_game_data() is not None}
        player_id_highest_QBR_in_one = max(tmpdict_without_None, key = lambda id: tmpdict_without_None[id].one_game_data())
        player_id_lowest_QBR_in_one = min(tmpdict_without_None, key = lambda id: tmpdict_without_None[id].one_game_data())
        print('Note here the id of game is originally XXXXXXXXXX.0, I don\'t know where the .0 comes from because the type of it is str from the very begining.')
        print('I cannot find a way to fix it and I suspect that this is becuase something in the csv.DictReader() and the csv files themselves.')
        print('So here I cut out two chars in the end of the string to make if looks like how it looks in the csv.')
        print('Solution:')
        print('Player',self.player_dict[player_id_highest_QBR_in_loss].name,
        'had the highest total_QBR of', self.player_dict[player_id_highest_QBR_in_loss].highest_QBR_in_loss,
        'in a lost game',self.player_dict[player_id_highest_QBR_in_loss].game_loss+'.')
        print('Player',self.player_dict[player_id_lowest_QBR_in_win].name,
        'had the lowest total_QBR of', self.player_dict[player_id_lowest_QBR_in_win].lowest_QBR_in_win,
        'in a win game',self.player_dict[player_id_lowest_QBR_in_win].game_win+'.')
        print('Player',self.player_dict[player_id_highest_action_plays].name,
        'had the highest number of action_plays of', self.player_dict[player_id_highest_action_plays].highest_action_plays,
        'in a game',self.player_dict[player_id_highest_action_plays].game_high_act+'.')
        print('Player',self.player_dict[player_id_highest_average_QBR].name,
        'had the highest average total_QBR of', self.player_dict[player_id_highest_average_QBR].average_QBR())
        print('Player',self.player_dict[player_id_highest_QBR_in_one].name,
        'had the highest total_QBR of', self.player_dict[player_id_highest_QBR_in_one].one_game_data(),
        'in only one game',self.player_dict[player_id_highest_QBR_in_one].game_high_act+'.')
        print('Player',self.player_dict[player_id_lowest_QBR_in_one].name,
        'had the lowest total_QBR of', self.player_dict[player_id_lowest_QBR_in_one].one_game_data(),
        'in only one game',self.player_dict[player_id_lowest_QBR_in_one].game_high_act+'.')




class Player(object):
    highest_action_plays = float('-inf')
    highest_QBR_in_loss = float('-inf')
    lowest_QBR_in_win = float('inf')
    game_loss = None
    game_win = None
    game_high_act = None

    def __init__(self,name,id,team):
        self.name = name
        self.id = id
        self.team = team
        self.game_list = []
    def add_game(self,game):
        self.game_list.append(game)
        #find the highest_QBR_in_loss and lowest_QBR_in_win
        #and highest_action_plays when add the game
        #which can avoid sorting and the time complexity can be O(n)
        if game.action_plays> self.highest_action_plays:
            self.game_high_act = game.id
            self.highest_action_plays = game.action_plays

        if game.won_lost == 'L' and game.total_QBR > self.highest_QBR_in_loss:
            self.game_loss = game.id
            self.highest_QBR_in_loss = game.total_QBR

        if game.won_lost == 'W' and game.total_QBR < self.lowest_QBR_in_win:
            self.game_win = game.id
            self.lowest_QBR_in_win = game.total_QBR

    def average_QBR(self):
        return sum([ game.total_QBR for game in self.game_list]) / len(self.game_list)

    def one_game_data(self):
        if len(self.game_list) == 1:
            return self.game_list[0].total_QBR
        else:
            return None


class Game(object):
    def __init__(self,id,won_lost,home_away,total_QBR,action_plays):
        self.id = id[:len(id)-2]
        self.won_lost = won_lost
        self.home_away = home_away
        self.total_QBR = float(total_QBR)
        self.action_plays = int(action_plays)

def main():
    namebook = Namebook()
    namebook.fill_dict()
    namebook.get_solution()

if __name__ == '__main__':
    main()

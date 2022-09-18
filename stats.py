from cgitb import reset


class Stats():
    #відслідковує статистику
    def __init__(self):  
        self.reset_stats() 
        self.run_game = True
        with open("hascor.txt", "r") as f: 
            
            self.high_score = int(f.readline())



    def reset_stats(self):  #статистика, що змінюється під час гри
        self.ships_left = 2  
        self.score = 0

       
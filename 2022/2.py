with open('2022/puzzle_inputs/2.txt') as file:
    strInput = file.read()

scoring = {'A X':{'opp':4,'me':4,'outcome':'draw'},
          'B Y':{'opp':5,'me':5,'outcome':'draw'},
          'C Z':{'opp':6,'me':6,'outcome':'draw'},
          'A Y':{'opp':1,'me':8,'outcome':'me'},
          'A Z':{'opp':7,'me':3,'outcome':'opp'},
          'B X':{'opp':8,'me':1,'outcome':'opp'},
          'B Z':{'opp':2,'me':9,'outcome':'me'},
          'C X':{'opp':3,'me':7,'outcome':'me'},
          'C Y':{'opp':9,'me':2,'outcome':'opp'}}

# 1 - 12458
print(sum([scoring[x]['me'] for x in strInput.split('\n')[:-1]]))

scoring2 = {'A X':{'opp':7,'me':3,'outcome':'opp'},
          'B Y':{'opp':5,'me':5,'outcome':'draw'},
          'C Z':{'opp':3,'me':7,'outcome':'me'},
          'A Y':{'opp':4,'me':4,'outcome':'draw'},
          'A Z':{'opp':1,'me':8,'outcome':'me'},
          'B X':{'opp':8,'me':1,'outcome':'opp'},
          'B Z':{'opp':2,'me':9,'outcome':'me'},
          'C X':{'opp':9,'me':2,'outcome':'opp'},
          'C Y':{'opp':6,'me':6,'outcome':'draw'}}

# 2 12683
print(sum([scoring2[x]['me'] for x in strInput.split('\n')[:-1]]))

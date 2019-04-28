#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:11:00 2019

@author: john
"""

def main():
    ctemps = [0, 12, 34, 100]
    
    temp_dict = {t: (t*9/5) + 32 for t in ctemps if t < 100}
    print(temp_dict)
    print(temp_dict[12])
    
    
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)
    # Can't this be done by .update()?

    new_team = {}
    new_team.update(team1)
    new_team.update(team2)
    print(new_team)

if __name__ == "__main__":
    main()

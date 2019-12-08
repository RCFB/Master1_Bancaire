#!/usr/local/bin/python3.7
#-*-coding:Utf-8 -*
"""
def user_connected(user_id):
  for user in static_users():
        if user['id'] == user_id:
            return user
        else:
          user = {'id': 0,'nom': 'Anonimous'}
          return user
"""
"""
def comptes_user(user_id):
    for comptesuser in static_comptes():
        if comptesuser['user_id'] == user_id:
            return comptesuser"""

def compte(compte_id):
    for compte in static_comptes():
        if compte['id'] == compte_id:
            return compte


def comptes_row( user_id):
  banque_id = static_banques['id']
  comptesuser= compte(compte_id)

  n_won_match_count = sum (team_wins_match(team_id, match) for match in matches)
  n_lost_match_count = sum (team_loses_match(team_id, match) for match in matches)
  n_draw_match_count = sum (team_makes_a_draw(team_id, match) for match in matches)
  n_match_played_count = n_won_match_count + n_lost_match_count + n_draw_match_count
  n_goals_for = sum (goals_for(team_id, match) for match in matches)
  n_goals_against = sum (goals_against(team_id, match) for match in matches)
  n_goal_difference = n_goals_for - n_goals_against
  n_points = 3*n_won_match_count + n_draw_match_count
  return {'comptes' : team,
  'stats': {
    'match_played_count': n_match_played_count,
    'points':             n_points,
    'won_match_count':    n_won_match_count, 
    'lost_match_count':   n_lost_match_count, 
    'draw_match_count':   n_draw_match_count, 
    'goals_for':          n_goals_for, 
    'goals_against':      n_goals_against, 
    'goal_difference':    n_goal_difference}}

"""
def ranking_row(team, matches):
  team_id = team['id']
  n_won_match_count = sum (team_wins_match(team_id, match) for match in matches)
  n_lost_match_count = sum (team_loses_match(team_id, match) for match in matches)
  n_draw_match_count = sum (team_makes_a_draw(team_id, match) for match in matches)
  n_match_played_count = n_won_match_count + n_lost_match_count + n_draw_match_count
  n_goals_for = sum (goals_for(team_id, match) for match in matches)
  n_goals_against = sum (goals_against(team_id, match) for match in matches)
  n_goal_difference = n_goals_for - n_goals_against
  n_points = 3*n_won_match_count + n_draw_match_count
  return {'team' : team,
  'stats': {
    'match_played_count': n_match_played_count,
    'points':             n_points,
    'won_match_count':    n_won_match_count, 
    'lost_match_count':   n_lost_match_count, 
    'draw_match_count':   n_draw_match_count, 
    'goals_for':          n_goals_for, 
    'goals_against':      n_goals_against, 
    'goal_difference':    n_goal_difference}}

def compare_key(row):
  return (row['stats']['points'], row['stats']['goal_difference'])

def ranking(teams, matches):
  rows = [ranking_row(team, matches) for team in teams]
  return sorted(rows, key=compare_key, reverse=True)"""


if __name__ == "__main__":
  from compte_static_model import static_users, static_comptes
  from pprint import pprint
  #pprint(ranking(static_users(), static_comptes()))
  
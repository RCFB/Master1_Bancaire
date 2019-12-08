#!/usr/local/bin/python3.7
#-*-coding:Utf-8 -*
import random
from datetime import datetime, timedelta
from collections import deque


def static_banques():
    return [{'id': 1, 'name': 'CIC'},
            {'id': 2, 'name': 'LCL'},
            {'id': 3, 'name': 'La Poste'},
            {'id': 4, 'name': 'CA'},
            {'id': 5, 'name': 'SG'},
            {'id': 6, 'name': 'BPCE'},
            {'id': 7, 'name': 'M.Maurel'},
            {'id': 8, 'name': 'HSBC'},
            {'id': 9, 'name': 'BNP'},
            {'id': 10, 'name': 'ING Direct'}]

def static_mouvements():
    return [{'id': 1, 'libelle': 'Credit Auto', 'tiers': 'TotoTiers'},
            {'id': 2, 'libelle':  'Credit Moto', 'tiers': 'TitiTiers'},
            {'id': 3, 'libelle':  'Taxe habitation', 'tiers': 'Tresor Public'},
            {'id': 4, 'libelle': 'Restaurant', 'tiers': 'Mcdo'},
            {'id': 5, 'libelle': 'Salaire', 'tiers': 'Circet'}]

"""def comptes_test(compte_id):
    for compte in comptes():
        if team['id'] == team_id:
            return team"""

def static_m_payement():
    return [{'id': 1, 'name': 'Especes'},
            {'id': 2, 'name': 'CB'},
            {'id': 3, 'name': 'Cheque'},
            {'id': 4, 'name': 'Virement'},
            {'id': 5, 'name': 'Prelevement'},
            {'id': 6, 'name': 'Paypal'}]

def static_categories():
    return [{'id': 1, 'name': 'Salaire'},
            {'id': 2, 'name': 'Impots'},
            {'id': 3, 'name': 'Courses'},
            {'id': 4, 'name': 'Credits'},
            {'id': 5, 'name': 'Telephone'},
            {'id': 6, 'name': 'Assurances'},
            {'id': 7, 'name': 'Medical'}]

def static_libelle():
    return [{'id': 1, 'name': 'Essence'},
            {'id': 2, 'name': 'Gasoil'},
            {'id': 3, 'name': 'Salaire'},
            {'id': 4, 'name': 'Credits'},
            {'id': 5, 'name': 'Telephone'},
            {'id': 6, 'name': 'Assurances'}]


def static_comptes():
    return [{'id': 1, 'numero': '10000', 'banque_id': 1, 'definition': 'compte courrant', 'user_id': 4, 'mdepart': 300},
            {'id': 2, 'numero': '7700', 'banque_id': 2, 'definition': 'compte courrant', 'user_id': 4, 'mdepart': 1000},
            {'id': 3, 'numero': '7880', 'banque_id': 2, 'definition': 'compte courrant Credits', 'user_id': 4, 'mdepart': 100},
            {'id': 4, 'numero': '300', 'banque_id': 5, 'definition': 'compte epargne', 'user_id': 1, 'mdepart': 3000},
            {'id': 5, 'numero': '10000', 'banque_id': 4, 'definition': 'compte courrant', 'user_id': 1, 'mdepart': 930}]


def static_users():
    return [{'id': 0, 'nom': 'Anonimous', 'prenom': 'Anonimous', 'mail': '', 'pass': 'AnonimousInterdit','genre':''},
            {'id': 1, 'nom': 'Tata', 'prenom': 'tata', 'mail': 'tata@gmail.com', 'pass': 'Tata','genre':'Feminin'},
            {'id': 2, 'nom': 'Tete', 'prenom': 'tete', 'mail': 'tete@yahoo.fr', 'pass': 'Tete','genre':'Masculin'},
            {'id': 3, 'nom': 'Titi', 'prenom': 'titi', 'mail': 'titi@gmail.com', 'pass': 'Titi','genre':'Feminin'},
            {'id': 4, 'nom': 'Toto', 'prenom': 'toto', 'mail': 'toto@yahoo.fr', 'pass': 'Toto','genre':'Masculin'},
            {'id': 5, 'nom': 'Tutu', 'prenom': 'tutu', 'mail': 'tutu@gmail.com', 'pass': 'Tutu','genre':'Masculin'}]

def utilisateur_et_comptes():
    return [{'id': 0, 'infos': {'nom': 'Anonimous', 'prenom': 'Anonimous', 'mail': '', 'pass': 'AnonimousInterdit','genre':''},
                        'comptes':[{'id': 1, 'numero': 00000, 'banque_id': 0, 'definition': '', 'mdepart': 000 }]},
            {'id': 1, 'infos': {'nom': 'Tata', 'prenom': 'Tata', 'mail': 'tata@gmail.com', 'pass': 'Tata','genre':'Feminin'},
                        'comptes':[{'id': 1, 'numero': 00000, 'banque_id': 0, 'definition': '', 'mdepart': 000 }]},
            {'id': 2, 'infos':{'nom': 'Tete', 'prenom': 'Tete', 'mail': 'tete@yahoo.fr', 'pass': 'Tete','genre':'Masculin'},
                        'comptes':[{'id': 1, 'numero': 00000, 'banque_id': 0, 'definition': '', 'mdepart': 000 }]},
            {'id': 3, 'infos':{'nom': 'Titi', 'prenom': 'Titi', 'mail': 'titi@gmail.com', 'pass': 'Titi','genre':'Feminin'},
                        'comptes':[{'id': 1, 'numero': 00000, 'banque_id': 0, 'definition': '', 'mdepart': 000 }]},
            {'id': 4, 'infos':{'nom': 'Toto','prenom': 'Toto', 'mail': 'toto@yahoo.fr', 'pass': 'Toto','genre':'Masculin'},
                        'comptes': [{'id': 1, 'numero': '10000', 'banque_id': 1, 'definition': 'compte courrant', 'mdepart': 300},
                                    {'id': 2, 'numero': '7700', 'banque_id': 2, 'definition': 'compte courrant', 'mdepart': 1000},
                                    {'id': 3, 'numero': '7880', 'banque_id': 2, 'definition': 'compte courrant Credits', 'mdepart': 100}]},
            {'id': 5, 'infos':{'nom': 'Tutu', 'prenom': 'Tutu', 'mail': 'tutu@gmail.com', 'pass': 'Tutu','genre':'Masculin'},
                        'comptes': [{'id': 1, 'numero': '300', 'banque_id': 5, 'definition': 'compte epargne','mdepart': 3000},
                                    {'id': 2, 'numero': '10000', 'banque_id': 4, 'definition': 'compte courrant', 'mdepart': 930}]},
            {'id': 6, 'infos': {'nom': '', 'prenom': '', 'mail': '', 'pass': 'null','genre':''},
                        'comptes':[{'id': 1, 'numero': 00000, 'banque_id': 0, 'definition': '', 'mdepart': 000 }]}]



def users_tiers():
    return [{'id': 1, 'name': 'TataTiers'},
            {'id': 2, 'name': 'TeteTiers'},
            {'id': 3, 'name': 'TitiTiers'},
            {'id': 4, 'name': 'TotoTiers'},
            {'id': 5, 'name': 'TutuTiers'},
            {'id': 6, 'name': 'TafaTiers'},
            {'id': 7, 'name': 'FefeTiers'},
            {'id': 8, 'name': 'FifiTiers'},
            {'id': 9, 'name': 'FofoTiers'},
            {'id': 10, 'name': 'FufuTiers'}]

def user_connected(user_id):
  for user in static_users():
        if user['id'] == user_id:
            if user['genre']== 'Masculin':
                user['genre']= 'Mr'

            if user['genre']== 'Feminin':
                user['genre']= 'Mme'
                
            return user


def compte(compte_id):
    for compte in static_comptes():
        if compte['id'] == compte_id:
            return compte

def comptes_user(user_id):
    comptes=static_comptes()
    liste= []
    for compte in comptes:
        if compte['user_id'] == user_id:
            compte['banque_id']=banque_idname(compte['banque_id'])
            liste.append(compte)
        """else:
            liste=[{'id': '', 'numero': '', 'banque_id': '', 'definition': '', 'user_id': '', 'mdepart': ''}]"""
    return liste

def montant_random(n_rand0, n_rand1):
    rand = random.randint(n_rand0, n_rand1)
    return rand

def banque_idname(banque_id):
    for banque in static_banques():
        if banque['id'] == banque_id:
            return banque['name']

def operation_random():
    pass


if __name__ == "__main__":
    print(static_mouvements())

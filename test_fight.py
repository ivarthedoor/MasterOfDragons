from random import randint
from utils import sleep_and_clear


def lets_fight():
    player_hp = 100
    enemy_hp = 80

    while True:
        if player_hp <= 0:
            player_hp = 0
            print(f"Player Hp: {player_hp}\nEnemy Hp: {enemy_hp}\nEnemy won, you died...")
            break
        elif enemy_hp <= 0:
            enemy_hp = 0
            print(f"Player Hp: {player_hp}\nEnemy Hp: {enemy_hp}\nYou won, Enemy died...")
            break
        else:
            player_hit = randint(0, 15)
            enemy_hit = randint(0, 10)

            if enemy_hit == 0:
                print("Enemy missed you")
                sleep_and_clear(1)
            elif player_hit == 0:
                print("You missed enemy")
                sleep_and_clear(1)
            else:
                print(f"Player Hp: {player_hp}\nEnemy Hp: {enemy_hp}")
                player_hp -= enemy_hit
                print(f"Enemy hits You with: {enemy_hit}")
                sleep_and_clear(1)

                print(f"Player Hp: {player_hp}\nEnemy Hp: {enemy_hp}")
                enemy_hp -= player_hit
                print(f"You hit enemy with: {player_hit}")
                sleep_and_clear(1)


lets_fight()

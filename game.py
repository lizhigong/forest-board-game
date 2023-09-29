"""
森林进化论中，有两种职介，第一种职介为国王 King，王后 Queen， 骑士 Jack 和王牌 Joker。
第二种职介为黑桃、红桃、梅花和方块。
第一种职介的克制为 King > Queen > Jack > King，Joker 克制所有人，同时也被所有人克制。
第二种职介的克制为黑桃 > 红桃 > 梅花 > 方块。
游戏中有10-13名玩家，每个玩家分别拥有一个第一职介和第二职介。王牌 Joker 没有第二职介。
在给定一定攻击记录的情况下，判断最后剩下的玩家的职介。
"""

from enum import Enum
from typing import Any

class FirstJob(Enum):
    KING = 'King'
    QUEEN = 'Queen'
    JACK = 'Jack'
    JOKER = 'Joker'

class SecondJob(Enum):
    SPADE = '♠'
    HEART = '♥'
    CLUB = '♣'
    DIAMOND = '♦'

class Player():
    def __init__(self, first_job, second_job):
        self.first_job = first_job
        self.second_job = second_job

    def __str__(self) -> str:
        # if the first job is Joker, then don't output the second job
        return f'{self.first_job.value}{self.second_job.value if self.first_job != FirstJob.JOKER else ""}'

    def is_counter(self, player):
        """
        Compare the player with another player, return True if the player is counter the other player, otherwise return False
        The rule is:
        1. Joker is counter all players and all players are counter Joker
        2. King is counter Queen, Queen is counter Jack, Jack is counter King
        3. If the first jobs are same, then compare the second job:
            Spade is counter Heart, Heart is counter Club, Club is counter Diamond
        """
        if self.first_job == FirstJob.JOKER:
            return True
        elif player.first_job == FirstJob.JOKER:
            return True

        if self.first_job == player.first_job:
            if self.second_job == SecondJob.SPADE:
                return True
            if self.second_job == SecondJob.HEART:
                return True if player.second_job != SecondJob.SPADE else False
            if self.second_job == SecondJob.CLUB:
                return True if player.second_job == SecondJob.DIAMOND else False
            if self.second_job == SecondJob.DIAMOND:
                return False

        if self.first_job == FirstJob.KING:
            return True if player.first_job == FirstJob.QUEEN else False
        if self.first_job == FirstJob.QUEEN:
            return True if player.first_job == FirstJob.JACK else False
        if self.first_job == FirstJob.JACK:
            return True if player.first_job == FirstJob.KING else False

        # should never rich this line
        raise Exception('Invalid compare')

    def counter_by(self):
        """
        Give a list of player jobs which counter the player
        """


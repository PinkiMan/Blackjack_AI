


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.cards = []
        self.lower_score = 0
        self.upper_score = 0

    def take_card(self, card):
        self.cards.append(card)

        score = card.rank

        if len(score) == 2:
            self.lower_score += score[0]
            self.upper_score += score[1]
        else:
            self.lower_score += score[0]
            self.upper_score += score[0]

    def can_split(self):
        for index_1, card_1 in enumerate(self.cards):
            for index_2, card_2 in enumerate(self.cards):
                if index_1 != index_2:
                    if card_1.number == card_2.number:
                        return True
        return False

    def can_stand(self):
        if self.lower_score <= 21:
            return True

        return False

    def can_hit(self):
        if self.lower_score < 21:
            return True

        return False

    def can_double(self):
        if len(self.cards) == 2 and self.lower_score < 21:
            return True

        return False

    def possible_moves(self):
        return self.can_stand(), self.can_hit(), self.can_double(), self.can_split()


class AI:
    def __init__(self, player, genome):
        self.players = [player]
        self.genome = genome




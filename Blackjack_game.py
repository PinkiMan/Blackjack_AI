
from Player import Player, AI
from Deck import Deck









class Game:
    def __init__(self, config = None):
        self.players = []
        self.dealer = None
        self.deck = Deck()
        self.config = config

    def game_init(self, player_count):
        self.deck.shuffle()

        self.dealer = Player('Dealer')

        for i in range(player_count):
            player = Player('P'+str(i))
            self.players.append(player)

        for player in self.players:
            card = self.deck.take_card()
            player.take_card(card)

        card = self.deck.take_card()
        self.dealer.take_card(card)

        for player in self.players:
            card = self.deck.take_card()
            player.take_card(card)

        card = self.deck.take_card()
        self.dealer.take_card(card)


    def setup_ai_players(self, genomes):
        ai_players = []
        for index, genome in enumerate(genomes):
            net = neat.nn.FeedForwardNetwork.create(genome, self.config)

            ai_player = AI(Player(f"net-{index}"), net)

            ai_players.append(ai_player)

        return ai_players

    def train(self, genomes):
        self.game_init(len(genomes))

        ai_players = self.setup_ai_players(genomes)

        for ai_player in ai_players:
            for player in ai_player.players:
                while True:


                    stand = False
                    hit = False
                    double = False
                    split = False

                    stand, hit, double, split = player.possible_moves()

                    if not stand:
                        break


    def player_game(self, player):


    def play(self):
        self.game_init(3)

        for player in self.players:
            while True:

                stand = False
                hit = False
                double = False
                split = False

                stand, hit, double, split = player.possible_moves()

                play = None
                if not stand:
                    break

                else:
                    rnd = random.randint(0,3)
                    if rnd == 0:
                        play = 'stand'

                if play == 'stand':
                    break
                elif play == 'hit':
                    player.take_card(self.deck.take_card())
                    player.score -=1
                elif play ==









                print("Xd")






Gg = Game()

Gg.play()



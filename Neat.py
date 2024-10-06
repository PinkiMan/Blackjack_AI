import neat


def eval_genomes(genomes, config):

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) -1:
            break
        genome1.fitness = 0
        for genome_id2,genome2 in genomes[i+1:]:
            if genome2.fitness is None:
                genome2.fitness = 0
            game = MyGame()
            game.train_ai(genome1,genome2,config)

    max_fitness = 0
    max_genome = None
    for genome in genomes:
        if max_fitness < genome[1].fitness:
            max_fitness = genome[1].fitness
            max_genome = genome

    #get_layers(max_genome[1].connections)
    update([generation,max_fitness])

def neat_runner(config, restore = False):
    if not restore:
        p = neat.Checkpointer.restore_checkpoint('checkopoints/neat-checkpoint-1')
    else:
        p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1, filename_prefix='checkopoints/neat-checkpoint-'))

    winner = p.run(eval_genomes, 1000)
    with open(MODEL, 'wb') as FILE:
        pickle.dump(winner, FILE)
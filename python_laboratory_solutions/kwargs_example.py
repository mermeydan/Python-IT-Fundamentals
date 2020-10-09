def animals(**kwargs):
    for key, value in kwargs.items():
        # print("are", key)
        print(value, "are", key)
animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")

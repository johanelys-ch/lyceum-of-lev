init python:

    affinities = {
        "Enzo": 0,
        "Scylla": 0,
        "Roger": 0,
        # "RogerMax": 0,
        # "ScyllaMax": 0,
        # "EnzoMax": 6,
        # "RogerEnough": 0,
        # "ScyllaEnough":0,
        # "EnzoEnough":4,
        # "EnzoFriend":3
    }

    def increase_affinity(name,amount):
        affinities[name] += amount

    def decrease_affinity(name,amount):
        affinities[name] -= amount
        if affinities[name] < 0:
            affinities[name] = 0
    
    # def check_affinity(name):
    #     if affinities[f"{name}Enough"] > affinities[f"{name}"]:
    #         return False
    #     else:
    #         return True
    # def check_affinity_max(name):
    #     if affinities[f"{name}Max"] > affinities[f"{name}"]:
    #         return False
    #     else:
    #         return True
    # def check_enzo_friend():
    #     if affinities[f"EnzoFriend"] > affinities["Enzo"]:
    #         return False
    #     else:
    #         return True
    
    def check_affinity_flexible(name,threshold):
        if threshold > affinities[f"{name}"]:
            return False
        else:
            return True

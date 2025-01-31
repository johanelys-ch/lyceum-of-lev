init python:

    affinities = {
        "Enzo": 0,
        "Scylla": 0,
        "Roger": 0,
        "Lalonde": 0,
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
    
    def check_affinity_flexible(name,threshold):
        if threshold > affinities[f"{name}"]:
            return False
        else:
            return True

import json
from enemy import Enemy


def safe_enemys_to_file():
    enemy1 = Enemy(health=100, mana=40, damage=20)
    enemy2 = Enemy(health=150, mana=10, damage=10)
    enemy3 = Enemy(health=60, mana=20, damage=40)
    all_enemys = {'enemy 1': enemy1.__dict__, 'enemy 2': enemy2.__dict__, 'enemy 3': enemy3.__dict__}
    with open('enemys_file.json', 'w') as f:
        use_for_load = json.dumps(all_enemys, indent=4)
        f.write(json.dumps(all_enemys, indent=4))
    return use_for_load

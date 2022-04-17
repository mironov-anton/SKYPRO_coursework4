from typing import Dict

from flask import Flask, render_template, request, redirect, url_for

from game.character_classes import character_classes
from game.equipment import EquipmentData
from game.hero import Hero, Player, Enemy
from game.utils import load_equipment

app = Flask(__name__)
app.url_map.strict_slashes = False

heroes: Dict[str, Hero] = dict()

EQUIPMENT: EquipmentData = load_equipment()


def render_choose_character_template(*args, **kwargs) -> str:
    return render_template(
        'hero_choosing.html',
        classes=character_classes.values(),
        equipment=EQUIPMENT,
        **kwargs,
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        return render_choose_character_template(header='Выберите героя', next_buton='Выбрать врага')

    heroes['player'] = Player(
        class_=character_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )

    return redirect(url_for('choose_enemy'))


@app.route('/choose-enemy', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        return render_choose_character_template(header='Выберите врага', next_buton='Начать сражение')

    heroes['enemy'] = Enemy(
        class_=character_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )

    return redirect(url_for('start_fight'))


@app.route('/fight')
def start_fight():
    if 'player' in heroes and 'enemy' in heroes:
        return render_template('fight.html', heroes=heroes, results='Fight!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

# Pokemon top trumps


## Contents
- [About](#about)
- [Setup guide](#setup-guide)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)
- [Licenses](#licenses)

## About

Welcome! This project uses [PokéAPI](https://pokeapi.co/) and [Flask](https://flask.palletsprojects.com/en/2.3.x/) to simulate a top trumps game, played against your computer.

<img src="static/gameplay.png" class='markdown-img' width=70% alt="Gameplay screenshot">

## Setup guide

1. Clone the repo
```
$ git clone https://github.com/Barbour-Condini/top_trumps_pokemon.git
```

2. Initialise and activate a virtual environment 
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

3.  Install the required libraries in their relevant versions
```
$ pip install -r requirements.txt
```

4. Generate a secret key, and copy it

```
$ python3
>>> import os
>>> os.urandom(24).hex()
```

5. Paste the code below into the project's `config.json` file
```json
 {"APP.SECRET_KEY": "ADD_KEY_HERE"}
```

6. Paste your secret key from step 4 to replace `"ADD_KEY_HERE"`



You should be all set for gameplay! Run the `app.py` file to go catch 'em all.


## Roadmap
- Add login functionality 
- Add a database with SQLAlchemy to let users track their scores, win streaks etc.


## Acknowledgements
With thanks to:
- [PokéAPI](https://pokeapi.co) (Pokemon data)
- [NES.css](https://nostalgic-css.github.io/NES.css/) (CSS framework & Poké Ball graphic)
- [PokéSprite](https://msikma.github.io/pokesprite/) (sprite images)
- [Pokermon](https://github.com/hertantoirawan/pokermon) (card back image)
- [Pokepalettes](https://pokepalettes.com) (colour palette)
- [Google Fonts](https://fonts.google.com/) ('Press Start 2P' font)


## Licenses

The sprite images are [© Nintendo/Creatures Inc./GAME FREAK Inc](https://www.pokemon.com/us/legal/).

This project is licensed under the terms of the [MIT license](https://opensource.org/license/mit/)

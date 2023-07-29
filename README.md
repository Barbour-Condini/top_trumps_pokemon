# Pokemon top trumps

## Contents
- [About](#about)
- [Setup guide](#setup-guide)
- [Roadmap](#roadmap)

## About

Welcome! This project uses [PokeAPI](https://pokeapi.co/) and [Flask](https://flask.palletsprojects.com/en/2.3.x/) to simulate a top trumps game, played against your computer.

The project is currently in its ~~ugly duckling~~ pocket monster phase. Styling is in the pipeline to turn it into a very fine ~~swan~~ pokemon indeed.

## Setup guide

1. In your terminal, navigate to (or create) an empty directory that you want to clone this repo into. Then enter:
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

4. Generate a secret key, and copy it:

```
$ python3
>>> import os
>>> os.urandom(16).hex()
```

5. Paste the code below into the project's `config.json` file
```json
 {"APP.SECRET_KEY": "ADD_KEY_HERE"}
```

6. Paste your secret key from step 4 to replace `"ADD_KEY_HERE"`. The key will need double quote marks round it.



You should be all set for gameplay! Run the `app.py` file to go catch 'em all.


## Roadmap
- [ ]: Add login functionality 
- [ ]: Add a database with SQLAlchemy to let users track their scores, win streaks etc.
- [ ]: Call an emergency CSS intervention to put some bootstraps on these pokemons' shoes.

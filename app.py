import json
from flask import Flask, render_template, request, url_for, redirect, session
import random
import pokefunctions as pokemon

app = Flask(__name__)
with open("config.json", "r") as f:
    load = json.load(f)
    app.config['SECRET_KEY'] = load["APP.SECRET_KEY"]


@app.route("/", methods=['GET', 'POST'])
def start():
    player_cards, computer_cards = pokemon.card_allocation()
    player_choice = True
    draw_cards = []

    # send these objects to the session dictionary so you can access them in any route
    session["player_cards"] = player_cards
    session["computer_cards"] = computer_cards
    session["player_choice"] = player_choice
    session["draw_cards"] = draw_cards

    if request.method=='POST':
        player_name = request.form['player_name']
        session["player_name"] = player_name
        return redirect(url_for('player_select'))
    return render_template('start.html')


@app.route("/player_select", methods=['GET', 'POST'])
def player_select():

    player_stats = pokemon.collect_stats(session["player_cards"][0])
    computer_stats = pokemon.collect_stats(session["computer_cards"][0])
    selectable_stats = ['height', 'weight', 'speed', 'hp', 'attack', 'defense']
    player_card_no = len(session['player_cards'])
    computer_card_no = len(session['computer_cards'])
    draw_card_no = len(session['draw_cards'])
    player_name = session["player_name"]

    # save player and computer stats to the session so you can access them from any view function
    session["player_stats"] = player_stats
    session["computer_stats"] = computer_stats

    if request.method=='POST': 
        # capture the selected stat and save it to the session
        session["selected_stat"] = request.form['selected_stat']
        # print(session["selected_stat"])

        return redirect(url_for('result'))

    return render_template('player_select.html', player_stats=player_stats, computer_stats=computer_stats,
                           player_card_no=player_card_no, computer_card_no=computer_card_no, draw_card_no=draw_card_no,
                           player_name = player_name)


@app.route("/computer_select", methods=['GET', 'POST'])
def computer_select():
    player_stats = pokemon.collect_stats(session["player_cards"][0])
    computer_stats = pokemon.collect_stats(session["computer_cards"][0])
    selectable_stats = ['height', 'weight', 'speed', 'hp', 'attack', 'defense']
    player_card_no = len(session['player_cards'])
    computer_card_no = len(session['computer_cards'])
    draw_card_no = len(session['draw_cards'])
    player_name=session['player_name']

    # save player and computer stats to the session
    session["player_stats"] = player_stats
    session["computer_stats"] = computer_stats

    if request.method=='POST': 
        # the user has clicked the 'Next' button, so go to the result route
        return redirect(url_for('result'))
    
    # capture the selected stat and save it to the session
    session["selected_stat"] = selectable_stats[random.randint(0, 5)]
    # print(session["selected_stat"])
    return render_template('computer_select.html', player_stats=player_stats, computer_stats=computer_stats,
                           player_card_no=player_card_no, computer_card_no=computer_card_no, draw_card_no=draw_card_no,
                           player_name=player_name)


@app.route("/result", methods=['GET', 'POST'])
def result():

    # collect & name all the data pieces you'll need to send to the result.html template 
    selected_stat = session["selected_stat"]
    player_stat = session["player_stats"][selected_stat]
    computer_stat = session["computer_stats"][selected_stat]
    computer_pokemon_name = session["computer_stats"]["name"]
    
    # if player clicks 'Next Card':
    if request.method=='POST':

        # if the game's not over, play the cards against each other and reallocate cards accordingly
        reallocated_cards = pokemon.play_round(session["selected_stat"], session['player_cards'], session['computer_cards'], 
                                               session['draw_cards'], session['player_choice'])

        # update the session dictionary data with the reallocated cards (and player_choice boolean)
        for i in ['player_cards', 'computer_cards', 'draw_cards','player_choice']:
            session[i] = reallocated_cards[i]

        # Check if the game's over
        player_card_no = len(session['player_cards'])
        computer_card_no = len(session['computer_cards'])

        if player_card_no == 0 or computer_card_no == 0:
            return redirect(url_for('end'))

        if session["player_choice"]:
            return redirect(url_for('player_select'))
        else:
            return redirect(url_for('computer_select'))
    
    # else if player's come straight here from one of the select.html routes:
    # then render the template, passing in three objects as arguments so the template knows what they reference
    return render_template('result.html', selected_stat=selected_stat, player_stat=player_stat, 
                           computer_stat=computer_stat, computer_pokemon_name=computer_pokemon_name,
                           player_stats=session['player_stats'], computer_stats=session['computer_stats'],
                           player_name=session['player_name'])


@app.route("/end", methods=['GET', 'POST'])
def end():
    if request.method == 'POST':
        return redirect(url_for('start'))
    
    winner = pokemon.end_of_play(session['player_cards'], session['computer_cards'])
    return render_template('end.html', winner=winner)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
from info_src.user_info_collector import player_summary

#Temp app.py to test and purely test out the display of the result

app = Flask(__name__)

@app.route("/", methods=['GET'])
def init_load():
    regions = ["RU", "BR", "LAN", "LAS", "OCE", "KR", "JP", "EUNE", "EUW", "TR", "NA"]
    return render_template('index.html', regions=regions, positions = ' ' * 5, champ5 = [[' '] * 6] * 5)

@app.route("/test", methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        regions = ["RU", "BR", "LAN", "LAS", "OCE", "KR", "JP", "EUNE", "EUW", "TR", "NA"]
        region = request.form.get('regions_data')
        username = request.form.get('username_data')
        res = player_summary(username, region)
        return render_template('index.html', regions = regions, positions = res['pos'], champ5 = res["top5"])
    elif request.method == 'GET':
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
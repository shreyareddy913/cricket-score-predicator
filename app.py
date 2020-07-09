from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 't20-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Australia':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'England':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Pakistan':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'India':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Australia':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'England':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Pakistan':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Sri Lanka':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'New Zealand':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)
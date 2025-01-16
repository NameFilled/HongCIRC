from flask import Flask, jsonify, render_template, request
import pandas as pd

app = Flask(__name__)

# Load datasets
circRNA_info = pd.read_csv('data/circ_info.csv')
circRNA_disease = pd.read_csv('data/circAtlas_disease.csv')
circRNA_function = pd.read_csv('data/function_circRNA.csv')

# Routes
@app.route('/')
def home():
    sample_data = {
        'circRNA_info': circRNA_info.head(5).to_dict(orient='records'),
        'circRNA_disease': circRNA_disease.head(5).to_dict(orient='records'),
        'circRNA_function': circRNA_function.head(5).to_dict(orient='records')
    }
    return render_template('index.html', sample_data=sample_data)

@app.route('/query/<table>', methods=['GET', 'POST'])
def query(table):
    if request.method == 'POST':
        key = request.form.get('key')
        if table == 'circRNA_info':
            result = circRNA_info[circRNA_info['circAtlas ID'] == key].to_dict(orient='records')
        elif table == 'circRNA_disease':
            result = circRNA_disease[circRNA_disease['circAtlas ID'] == key].to_dict(orient='records')
        elif table == 'circRNA_function':
            result = circRNA_function[circRNA_function['circRNA name'] == key].to_dict(orient='records')
        else:
            result = []
        return render_template('query.html', table=table, result=result)
    return render_template('query.html', table=table)

@app.route('/api/statistics')
def statistics():
    stats = {
        'total_circRNAs': len(circRNA_info),
        'total_diseases': circRNA_disease['Disease Name'].nunique(),
        'total_functions': circRNA_function['Function'].nunique()
    }
    return jsonify(stats)

@app.route('/api/circRNAs', methods=['GET'])
def get_circRNAs():
    circRNAs = circRNA_info.to_dict(orient='records')
    return jsonify(circRNAs)

@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    diseases = circRNA_disease.to_dict(orient='records')
    return jsonify(diseases)

@app.route('/api/functions', methods=['GET'])
def get_functions():
    functions = circRNA_function.to_dict(orient='records')
    return jsonify(functions)

if __name__ == '__main__':
    app.run(debug=True)
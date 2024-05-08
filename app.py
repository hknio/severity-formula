from flask import Flask, request
from calculator.formula import *
import json

app = Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculate():

    if request.is_json:
        data = request.json
        likelihood = int(data["Likelihood"])
        impact = int(data["Impact"])

        exploitability = int(search_item_by_name("Dropdown1", data)["Value"]) - 1 # custom fields start from 1 rather than 0
        complexity = int(search_item_by_name("Dropdown2", data)["Value"]) - 1 # custom fields start from 1 rather than 0

        if likelihood not in range(1, 6):
            return f"invalid likelihood: {likelihood}", 400
        elif impact not in range(1, 6):
            return f"invalid impact: {impact}", 400
        elif exploitability not in range(3):
            return f"invalid exploitability: {exploitability}", 400
        elif complexity not in range(3):
            return f"invalid issue_complexity: {complexity}", 400

        (result, _, _, _, _,) = calculate_severity(
            likelihood=likelihood, 
            impact=impact,
            exploitability=exploitability,
            issue_complexity=complexity
        )

        (label, _) = generate_label(result)
        result = round(result, 1)
        data = {"result": result,  "severity": label, "version": VERSION}
    
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

        return response

def search_item_by_name(name, data):
    for item in data['CustomFields']:
        if item['Name'] == name:
            return item
    return None
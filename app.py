from flask import Flask, request
from calculator.formula import *
import json

app = Flask(__name__)

@app.route("/calculate")
def calculate():
    likelihood = int(request.args.get('L'))
    impact = int(request.args.get('I'))
    exploitability = int(request.args.get('E'))
    complexity = int(request.args.get('C'))

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
    score = "{:.1f}".format(result)
    
    data = {"score": score,  "severity": label}
    
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response
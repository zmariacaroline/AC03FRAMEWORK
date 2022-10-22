from flask import Flask, request
import json
app = Flask(___name___)

ra = 210000

@app.route('consultar/(ra)', methods = ['GET'])

def consultar_aluno()

task = [

    {
        "ra": 210000,
        "name": "Emmanuel",
        "curso" "Analise e desenvolvimento de sistemas"

    }
]
tasksJSON = json.dumps(tasks)
return tasksJSON
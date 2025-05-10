from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = []

@app.route('/api/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

@app.route('/api/tareas', methods=['POST'])
def agregar_tarea():
    nueva_tarea = request.get_json()
    nueva_tarea['id'] = len(tareas) + 1
    nueva_tarea['dias_sugeridos'] = calcular_dias_sugeridos(nueva_tarea['prioridad'])
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

def calcular_dias_sugeridos(prioridad):
    if prioridad == "Alta":
        return 1
    elif prioridad == "Media":
        return 3
    else:
        return 7

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

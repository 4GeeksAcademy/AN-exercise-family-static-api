from flask import Flask, request, jsonify

app = Flask(__name__)

# Estructura de datos: la familia inicial con 3 miembros.
family_members = [
    {"id": 1, "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 8, 9]},
    {"id": 2, "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [4, 2, 5]},
    {"id": 3, "first_name": "Jenna", "last_name": "Jackson", "age": 30, "lucky_numbers": [1, 2, 3]}
]

# Ruta GET para obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(family_members)

# Ruta GET para obtener un miembro por su ID
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    # Buscar al miembro por ID
    member = next((m for m in family_members if m['id'] == id), None)
    
    if member:
        return jsonify(member)
    else:
        return jsonify({"error": "Member not found"}), 404

# Ruta POST para agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json 
    family_members.append(new_member)  
    return jsonify(new_member), 200

# Ruta DELETE para eliminar un miembro por su ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    global family_members
    # Filtrar todos los miembros que no sean el que queremos eliminar
    family_members = [m for m in family_members if m['id'] != id]
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(debug=True)

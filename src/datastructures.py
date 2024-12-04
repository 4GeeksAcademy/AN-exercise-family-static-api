class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Este método genera un id único para los miembros
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Método para agregar un miembro
    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generate_id()  
        member["lucky_numbers"] = list(member.get("lucky_numbers", []))  
        self._members.append(member)
        return member

    # Método para eliminar un miembro por su id
    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return  
        return None  # Si no se encuentra el miembro

    # Método para obtener un miembro por su id
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # Si no se encuentra el miembro, retornar None

    # Este método devuelve todos los miembros
    def get_all_members(self):
        return self._members

class SerializeMixin:

    """
        Willyam cutrim - Criado para serializar qualquer modelo, mas o Schema nesse momento resolveu meu problema
    """
    def to_dict(self, visited=None):
        if visited is None:
            visited = set()

        # Evitar recursão infinita
        if self in visited:
            return {}

        visited.add(self)

        result = {col.name: getattr(self, col.name) for col in self.__table__.columns}
        for relationship in self.__mapper__.relationships:
            related_value = getattr(self, relationship.key)
            if related_value is not None:
                if relationship.uselist:
                    result[relationship.key] = [item.to_dict(visited) for item in related_value if item is not None]
                else:
                    result[relationship.key] = related_value.to_dict(visited) if related_value is not None else None
        return result

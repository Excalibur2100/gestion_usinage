from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class GestionAcces(Base):
    __tablename__ = "gestion_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    niveau_acces = Column(String(50))

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="gestion_acces")
    def __repr__(self):
        return f"<GestionAcces(id={self.id}, utilisateur_id={self.utilisateur_id}, niveau_acces={self.niveau_acces})>"
    def __init__(self, utilisateur_id, niveau_acces):
        self.utilisateur_id = utilisateur_id
        self.niveau_acces = niveau_acces
    def __str__(self):
        return f"GestionAcces(id={self.id}, utilisateur_id={self.utilisateur_id}, niveau_acces={self.niveau_acces})"
    def __eq__(self, other):
        if not isinstance(other, GestionAcces):
            return False
        return self.id == other.id and self.utilisateur_id == other.utilisateur_id and self.niveau_acces == other.niveau_acces
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if not isinstance(other, GestionAcces):
            return NotImplemented
        return self.id < other.id
    def __le__(self, other):
        if not isinstance(other, GestionAcces):
            return NotImplemented
        return self.id <= other.id
    def __gt__(self, other):
        if not isinstance(other, GestionAcces):
            return NotImplemented
        return self.id > other.id
    def __ge__(self, other):
        if not isinstance(other, GestionAcces):
            return NotImplemented
        return self.id >= other.id
    def __hash__(self):
        return hash((self.id, self.utilisateur_id, self.niveau_acces))
    def __len__(self):
        return len(self.niveau_acces)
    def __getitem__(self, key):
        if key == "id":
            return self.id
        elif key == "utilisateur_id":
            return self.utilisateur_id
        elif key == "niveau_acces":
            return self.niveau_acces
        else:
            raise KeyError(f"Key {key} not found in GestionAcces")
    def __setitem__(self, key, value):
        if key == "id":
            self.id = value
        elif key == "utilisateur_id":
            self.utilisateur_id = value
        elif key == "niveau_acces":
            self.niveau_acces = value
        else:
            raise KeyError(f"Key {key} not found in GestionAcces")
    def __delitem__(self, key):
        if key == "id":
            del self.id
        elif key == "utilisateur_id":
            del self.utilisateur_id
        elif key == "niveau_acces":
            del self.niveau_acces
        else:
            raise KeyError(f"Key {key} not found in GestionAcces")
    def __contains__(self, item):
        if isinstance(item, GestionAcces):
            return self.id == item.id
        elif isinstance(item, int):
            return self.id == item
        elif isinstance(item, str):
            return self.niveau_acces == item
        else:
            return False
    def __iter__(self):
        yield "id", self.id
        yield "utilisateur_id", self.utilisateur_id
        yield "niveau_acces", self.niveau_acces
    def __next__(self):
        if self.id is None:
            raise StopIteration
        else:
            return self.id
    def __reversed__(self):
        yield "niveau_acces", self.niveau_acces
        yield "utilisateur_id", self.utilisateur_id
        yield "id", self.id
    def __sizeof__(self):
        return len(self.niveau_acces) + len(self.utilisateur_id) + len(self.id)
    def __format__(self, format_spec):
        return f"GestionAcces(id={self.id}, utilisateur_id={self.utilisateur_id}, niveau_acces={self.niveau_acces})"
    def __copy__(self):
        return GestionAcces(self.utilisateur_id, self.niveau_acces)
    def __deepcopy__(self, memo):
        return GestionAcces(self.utilisateur_id, self.niveau_acces)
    def __reduce__(self):
        return (GestionAcces, (self.utilisateur_id, self.niveau_acces))
    def __reduce_ex__(self, protocol):
        return (GestionAcces, (self.utilisateur_id, self.niveau_acces))
    def __dir__(self):
        return ["id", "utilisateur_id", "niveau_acces"]
    def __sizeof__(self):
        return len(self.niveau_acces) + len(self.utilisateur_id) + len(self.id)
    def __doc__(self):
        return "GestionAcces(id, utilisateur_id, niveau_acces)"
    def __str__(self):
        return f"GestionAcces(id={self.id}, utilisateur_id={self.utilisateur_id}, niveau_acces={self.niveau_acces})"
    def __repr__(self):
        return f"<GestionAcces(id={self.id}, utilisateur_id={self.utilisateur_id}, niveau_acces={self.niveau_acces})>"
    def __hash__(self):
        return hash((self.id, self.utilisateur_id, self.niveau_acces))
    def __len__(self):
        return len(self.niveau_acces) + len(self.utilisateur_id) + len(self.id)
    def __bool__(self):
        return bool(self.niveau_acces) and bool(self.utilisateur_id) and bool(self.id)
    def __call__(self, *args, **kwargs):
        return GestionAcces(self.utilisateur_id, self.niveau_acces)
    def __getattr__(self, name):
        if name == "id":
            return self.id
        elif name == "utilisateur_id":
            return self.utilisateur_id
        elif name == "niveau_acces":
            return self.niveau_acces
        else:
            raise AttributeError(f"Attribute {name} not found in GestionAcces")
    def __setattr__(self, name, value):
        if name == "id":
            self.id = value
        elif name == "utilisateur_id":
            self.utilisateur_id = value
        elif name == "niveau_acces":
            self.niveau_acces = value
        else:
            raise AttributeError(f"Attribute {name} not found in GestionAcces")
    def __delattr__(self, name):
        if name == "id":
            del self.id
        elif name == "utilisateur_id":
            del self.utilisateur_id
        elif name == "niveau_acces":
            del self.niveau_acces
        else:
            raise AttributeError(f"Attribute {name} not found in GestionAcces")

from models import session, Role, Audition

# Create a role
role = Role(character_name="Jat")
session.add(role)
session.commit()

# Add auditions
audition1 = Audition(actor="Fung", location="Tokyo", phone=1234567890, role_id=role.id)
audition2 = Audition(actor="Will Smith", location="LA", phone=9876543210, role_id=role.id)

session.add_all([audition1, audition2])
session.commit()

# Test methods
print(role.actors())  # Output: ["Fung", "Will Smith"]
audition1.call_back()
print(role.lead())  # Output: <models.Audition object at 0x7fbdd338ac10>

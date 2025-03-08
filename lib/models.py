from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, create_engine

Base = declarative_base()

class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    # Relationship to Role
    role = relationship("Role", back_populates="auditions")

    def call_back(self):
        #Changes the hired attribute to True.
        self.hired = True

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # Relationship to Audition
    auditions = relationship("Audition", back_populates="role")

    def actors(self):
        #Returns a list of actor names associated with this role
        return [audition.actor for audition in self.auditions]

    def locations(self):
        #Returns a list of locations from the auditions associated with this role
        return [audition.location for audition in self.auditions]

    def lead(self):
        #Returns the first hired audition for this role or a default message.
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role"

    def understudy(self):
        #Returns the second hired audition for this role or a default message
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for not understanding this role"

# Create the SQLite database
engine = create_engine("sqlite:///theater.db")
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()




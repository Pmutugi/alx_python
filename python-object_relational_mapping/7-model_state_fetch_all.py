# '''script that lists states from hbtn_0e_usa'''
# from sys import argv
# import sqlalchemy
# from model_state import State, Base
# from  sqlalchemy import create_engine
# if __name__=='__main__':
#     dialect = 'mysql'
#     username =argv[1]
#     password = argv[2]
#     database = argv[3]
#     host = 'localhost'
#     port = '3306'
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}")

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and list all State objects in ascending order by states.id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

    
    
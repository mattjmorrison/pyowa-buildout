import sqlalchemy

def show_versions():
    print "Here are the versions I'm using"
    print "SQLAlchemy %s " % sqlalchemy.__version__
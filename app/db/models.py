from . import DB


class ToDo(DB.Model):
    """
    Specifies columns that table To-Do should consist.
    """
    id_task = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    complete = DB.Column(DB.Boolean)
    when = DB.Column(DB.String(20))
    priority = DB.Column(DB.Integer)

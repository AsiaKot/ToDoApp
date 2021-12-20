from . import DB


class ToDo(DB.Model):
    id_task = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    complete = DB.Column(DB.Boolean)


class ThisWeek(DB.Model):
    id_task = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    complete = DB.Column(DB.Boolean)


class NextWeek(DB.Model):
    id_task = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    complete = DB.Column(DB.Boolean)

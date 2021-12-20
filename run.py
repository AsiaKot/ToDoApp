from app import create_app, create_db

app = create_app()
db = create_db(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


from application import create_app

# initiate the app
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
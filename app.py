from config.settings import create_app
app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run(host=app.config['HOST'],port=app.config['PORT'], debug=app.config['DEBUG'])

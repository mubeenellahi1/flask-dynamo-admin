# sibylity-curation


# Application Structure
* config: config/settings.py makes a create_app function using config from config/config.py file
* controllers: contains logic to route urls to functions
* helpers: contains helper functions used by controllers
* static: contains css/js files
* templates: contains html files
* app.py: gets create_app function from config/settins.py and creates a flask app
* requirements.txt: Contains python dependencies
    

# Running the application
* create python virtual environment
* activate virtual environment
* ```pip install -r requirements.txt```
* create .env in root dir with these keys
  * SECRET_KEY=
  * CONFIG_NAME=dev
  * HOST=127.0.0.1
  * PORT=5000
  * DATABASE_URI=
  * DEBUG=True
  * FLASK_ENV=development  
  * AWS_ACCESS_KEY_ID=
  * AWS_SECRET_ACCESS_KEY=
* ```flask run```
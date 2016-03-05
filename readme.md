Environment:
SQLAlchemy, Python, Flask

IP address: 52.25.117.98
SSH port: 2200
URL: http://ec2-52-25-117-98.us-west-2.compute.amazonaws.com/catalog/

Software installed:
psycopg2
postgresql
postgresql-server-9.3
postgresql-server-dev-9.3
python-dev
Flask
Flask-SQLAlchemy
gclound-python
google-api-python-client

Configuration changes:
Change ssh port to 2200
Add user grader and mybackup
Disable root user access
Disable password authentication & only allow key-pair authentication
Firewall only allow ssh and www
/etc/apache2/sites-available/catalog.conf if configured to serve the app

How to use:
Go to /var/www/catalog/catalog

1. Setup the database with schema.
   python database_setup.py

2. Insert initial data into the database.
   python addItems.py

3. Restart apache
   sudo service apache2 restart

4. Access the application through browser
   use app address(IP or URL) to access

   Public pages:
   Index page: <app_address>/catalog
   User login page: <app_address>/login
   JSON API: <app_address>/catalog.json
   View items of a category: <app_address>/catalog/<category name>/items
   View detail of an item: <app_address>/catalog/<category name>/<item name>

   User need to be logged in to access:
   Add new item: <app_address>/catalog/new

   Only the user who created that item can access:
   Edit an item: <app_address>/catalog/<category name>/<item name>/edit
   Delete an item: <app_address>/catalog/<category name>/<item name>/delete

User can browse items in different categories. Each item has a name, a
paragraph of description, an optional image and belongs to one of the
existed categories When logged in with Google or Facebook account, user
can add new item to categories. A user can also edit or delete
items that he/she created.

# JWT_example

Simple flask project to explore JWT use.

## Setup

1. Clone repo  
   `git clone https://github.com/koutsilis1999/JWT_example.git`
2. Create virtual env  
   `python3 -m venv env`
3. Activate env  
   `source env/bin/activate`
4. Install requirements  
   `pip install -r requirements.txt`
5. Create sqlite database  
   `flask db upgrade`
6. Run app  
   `flask run`  
   The app is running at localhost:5000

## Create users

- To create a simple user you can send a POST request at /auth/register. Example:

  ```bash
  curl -d '{"username":"user","email":"user@example.com","password":"user1234"}' -H "Content-Type: application/json" -X POST http://localhost:5000/auth/register
  ```

- To create an admin user, you have to do it flask shell. Example:

  ```bash
  flask shell
  >>> user = User("admin","admin@example.com","admin1234",True)
  >>> db.session.add(user)
  >>> db.session.commit()
  ```

  You can also create a simple user like this if you don't add the last argument.

## Usage

Use postman or something equivalent to make calls.  
Now you can login with as a simple user or as an admin user.  
When you log in you will get the JWT as a response. Copy that.  
To access the endpoitns you need to add the JTW as a request header.  
`Authorization: Bearer {JWT} # Needs space between Bearer and JTW`  
There are three endpoints

1. /api/public
2. /api/authenticated
3. /api/autorized

The first one, as the name implies can be accessed by anyone. Uses doesn't need to be logged in.  
The second one can be access by logged in user, either simple ones or admin ones.  
The third one can be accessed only by logged in admin users.

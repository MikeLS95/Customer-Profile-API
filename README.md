# Customer Profile API

- [R1 - Explain the problem that this app will solve, and explain how this app solves or addresses the problem.](#R1)

- [R2 - Describe the way tasks are allocated and tracked in your project.](#R2)

- [R3 - List and explain the third-party services, packages and dependencies used in this app.](#R3)

- [R4 - Explain the benefits and drawbacks of this app’s underlying database system.](#R4)

- [R5 - Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.](#R5)

- [R6 - Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.](#R6)

- [R7 - Explain the implemented models and their relationships, including how the relationships aid the database implementation.](#R7)

- [R8 - Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint: ](#R8)
    - [HTTP verb](#R8)
    - [Path or route](#R8)
    - [Any required body or header data](#R8)
    - [Response](#R8)

<a id="R1"></a>
### R1 - Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

This app has been created to address the problem of customer data management for a travel agency.  The app tracks users who have either added themselves or been added by the admin user.  Once their user profile is in the database, a passport can be added to a user.  Adding a passport allows for ease of access when booking travel overseas.  The different loyalty programs currently on offer are displayed in the database, when more rewards are offered, they are added to loyalties.  Users can be filtered into their travel groups to make it simpler for them to travel together with their information being stored in their group of travel companions.

<a id="R2"></a>
### R2 - Describe the way tasks are allocated and tracked in your project.

In my project I utilized the Kanban agile methodology.  Before I started work on my code I created my ERD and broke the project into several areas to help manage the moving parts.  I utilized Trello as my software of choice and I took screenshots of my Trello board as I continued to work on my API webserver.


First screenshot upon creation of the Trello board.  The board lists out several areas of focus for the period of my API webserver project.
![First Trello](./docs/16-06-24-First-SS.JPG)

This second screenshot shows that I added items to my To Do and Doing lists to breakdown what is required in each of my entity endpoints.
![Second Trello](./docs/17-06-2024--Second-SS.JPG)

Screenshots of progress throughout development.
![Third Trello](./docs/18-06-24-Third-SS.JPG)
![Fourth Trello](./docs/20-06-2024-FourthSS.JPG)

The last two screenshots of my Trello board have created a second 'Done' table for readability.
![Fifth Trello](./docs/27-06-2024-Fifth-SS.JPG)
![Final Trello](./docs/28-06-2024-Final-SS.JPG)

<a id="R3"></a>
### R3 - List and explain the third-party services, packages and dependencies used in this app.

The software used in this project:

- Flask
- PostgreSQL
- SQLAlchemy
- Marshmallow
- Psycopg2
- JWT Manager
- Bcrypt

#### Flask:
I used flask framework for creating my routes that are used in the app.  These routes are used for deciding what will happen when a request is made.

#### PostgreSQL:
I chose PostgreSQL for my database, the place where all of the information inside my app is stored.

#### SQLAlchemy:
My app relies on SQLAlchemy as the tool to communicate with the database with interactions with PostgreSQL. SQLAlchemy allows the application of Object Orientated Programming in the databse and allows a more robust use of databse and SQL commands.

#### Marshmallow:
The use of Marshmallow is required for object serialization in my flask app.  It is the tool used for creating my entity schemas.  Marshmallow also allows for the use of JSON serialization, returning and accepting JSON responses.

#### Psycopg2:
Psycopg2 is a python library, it is used to interact with the my PostgreSQL database from within the python application.  Its primary focus is to allow communication with the PostgreSQL database and the python app.

#### JWT Manager:
This is the tool that is used for managing authentication.  JWT manager will take a hashed password and store it as a token. This token can be used across different endpoints so the user does not need to log in every time.  The manager is for creating, storing and checking the tokens.

#### Bcrypt:
Bcrypt is used to encrypt and decrypt passwords.  Bcrypt will hash a password before it is stored in the JWT manager as a token.  This is a method for keeping the database secure.

<a id="R4"></a>
### R4 - Explain the benefits and drawbacks of this app’s underlying database system.

This app utilizes PostgreSQL.  PostgreSQL is a popular often used database open-source Relational Database Management System (RDBMS), it is know for its extensibility, adherence to SQL standards and for its robustness.  Here are its benefits and drawbacks:

#### Benefits

__Feature Rich:__ PostgreSQL includes a large range of features which include support for complex queries, indexing and JSON data types.  PostgreSQL also supports various extensions that offer additional functionalities.

__Extensibility:__ Using postgresql will allow the user to define their own data types, indexing methods and procedural languages through extensions.  This making it flexible and suitable for an array of uses.

__Scalability:__ PostgreSQL has the ability to handle high loads and large data volumes.  This is due to it having multi-version concurrency control (MVCC) support. MVCC allows for the efficient handling of concurrent transactions.

__Reliability:__ PostgreSQL is known for its reliability and stability, often being chosen for mission-critical applications when uptime and data integrity is essential.

#### Drawbacks

__Complexity:__

__Learning Curve:__

__Performance:__

__

<a id="R5"></a>
### R5 - Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

<a id="R6"></a>
### R6 - Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.

<a id="R7"></a>
### R7 - Explain the implemented models and their relationships, including how the relationships aid the database implementation.

<a id="R8"></a>
### R8 - Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:

- HTTP verb
- Path or route
- Any required body or header data
- Response
CREATE TABLE IF NOT EXISTS Utilisateurs(
    id serial PRIMARY KEY, 
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL, 
    age int not null, 
    email VARCHAR(100) NOT NULL, 
    job VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS Applications(
    id serial PRIMARY KEY, 
    appname VARCHAR(100)NOT NULL, 
    username VARCHAR(100) NOT NULL, 
    lastconnection DATE NOT NULL, 
    user_id int,
    Foreign key (user_id) references Utilisateurs(id));


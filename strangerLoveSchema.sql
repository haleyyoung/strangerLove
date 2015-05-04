CREATE TABLE "user"(
    id serial PRIMARY KEY NOT NULL,
    first_name varchar(100) NOT NULL,
    last_name varchar(100) NOT NULL,
    email varchar(100) NOT NULL
);

CREATE TABLE event(
    id serial PRIMARY KEY NOT NULL,
    title varchar(1000) NOT NULL,
    description varchar(5000) NOT NULL,
    number_of_people_needed INT
);

CREATE TABLE user_event(
    user_id int REFERENCES "user"(id) ON UPDATE CASCADE ON DELETE CASCADE,
    event_id int REFERENCES Event(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT user_event_primary_key PRIMARY KEY (user_id, event_id)
);
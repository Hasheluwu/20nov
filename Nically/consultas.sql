CREATE TABLE users (
  id integer,
  gmail text,
  password text,
  username text,
  gender char(1),
  birthday integer,
  PRIMARY KEY (id)
)

CREATE TABLE achievements (
  achievement_id integer,
  title text,
  description text,
  PRIMARY KEY(achievement_id)
)

CREATE TABLE user_achievements (
  user_id integer,
  achievement_id integer,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (achievement_id) REFERENCES achievements(achievement_id)
)


CREATE TABLE categories (
  category_id integer,
  name text,
  PRIMARY KEY (category_id)
)


CREATE TABLE trivias (
  trivia_id integer,
  user_id integer,
  category_id integer,
  title text,
  image text,
  points integer,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (category_id) REFERENCES categories(category_id)
  PRIMARY KEY (trivia_id)
)

CREATE TABLE questions (
  question_id integer,
  trivia_id integer,
  question_text text,
  FOREIGN KEY (trivia_id) REFERENCES trivias(trivia_id),
  PRIMARY KEY (question_id)
)

CREATE TABLE responses (
  response_id integer,
  trivia_id integer,
  question_id integer,
  response_text text,
  correct boolean,
  FOREIGN KEY (trivia_id) REFERENCES trivias(trivia_id),
  FOREIGN KEY (question_id) REFERENCES questions(question_id),
  PRIMARY KEY (response_id)
)

CREATE TABLE user_trivias (
  user_id integer,
  trivia_id integer,
  date_played text,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (trivia_id) REFERENCES trivias(trivia_id)
)

CREATE TABLE user_responses (
  user_id integer,
  trivia_id integer,
  response_id integer,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (trivia_id) REFERENCES trivias(trivia_id),
  FOREIGN KEY (response_id) REFERENCES responses(response_id)
);



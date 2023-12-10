CREATE TABLE
    IS601_WatchList (
        id INT AUTO_INCREMENT PRIMARY KEY,
        team_id int not null,
        user_id int not null,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY(team_id) REFERENCES IS601_Team(id),
        FOREIGN KEY(user_id) REFERENCES IS601_Users(id),
        UNIQUE KEY(team_id, user_id)
    );
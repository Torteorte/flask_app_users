from application.db.db import get_db


def get_profile_by_token(token):
    db = get_db()

    return db.execute(
        'SELECT * FROM users JOIN tokens WHERE tokens.userId = users.id and tokens.token = ?', [token]
    ).fetchone()


def check_edit_properties(username, email, about):
    fields = {'Username': username, 'Email': email, 'About': about}

    for field in fields.keys():

        if not fields[field]:
            return f'{field} can`t be empty.'

    return None


def update_user(username, email, about, profile):
    db = get_db()

    db.execute(
        'UPDATE users SET username = ?, email = ?, about = ? WHERE id = ?',
        [username, email, about, profile['id']]
    )
    db.commit()


def delete_user(profile):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', [profile['id']])
    db.commit()

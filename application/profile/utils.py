from application.db.helpers import get_db
from application.application_config.exceptions import InvalidAPIUsage


def get_profile_by_token(token):
    db = get_db()

    return db.execute(
        'SELECT * FROM users JOIN tokens WHERE tokens.userId = users.id and tokens.token = ?', [token]
    ).fetchone()


def validate_edit_properties(username, email, about):
    fields = {'Username': username, 'Email': email, 'About': about}

    for field in fields.keys():

        if not fields[field]:
            raise InvalidAPIUsage(f"'{field}' can`t be empty.")


def update_user(username, email, about, profile):
    db = get_db()

    try:
        update_user_in_data_base(username, email, about, profile)

    except db.IntegrityError:
        raise InvalidAPIUsage(f"Email '{email}' is already taken.")


def update_user_in_data_base(username, email, about, profile):
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

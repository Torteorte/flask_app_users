from application.db.db import get_db


def test_user_from_tokens():
    db = get_db()

    test_user_id = 'cd8197ece12c04a7aa77f5f87cd44eee'
    token_table = db.execute(
        'SELECT * FROM tokens, users WHERE id = ?', [test_user_id]
    ).fetchone()

    print(token_table['username'])


test_user_from_tokens()

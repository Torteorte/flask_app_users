INSERT INTO users (id, username, password, email, about)
VALUES
       ('test_id', 'test_username',
        'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f',
        'test_email@email.com', 'test_about'),
       ('test_id2', 'test_username2',
        'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79',
        'test_email@email.com2', 'test_about2');

INSERT INTO tokens (token, tokenExpiration, userId)
VALUES
       ('test_token', '2021-12-30 10:10:10.0001', 'test_id'),
       ('test_token2', '2021-12-30 10:10:10.0001', 'test_id2');
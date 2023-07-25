from sqlalchemy import text

get_or_create_user_query = text('''
    INSERT INTO bot_users (
        full_name,
        telegram_id,
        added_at,
        updated_at
    ) VALUES (
        :full_name,
        :telegram_id,
        :added_at,
        :updated_at
    ) ON CONFLICT DO NOTHING
''')

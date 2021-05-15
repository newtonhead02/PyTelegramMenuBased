#Prints a message in the chatlog with information of the messages received
import telebot

def chat_log(message):
    if message.from_user.first_name == 'None':
        first_name = '\b'
    if message.from_user.username == 'None':
        username = '\b'
    if message.from_user.last_name == 'None':
        last_name = '\b'

    chat_log = str('ID: ' + str(message.from_user.id) + '    Name: ' + str(message.from_user.first_name) + '   Username: ' + str(message.from_user.username) + '   Last Name: ' + str(message.from_user.last_name) + '     Says: ' + str(message.text) )
    return chat_log

#"message" object: {'content_type': 'text', 'id': 1801, 'message_id': 1801, 'from_user': {'id': 825074126, 'is_bot': False, 'first_name': 'lobo', 'username': None, 'last_name': None, 'language_code': 'es', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1608224269, 'chat': {'id': 825074126, 'type': 'private', 'title': None, 'username': None, 'first_name': 'lobo', 'last_name': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': '/start', 'entities': [<telebot.types.MessageEntity object at 0x03D64370>], 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'json': {'message_id': 1801, 'from': {'id': 825074126, 'is_bot': False, 'first_name': 'lobo', 'language_code': 'es'}, 'chat': {'id': 825074126, 'first_name': 'lobo', 'type': 'private'}, 'date': 1608224269, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}

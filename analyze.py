import re

user_one_name = ''
user_two_name = ''

user_one_count = 0
user_two_count = 0




def updatecount(name, count):
    global user_one_name, user_two_name, user_one_count, user_two_count

    if user_one_name == user_two_name == '' or user_one_name == '':
        user_one_name = name
        print(f'INFO: Sender 1 name set to \'{user_one_name}\'')
    elif user_two_name == '':
        user_two_name = name
        print(f'INFO: Sender 2 name set to \'{user_two_name}\'')
    else:
        if name == user_one_name:
            user_one_count += count
        elif name == user_two_name:
            user_two_count += count
        else:
            print(f'ERR: SKIP: Sender name \'{name}\' is not one of the two already-read names.')





word_to_find = input('Please enter a phrase to search for: ')
print()

with open('chat.txt', 'r', encoding='utf-8') as chatfile:
    date_pattern = re.compile('\d\d?/\d\d?/\d\d,')
    word_pattern = re.compile(f'{word_to_find}(?![A-z])')
    current_user_name = ''

    for line in chatfile:
        count = 0
        segments = line.split(' ', 4)

        # Check if it's a message or just a new line within a message
        if not date_pattern.fullmatch(segments[0]):
            if current_user_name == '': # If we haven't gotten to a name yet, ignore the line as it's not a message
                continue
            
            # Otherwise add the count to the last name we looked at
            for segment in segments:
                count += segment.count(word_to_find)
            updatecount(current_user_name, count)
            continue

        # Strip the new line from the message for easier printing to the console
        segments[4] = segments[4][:-1]

        # Split the message into a name and a message
        message = segments[4].split(': ', 1)

        # Check if it's an actual message or just an encryption update
        if len(message) < 2:
            print(f'INFO: SKIP: Non-chat message. MESSAGE: \'{message[0]}\'')
            continue
        
        # Update for future reference
        current_user_name = message[0]

        # print(message)
        count = len(re.findall(word_pattern, message[1].lower()))
        
        updatecount(message[0], count)

print('-' * 30, '\n')

print(f'{word_to_find} occured {user_one_count + user_two_count} times in the chat file.')
print(f'{user_one_name} used it {user_one_count} times.')
print(f'{user_two_name} used it {user_two_count} times.')
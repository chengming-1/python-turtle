
# Function to cleanup language.  It replaces bad words with less bad words.

def cleanup(message):
    words = [
        ('damn', 'darn'),
        ('hell', 'hades'),
        ('shit', 'poop')
    ]
    for (word, replacement) in words:
        message = message.replace(word, replacement)
    print(message)
    return message
    

# Test cases
message='damn this shit to hell'
def test_cleanup():
    pass
cleanup(message)

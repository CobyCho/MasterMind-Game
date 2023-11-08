import urllib.request

def spell_check(word):
    return parse_text(get_response(word))

def parse_text(response):
    return response == 'true'

def get_response(word):
    url = f'http://agilec.cs.uh.edu/spell?check={word}'
    
    return urllib.request.urlopen(url).read().decode('utf-8')

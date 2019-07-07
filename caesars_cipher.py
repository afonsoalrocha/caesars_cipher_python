def caesars_cipher():
    import requests
    import hashlib
    import json

    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=ba9c3a40a70664e44aebf97c426159152f93d62a')
    
    challenge = response.json()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    shift = int(challenge['numero_casas'])

    for char in challenge['cifrado']:
        
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index - shift) % 26
            char = alphabet[new_index]

        decrypted += char

    decrypted_sha1 = hashlib.sha1(decrypted.encode('utf-8')).hexdigest()#encoding needed to create sha1 key

    challenge['decifrado'] = decrypted
    challenge['resumo_criptografico'] = decrypted_sha1

    challenge_json = json.dumps(challenge)

    answer_file = open('answer.json', 'w')
    answer_file.write(challenge_json)
    answer_file.close()
    
    files = {'answer': ('answer.json', open('answer.json', 'rb'))}

    response = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=ba9c3a40a70664e44aebf97c426159152f93d62a', files=files)
    
    print(response.text)
    



if __name__=='__main__':
    caesars_cipher()
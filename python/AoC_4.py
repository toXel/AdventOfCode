from hashlib import md5

inp = 'ckczppom'

for i in range(10000000):
    text = inp + str(i)
    m = md5()
    m.update(text.encode('utf-8'))

    if m.hexdigest().startswith('000000'):
        print(i)
        break

me = {'name': "Deji", 'age': 23}
if 'color' not in me:
    me.setdefault('color', 'yellow')
print(me.keys())
print(me.values())
me['color'] = 'white'
print(me.values())
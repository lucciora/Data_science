a=dict(amy=12, bob=14, seth=13)
print(a)
b=dict(zip(['amy', 'bob', 'seth'], [12,14,13]))
print(b)
user_age = [('bob', 13),
            ('cindy', 11),
            ('sadra', 13),
            ('sam', 15),
            ('kevin', 10)]
user_age_dict = {name : age for name, age in user_age}
print(user_age_dict.items())
user_age_dict_upper = {name.upper() : age for name, age in user_age_dict.items() if age >  11}
print(user_age_dict_upper)
print(user_age_dict_upper.__getitem__('BOB'))
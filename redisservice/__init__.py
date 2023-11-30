import redis

# Podkluchenie k redis
redis_db = redis.from_url('redis://localhost')
# create zapis in datadase
redis_db.set('spam', 27)

data = redis_db.get('spam')
print(data)

# redis_db.set('name', 'ahat', 5)
data2 = redis_db.get('name')
print(data2)

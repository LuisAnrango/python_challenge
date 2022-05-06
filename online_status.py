statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(dicts):
    return len([rec for rec in dicts.values() if rec == 'online'])
print(online_count(statuses))

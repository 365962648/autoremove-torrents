import json

SUM = 10

f = open('data.json')
l = json.load(f)

# remove-big-seeds
print('remove-big-seeds')
rem = []
l.sort(key=lambda x: x['size'], reverse=True)
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
    else:
        break
for x in rem:
    print(x)

# remove-small-seeds
print('remove-small-seeds')
rem = []
l.sort(key=lambda x: x['size'])
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
for x in rem:
    print(x)

# remove-new-seeds
print('remove-new-seeds')
rem = []
l.sort(key=lambda x: x['added_on'], reverse=True)
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
for x in rem:
    print(x)

# remove-old-seeds
print('remove-old-seeds')
rem = []
l.sort(key=lambda x: x['added_on'])
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
for x in rem:
    print(x)

# remove-inactive-seeds
print('remove-inactive-seeds')
rem = []
l.sort(key=lambda x: x['last_activity'])
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
for x in rem:
    print(x)

# remove-active-seeds
print('remove-active-seeds')
rem = []
l.sort(key=lambda x: x['last_activity'], reverse=True)
su = 0
for torrent in l:
    if su < SUM*(1<<30):
        su += torrent['size']
        rem.append(torrent['name'])
for x in rem:
    print(x)

# http POST localhost:8000/api/projects/project-example-1/mapitems <<< '{'\
# '  "name": "caca",'\
# '  "type": "point",'\
# '  "data": {'\
# '    "icon": "other",'\
# '    "position": [38.0450, 4.1693]'\
# '  }'\
# '}'


http PUT localhost:8000/api/projects/project-example-1/mapitems/00b3130d-6103-49d5-84da-6347a616de6c <<< '{'\
'  "name": "caca",'\
'  "description": "cacota",'\
'  "type": "point",'\
'  "data": {'\
'    "icon": "other",'\
'    "position": [38.0450, 4.1693]'\
'  }'\
'}'


# http DELETE localhost:8000/api/projects/project-example-1/mapitems/1d1486e4-4a6b-4222-91fb-4bf63e71b194

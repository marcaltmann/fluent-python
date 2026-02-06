"""
Tuples as records.
Tuples are unnamed, fields are determined not by name,
but by position.
Works really well, but not if values are referenced by indexing:
passport[1]
Instead, tuple unpacking is used, e.g.:
_, id = passport
"""

traveler_ids = [('USA', '31195855'), ('GER', '3CFK8JHDL')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)

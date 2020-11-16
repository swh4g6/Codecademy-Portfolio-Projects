#!/usr/bin/env python
# coding: utf-8

# First section of code is provided lists for practice with loops, lists and dictionaries.

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 
         'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 
         'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October',
          'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988,
         1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160,
                       175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
                  ['The Bahamas', 'Northeastern United States'], 
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
                  ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
                  ['Bermuda', 'New England', 'Atlantic Canada'], 
                  ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], 
                  ['Central America'], 
                  ['The Caribbean', 'Mexico', 'Texas'], 
                  ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
                  ['Mexico'], 
                  ['The Caribbean', 'United States East coast'], 
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
                  ['Bahamas', 'United States Gulf Coast'], 
                  ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], 
                  ['The Caribbean', 'Central America'], 
                  ['Nicaragua', 'Honduras'], 
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', 
           '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', 
           '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', 
           '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,
          45,133,603,138,3057,74]


# My code starts here.

# write your update damages function here:
def update_damages(damages):
    # dictionary to handle the conversion from m to million and b to billion
    conversion = {'M': 1000000, 'B': 1000000000}
    # empty list for storing return
    updated_lst = []
    # iterate through each amount in damages list
    for amount in damages:
        # if the last letter is a B or M, convert to appropriate float and append to the new list
        if amount[-1] == 'B' or amount[-1] == 'M':
            updated_lst.append(float(amount[:-1])*conversion[amount[-1]])
        # if it has no recorded damages, just append the string to the list
        else:
            updated_lst.append(amount)      
    return updated_lst
# test the function on the damages list and print result
damages_update = update_damages(damages)
# print(damages_update)

# write your construct hurricane dictionary function here:
def construct_hurricane_dict(name, month, year, max_wind, area, damage, death):
    # empty dictionary for return
    hurricane_dict = {}
    # iterate through each index in the range of the length of name (key)
    for i in range(len(name)):
        # populate new dictionary using name[i] as key and the index to reference each value
        hurricane_dict[name[i]] = {'Name': name[i], 
                                   'Month': month[i], 
                                   'Year': year[i], 
                                   'Max Sustained Wind': max_wind[i], 
                                   'Areas Affected': area[i],
                                   'Damage': damage[i], 
                                   'Deaths': death[i]}
    return hurricane_dict
# Use function on all of the data to form a dictionary of dictionaries. Test by printing result. 
hurricanes = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_update, deaths)
#print(hurricanes)


# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year(hurricanes):
    # empty dictionary to store result
    by_year = {}
    # iterate through each outer key in nested hurricanes dictionary
    for name in hurricanes:
        # store the year value by accessing the value of the inner dictionary key
        this_year = hurricanes[name]['Year']
        # store the current dictionary
        this_hurricane = hurricanes[name]
        # Check if the year is already in the new dictionary as a key. If not add it as new key:value pair.
        if this_year not in by_year:
            by_year[this_year] = this_hurricane
        # If the year is already represented, add the current dictionary as a second dictionary in the value list 
        else:
            by_year[this_year][-1] = this_hurricane
    return by_year
# Use function to create new nested dictionary. Print 1932 to test the else clause functions correctly.
hurricanes_by_year = construct_hurricane_by_year(hurricanes)
#print(hurricanes_by_year[1932])

# write your count affected areas function here:
def count_num_area_affected(hurricanes):
    # empty dictionary to store result
    area_affected_count = {}
    # iterate through each hurricane
    for name in hurricanes:
        # store list of areas affected for this hurricane
        this_hurricanes_areas = hurricanes[name]['Areas Affected']
        # iterate through the areas list        
        for i in range(len(this_hurricanes_areas)):
            # if area is not in the new dictionary, add it with count 1
            if this_hurricanes_areas[i] not in area_affected_count:
                area_affected_count[this_hurricanes_areas[i]] = 1
            # if it already exists, add 1 to the existing count
            else:
                area_affected_count[this_hurricanes_areas[i]] += 1
    return area_affected_count
# Use function on hurricane dictionary. Test by printing result.
area_count = count_num_area_affected(hurricanes)
#print(area_count)


# write your find most affected area function here:
def find_most_affected_area(area_count_dict):
    # two variables for most affected area and the count
    max_area = ''
    max_count = 0
    # iterate through dictionary key:value pairs
    for area, count in area_count_dict.items():
        # update variables if count is a new max
        if count > max_count:
            max_area = area
            max_count = count
    # print message with information        
    return print('The most affected area is {area}, which was hit {count} times.'.format(area=max_area, count=max_count))
# Test output with area:count dictionary
find_most_affected_area(area_count)


# write your greatest number of deaths function here:
def find_deadliest(hurricanes):
    # create variables for hurricane and number of deaths
    deadliest = ''
    max_deaths = 0
    # iterate through hurricanes
    for name in hurricanes:
        # if the value for deaths is a new max, update variables
        if hurricanes[name]['Deaths'] > max_deaths:
            deadliest = name
            max_deaths = hurricanes[name]['Deaths']
    # print a message with the information        
    return print('The deadliest hurricane was {name} with {count} deaths.'.format(name=deadliest, count=max_deaths))
# test output on hurricanes dictionary
find_deadliest(hurricanes)


# write your catgeorize by mortality function here:
def construct_by_mortality(hurricanes):
    # dictionary with keys for mortality rating, but empty list values to store results
    mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    # iterate through hurricanes
    for name in hurricanes:
        # compare each death count and add to appropriate rating based on scale
        if hurricanes[name]['Deaths'] == 0:
            mortality_dict[0].append(hurricanes[name])      
        elif hurricanes[name]['Deaths'] <= 100:
            mortality_dict[1].append(hurricanes[name])
        elif hurricanes[name]['Deaths'] <= 500:
            mortality_dict[2].append(hurricanes[name])
        elif hurricanes[name]['Deaths'] <= 1000:
            mortality_dict[3].append(hurricanes[name])
        elif hurricanes[name]['Deaths'] <= 10000:
            mortality_dict[4].append(hurricanes[name])
        else:
            mortality_dict[5].append(hurricanes[name])
    return mortality_dict
# Use function on hurricanes dictionary. Print to test.
hurricanes_by_mortality = construct_by_mortality(hurricanes)
#print(hurricanes_by_mortality)


# write your greatest damage function here:
def find_costliest(hurricanes):
    # create variables for hurricane and damage cost
    costliest = ''
    max_cost = 0
    # iterate through hurricanes
    for name in hurricanes:
        # if the damage is not recorded, do nothing
        if hurricanes[name]['Damage'] == 'Damages not recorded':
            continue
        # elif the value for cost is a new max, update variables
        elif hurricanes[name]['Damage'] > max_cost:
            costliest = name
            max_cost = hurricanes[name]['Damage']
    # print a message with the information        
    return print('The most expensive hurricane was {name} with ${damage} in damages.'.format(name=costliest, damage=max_cost))
find_costliest(hurricanes)


# write your catgeorize by damage function here:
def construct_by_damage(hurricanes):
    # create a shell dictionary of keys with empty lists. unknown will be for 'Damage not recorded' hurricanes
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 'Unknown': []}
    # iterate through hurricanes
    for name in hurricanes:
        if hurricanes[name]['Damage'] == 'Damages not recorded':
            damage_dict['Unknown'].append(hurricanes[name])
        # compare each death count and add to appropriate rating based on scale
        elif hurricanes[name]['Damage'] == 0:
            damage_dict[0].append(hurricanes[name])      
        elif hurricanes[name]['Damage'] <= 100000000:
            damage_dict[1].append(hurricanes[name])
        elif hurricanes[name]['Damage'] <= 1000000000:
            damage_dict[2].append(hurricanes[name])
        elif hurricanes[name]['Damage'] <= 10000000000:
            damage_dict[3].append(hurricanes[name])
        elif hurricanes[name]['Damage'] <= 50000000000:
            damage_dict[4].append(hurricanes[name])
        else:
            damage_dict[5].append(hurricanes[name])
    return damage_dict
# Use function on hurricanes. Print result to test.
hurricanes_by_damage = construct_by_damage(hurricanes)
#print(hurricanes_by_damage)


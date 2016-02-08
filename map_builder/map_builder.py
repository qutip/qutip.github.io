# This file is part of QuTiP: Quantum Toolbox in Python.
#
#    Copyright (c) 2011 and later, Paul D. Nation, Robert J. Johansson,
#    Alex Pitchford, and Chris Granade.
#
#    All rights reserved.
#
#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are
#    met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of the QuTiP: Quantum Toolbox in Python nor the names
#       of its contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#    PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#    HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################
import csv
import pycountry as pc
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

"""
Builds the QuTiP users maps from Google Analytics data
in csv format. Requires pycountry to get ISO alpha-3 codes.
"""

# Google analytics does not use offical country names.
# Replace names of several countries to offical ones.
replace_countries={
    'Bolivia' : 'Bolivia, Plurinational State of',
    'Bosnia & Herzegovina': 'Bosnia and Herzegovina',
    "Côte d’Ivoire" : "Côte d'Ivoire",
    'Iran' : 'Iran, Islamic Republic of',
    'Kosovo' : 'Serbia',
    'Macau': 'Macao',
    'Macedonia (FYROM)' : 'Macedonia, Republic of',
    'Moldova' : 'Moldova, Republic of',
    'Myanmar (Burma)': 'Myanmar',
    'Russia' : 'Russian Federation',
    'South Korea': 'Korea, Republic of',
    'Syria' : 'Syrian Arab Republic',
    'Taiwan' : 'Taiwan, Province of China',
    'Tanzania' : 'Tanzania, United Republic of',
    'Trinidad & Tobago' : 'Trinidad and Tobago',
    'Vietnam' : 'Viet Nam',
    'Venezuela': 'Venezuela, Bolivarian Republic of'  
    }

header_string = """
//basic map config with custom fills, mercator projection
var map = new Datamap({
	scope: 'world',
	element: document.getElementById('container1'),
	projection: 'mercator',
	geographyConfig: {
		highlightBorderColor: '#666666',
		popupTemplate: function(geography, data) {
			if (data != null) return "<div class='hoverinfo'>" + geography.properties.name+': '+data.visitors +'</div>'
	},
	highlightBorderWidth: 1
	},
"""

footer_string="""
})
"""

max_users = 0
total_users = 0
countries = {}
with open('2015.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        name = row[0]
        if name in replace_countries.keys():
            name = replace_countries[name]
        country = pc.countries.get(name=name)
        country_users = int(row[1].replace(',', ''))
        countries[country.alpha3] = country_users
        total_users += country_users
        max_users = max(max_users,country_users)

print(total_users)

# Pick colormap and normalize. Colors too light if vmin=0.
cmap = cm.Blues
norm = mpl.colors.Normalize(vmin=-int(0.33*max_users), vmax=max_users)
map_color = cm.ScalarMappable(norm=norm, cmap=cmap)


# build_fills
fills = ["fills: { \n","defaultFill: '#CCCCCC', \n"]
for item in countries:
    rgb_color = map_color.to_rgba(countries[item])[:3]
    fills += [item+": '" + str(colors.rgb2hex(rgb_color))+"',"+"\n"]
fills += ["},"]


# build_data
data = ["data: { \n"]
for item in countries:
    item_str = item+": "+"{fillKey: '"+item+"', visitors: "+str(countries[item])+""", country: " """+pc.countries.get(alpha3=item).name+""" " },"""+"\n"
    data += [item_str]
data += ["}"]


# Generate map.js file
out_file = open('map.js', "w")
out_file.writelines(header_string)
for line in fills:
    out_file.writelines(line)
for line in data:
    out_file.writelines(line)
out_file.writelines(footer_string)
out_file.close()
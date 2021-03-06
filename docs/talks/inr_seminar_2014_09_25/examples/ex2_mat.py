from pirs.mcnp import Material
# Copyright 2015 Karlsruhe Institute of Technology (KIT)
#
# This file is part of PIRS-2.
#
# PIRS-2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PIRS-2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# water 
h = Material('H')
o = Material('O')

w = 2*h + o
print w.report()

w.thermal = 'lwtr'
w.T = 450
w.sdict[8018] = 8016
print w.card(comments=False)

# Zircaloy
s = Material( ('Zr', 98.23, 1),
              ('Sn', 1.50,  1),
              ('Fe', 0.12,  1))

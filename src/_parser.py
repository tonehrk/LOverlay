#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  _parser.py
#  
#  Copyright 2020 Tony San Agustin <hormone@live.com.mx>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os 
import sys

#H_PATH=os.environ['HOME']+"/.config/MangoHud/"

class parser ( ):
	
		
	def __init__(self):
		super().__init__()

		
	def get(data, key):
		no_key_true = "fps", "frame_timing", "cpu_stats", "gpu_stats", "vsync"
		
		if  data.find(key) == -1:
			
			for i in range (len(no_key_true)):
				if no_key_true[i] == key: return "1"
				
			return "0"
			
		key = "\n"+key
		a=data.find(key)
		if  a > 0:

			while data[a+len(key):a+len(key)+1] != "\n" and data[a+len(key):a+len(key)+1] != "=":
				
				
				b=a+1
				a =  data[a+1:].find(key)
				if a == -1: break 
				a=a+b
				
		
		if data[a+len(key):a+len(key)+1] == "\n": 	return "1"
		if data [a+len(key):a+len(key)+1] == "=":  
			a = data[a+len(key)+1:a+len(key)+data[a+len(key):].find("\n")]
			return a
		else: 
			
			#if key == "\nram": return "0"
			return "1"
	

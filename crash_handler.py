"""
If you contribute to this file, you may add your git/github username to the copyright statement. See example in CONTRIBUTING.md

Copyright 2022 Tinkering-Townsperson

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License Version 3 as published by the Free Software Foundation; 

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""

# Imports start
from datetime import datetime as dt
import sys, re
import webbrowser as web
# Imports end

# Handler start 
class Handler():
	errorURL = None # Sets URL/URI to open if error is encountered.
	log = None # Logfile
	p = re.compile(r"<class '([a-zA-Z0-9.]*)'>")
	
	def handle(self, exc_type, exc_value, exc_traceback):
		if issubclass(exc_type, KeyboardInterrupt): # Checks if error is KeyboardInterrupt. If it is, ignore it, it's harmless. If not, continue with program.
			sys.__excepthook__(exc_type, exc_value, exc_traceback)
			return
		
		l = self.log
		l.write(f"ERROR\u007b\nCurrent time: {dt.now().strftime('%b-%d-%Y %H:%M:%S')}\nError type: {self.p.findall(str(exc_type))[0]}\nError value: {exc_value}\n\u007d\n\n")
		print(exc_value)
		web.open(f"{self.errorURL}?error={self.p.findall(str(exc_type))[0]}") # Opens help URL/URI.
	
	def __init__(self, log, url="http://127.0.0.1/"):
		self.log = log
		self.errorURL = url
		sys.excepthook = self.handle
# Handler end

if __name__ == "__main__":
	logfile = open("_temp.log", "wt")
	Handler(logfile)
	raise RuntimeError("Test")

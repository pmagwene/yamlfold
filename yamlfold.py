#!/usr/bin/env python
import yaml
import sys
import argparse

def yamlfold(ystr, sep=' | '):
	if type(ystr) == file:
		ystr = ystr.read()
		
	docs = ystr.split('---')
	s = ''
	for d in docs:
		if not len(d): continue
		f = d.strip()
		s += f.replace('\n', sep) + "\n"
	return s

		
if __name__ =='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = argparse.FileType('r'), default = '-')
	args = parser.parse_args()
	print yamlfold(args.input)
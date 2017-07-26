#!/usr/bin/python
import os,sys

inpert = open(sys.argv[1],'r')
buffer = inpert.readlines()
inpert.close()

scale = float(sys.argv[2])


qi = 0.0
qf = 0.0
for line in buffer:
   if line.find("initial_type") > -1:
       elems = line.split()
       itype = elems[1]
   if line.find("final_type") > -1:
       line2="                final_type      %s" % itype
       print line2.rstrip()
       continue
   if line.find("initial_LJ") > -1:
       elems= line.split()
       isig = float(elems[1])   
       ieps = float(elems[2])
   if line.find("final_LJ") > -1:
       line2="                final_LJ        %6.5f  %6.5f " % (isig,ieps)
       print line2.rstrip()
       continue
   if line.find("initial_charge") > -1:
       elems = line.split()
       qi = float( elems[1] )
   if line.find("final_charge") > -1:
       qf = qi * scale
       line2="		final_charge   %-6.5f" % qf
       print line2.rstrip()   
       continue
   print line.rstrip() 

#!/bin/bash

#ok, so here is my second script. my first one did the foward dns lookup, this one will do the reverse dns lookup.
#my method is pretty simple, i ran my first script and directed it to an output file called 'foward-dns-raw-output.txt'
#then i got only the ips from that file using the command:
#cat foward-dns-raw-output.txt | xargs n1 | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
#and redirected it to a file called 'ips.txt'. now i have a list of ips that i can run this simple for loop script on
#for a reverse dns lookup. yay. magic! :D

for line in $( cat ips.txt ): 
do 
    host $line
done

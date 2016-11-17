#!/bin/bash
#my very sloppy/lazy script to do a forward DNS lookup. :]
#oh, btw, i may or may not have lowercased "PayPal.com" and "Naver.com" in the og domains.tsv to make my life easier.
#because those were the only two that were uppercase, and it made no sense, so i fixed it.

for i in $( cat domains.tsv | xargs -n1 | grep '[.]' | grep -v [[:upper:]] )
do
   host $i 
done

#!/usr/bin/env sh

## Storing large data sets in memory is bad so output sorted file.
#sortedCSV="$(uuidgen)".csv
#sort -t, -d -k2 -o "$sortedCSV" res/one-duplicate.csv
#
#serialNumbersOfDuplicateIds=[]
#
#previousSerialNumber=''
#previousClientId=''
#while read -r line; do
#    if [[ $line == 'Serial Number,Client ID' ]]; then
#        continue
#    fi
#
#    serialNumber=${line%%,*}
#    clientId=${line##*,}
#
#    if [[ "$previousClientId" == "$clientId" ]]; then
#        serialNumbersOfDuplicateIds+="($serialNumber)"
#    fi
#
#    previousSerialNumber=
#    previousClientId="$clientId"
#done < "$sortedCSV"
#
## TODO: Output serialNumbersOfDuplicateIds to file.
#
#rm "$sortedCSV"

echo "(0000 0000 0000 0003, 0000 0000 0000 0001)"

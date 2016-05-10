#!/bin/bash
# use option -g without arguments to drop only geomongo db

FLAG_DROP_ALL_DB=true

while getopts ":g" opt ;
do
    case $opt in
        g) FLAG_DROP_ALL_DB=false;
             ;;
        *) echo "the option is incorrect";
             exit 1
             ;;
    esac
done

echo "$FLAG_DROP_ALL_DB"
mongo geomongo --eval "db.dropDatabase()"

if $FLAG_DROP_ALL_DB
then
    mongo testservice --eval "db.dropDatabase()"
    mongo master_db_template --eval "db.dropDatabase()"
fi

# !/bin/bash

MONGOPATH=/root/mongodb

nowtime=`date +%Y%m%d%H%M%S`

if [ ! -d "$MONGOPATH/worldship-h5" ]; then
  mkdir $MONGOPATH/worldship-h5
fi

$MONGOPATH/bin/mongodump -o $MONGOPATH/worldship-h5/$nowtime

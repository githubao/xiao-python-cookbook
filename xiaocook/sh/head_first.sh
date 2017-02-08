#!/usr/bin/env bash



if false; then

c=$1
if [ $c -lt 5 ]; then
echo 'lt 5'
elif [ $c -gt 10 ];then
echo 'gt 10'
else
echo '5-10'
fi

score=59
if ((score<60)) ; then
echo 'you failed'
else
echo 'you passed'
fi

sum2=$[$1+$2]
echo "sum2: $sum2"

a=1
b=2
sum=$[$a+$b]
echo "sum: $sum"

d=`date`
echo "now is $d"

fi
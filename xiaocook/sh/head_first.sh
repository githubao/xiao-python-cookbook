#!/usr/bin/env bash

#12 特殊变量
echo $0
echo "cmd cnt: $#"
echo "cmd str: $*"
echo "cmd list: $@"
for item in $@; do
echo $item
done
echo "cmd id: $$"
echo "cmd retcode: $?"

if false; then
#11 字符串测试
if [ -z $1 ];then
echo 'empty str'
else
echo 'not empty'
fi

#s10 函数
function sub(){
    res=$[$1-$2];
    echo $res
}
sub $1 $2

#s9 死循环 用于监控程序
while true;do
echo 'loop'
done

#s8 循环结构
a=5
while [ $a -ge 1 ]; do
echo $a
a=$[$a-1]
done

for i in `seq 1 5`;do
echo $i
done

#s7 多重选择结构
command=$1
shift 1
case $command in
start)
echo 'start';
;;
stop)
echo 'stop';
;;
restart)
echo 'restart';
;;
*)
echo 'help';
;;
esac

#s6 测试目录和文件
if [ -e head_first.sh ] ; then
echo 'head_first.sh exists'
fi
if [ -d /d/mnt ] ; then
echo '/d/mnt exists'
fi

#s5 多重比较结构
c=$1
if [ $c -lt 5 ]; then
echo 'lt 5'
elif [ $c -gt 10 ];then
echo 'gt 10'
else
echo '5-10'
fi

#s4 比较结构
score=59
if ((score<60)) ; then
echo 'you failed'
else
echo 'you passed'
fi

#s3 读取命令行参数
sum2=$[$1+$2]
echo "sum2: $sum2"

#s2 使用变量
a=1
b=2
sum=$[$a+$b]
echo "sum: $sum"

#s1 运行命令
d=`date`
echo "now is $d"

fi
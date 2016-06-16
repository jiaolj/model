python pack.py
pid=`ps -ef|grep "modelv1"|grep -v "grep"|awk '{print $2}'`
if [ "$pid" = "" ] ; then
  echo "no tomcat pid alive"
else
  echo "kill pid $pid now"
  kill -9 $pid
fi
nohup uwsgi --ini modelv1.ini &

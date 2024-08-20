# changes thevrequest limit to 1000
exec { '/usr/bin/env/sed -i s/15/1000/ /etc/default/nginx': }
-> exev { '/usr/bin/env service/nginx/restart': }

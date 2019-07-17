#!/bin/bash

cd /app/HATP/order/test_suite
if [ $1 = 'ORDER' ]
then
   sleep 300
   i=0
   while (( 1 ))
   do
       i=$[$i+1]
       res_md=`curl -I -m 10 -o /dev/null -s -w %{http_code}"\n" "http://dohko.promotion-api.shopcenter.hualala.com/health"`
       res_wm=`curl -I -m 10 -o /dev/null -s -w %{http_code}"\n" "http://dohko.promotion.shopapi.hualala.com/health"`
       if [ $res_md -eq 200 -a $res_wm -eq 200 ]
       then
               break
       elif [ $i -gt 30 ]
       then
               echo "build failure"
               break
       fi
       sleep 2
    done
    {
        python /app/HATP/order/test_suite/test_suite_order.py $2
    }||{
        cat /root/Mail/mailHeaderOrder.txt > /root/Mail/mailContent.txt
        cat /root/Mail/mailContentError.txt >> /root/Mail/mailContent.txt
        cat /root/Mail/mailContent.txt | sendmail -t
        exit 0
    }
else
   echo There is no running file now, Please edit!
   exit 0
fi

{
    mv /app/HATP/order/report/*.html /app/HATP_REPORT/
}||{
    cat /root/Mail/mailHeaderOrder.txt > /root/Mail/mailContent.txt
    cat /root/Mail/mailContentError.txt >> /root/Mail/mailContent.txt
    cat /root/Mail/mailContent.txt | sendmail -t
    exit 0
}
echo http://172.16.32.39/`ls /app/HATP_REPORT | grep order| sort -r | head -n 1`
#mutt yundian@hualala.com -s "HATP REPORTER" -a  /app/HATP/order/report/`ls /app/HATP/report/ | grep html | sort -r | head -n 1` < /root/Mail/mailContent.txt
cat /root/Mail/mailHeaderOrder.txt > /root/Mail/mailContent.txt
head -n 2 /root/Mail/mailContentTemplate.txt >> /root/Mail/mailContent.txt
echo http://172.16.32.39/`ls /app/HATP_REPORT | grep order| sort -r | head -n 1` >> /root/Mail/mailContent.txt
cat /app/HATP_REPORT/`ls /app/HATP_REPORT | grep order | sort -r | head -n 1` | sed -n "198p" | awk -F ">" '{print $4}' |  awk -F "<" '{print $1}' >> /root/Mail/mailContent.txt
cat /root/Mail/mailContentTemplate.txt | sed -n "2,+5p" >> /root/Mail/mailContent.txt
cat /root/Mail/mailContent.txt | sendmail -t
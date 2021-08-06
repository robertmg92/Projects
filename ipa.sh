#! /bin/bash
echo "Your IP Address is:"
echo $(ifconfig |grep broadcast |awk '{print $2}')
echo "Your Subnet Mask is:"
echo $(ifconfig |grep broadcast |awk '{print $5}')


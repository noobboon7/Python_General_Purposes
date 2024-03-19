#!/bin/bash

if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Everything ok"

else

	echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi

#  Added a check to see if the PATH environment variable is not empty.
# if test -n "$PATH"; then echo "Your path is not empty"; fi

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi
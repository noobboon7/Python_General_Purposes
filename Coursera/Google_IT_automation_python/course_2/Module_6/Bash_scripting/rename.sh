#!/bin/bash

for file in *.HTM; do
        name=$(basename "$file" .HTM)
      # you can use echo  to see what it's doing before actually running
        echo mv "$file" "$name.html" 
done 

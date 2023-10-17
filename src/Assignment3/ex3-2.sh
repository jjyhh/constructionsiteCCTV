#!/bin/bash

case "$2" in
   +)
      expr $1 + $3;;
   -)
      expr $1 - $3;;
   *)
      echo "TRY AGAIN";;
esac

exit 0
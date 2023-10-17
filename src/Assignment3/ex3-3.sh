#!/bin/bash
bmi=$(( 100000 * $1 / $2 / $2))
if [ $bmi -gt 230 ]; then
  echo "과체중입니다."
elif [ $bmi -ge 185 ]; then
  echo "정상체중입니다."
else
  echo "저체중입니다."
fi
exit 0

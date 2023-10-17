#!/bin/bash

# 명령줄 인자로 받은 숫자를 count 변수에 저장
count="$1"

# 입력된 숫자만큼 "Hello, World!"를 출력
i=1
while [ $i -le $count ]
do
  echo "Hello, World!"
  i=$((i + 1))
done

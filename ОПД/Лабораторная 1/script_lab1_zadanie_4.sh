#=================Задание 4================================
echo '4.1'	
wc -l oddish7/herdier oddish7/venonat > tmp/record 2>&/dev/null

echo '4.2'
ls -lR | sort -t ' ' -k 6 -r | head -n 3 2>/tmp/errors

echo '4.3'
cat s* */s* */*/s* | sort | cat -n 2>&/dev/null

echo '4.4'
ls -lR | grep -v '^total$' | grep -v '^$' | grep -v '^\.\/' | sort -r -k 2 | tail -n 2 | awk '{print $2, $9}' 2>/tmp/errors

echo '4.5'
ls -lR | sort -t ' ' -k 6 -r | grep "ka" | head -n 3 2>&1

echo '4.6'
ls -R oddish7 | grep . | sort 2>&/dev/null
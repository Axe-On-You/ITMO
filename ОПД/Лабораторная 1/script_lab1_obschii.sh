#=================Задание 1================================
mkdir lab0
cd lab0

touch kakuna6
touch trubbish3
touch wingull0

mkdir -p houndour4/lampent
touch houndour4/glameow
touch houndour4/palpitoad
touch houndour4/amoongus

mkdir -p nidoranF6/ivysaur
mkdir nidoranF6/braviary
mkdir nidoranF6/woobat
mkdir nidoranF6/mienshao
touch nidoranF6/swampert

mkdir -p oddish7/snover
mkdir oddish7/machoke
touch oddish7/kadabra
touch oddish7/herdier
touch oddish7/venonat
touch oddish7/garbodor

echo -e 'Тип диеты  Carnivore' > houndour4/glameow
echo -e 'Живет  Freshwater\nMarsh' > houndour4/palpitoad
echo -e 'Ходы  After You Foul Play Gastro Acid Giga Drain Seed\nBomb Sleep Talk Snore Synthesis Worry Seed' > houndour4/amoongus
echo -e 'Тип диеты\nNullivore' > kakuna6
echo -e 'Возможности  Overland=7 Surface=7 Underwater=7\nBurrow7=0 Jump=2 Power=4 Intelligence=4 Fountain=0\nGilled=0' > nidoranF6/swampert
echo -e 'Тип покемона  PSYCHIC NONE' > oddish7/kadabra
echo -e 'Способности\nOdor Sleuth Bite Helping Hand Take Down Work Up Crunch Roar Retaliate\nReversal Last Resort Giga Impact' > oddish7/herdier
echo -e 'satk=4 sdef=6\nspd=5' > oddish7/venonat
echo -e 'weight=236.6 height=75.0 atk=10\ndef=8' > oddish7/garbodor
echo -e 'satk=4 sdef=6 spd=7' > trubbish3
echo -e 'Возможности  Overland=4\nSurface=8 Underwater=5 Sky=6 Jump=2 Power=1 Intelligence=3' > wingull0

#=================Задание 2================================
chmod 330 houndour4
chmod 573 houndour4/lampent
chmod 440 houndour4/glameow
chmod 664 houndour4/palpitoad
chmod 004 houndour4/amoongus
chmod 006 kakuna6
chmod 777 nidoranF6
chmod 777 nidoranF6/ivysaur
chmod 711 nidoranF6/braviary
chmod 664 nidoranF6/swampert
chmod 777 nidoranF6/woobat
chmod 752 nidoranF6/mienshao
chmod 753 oddish7
chmod 700 oddish7/snover
chmod 044 oddish7/kadabra
chmod 044 oddish7/herdier
chmod 006 oddish7/venonat
chmod 046 oddish7/garbodor
chmod 312 oddish7/machoke
chmod 664 trubbish3
chmod 004 wingull0

#=================Добавление прав для user=================
chmod 773 houndour4/lampent
chmod 706 kakuna6
chmod 706 oddish7/venonat
chmod 704 wingull0

#=================Задание 3================================
ln -s wingull0 oddish7/venonatwingull
cat oddish7/venonat houndour4/palpitoad > kakuna6_53
cp -R nidoranF6 houndour4/lampent
ln wingull0 houndour4/amoongusswingull	
ln -s oddish7 Copy_46
cat kakuna6 > oddish7/herdierkakuna
cp wingull0 nidoranF6/woobat

#=================Возвращение прав для user================
chmod 573 houndour4/lampent
chmod 006 kakuna6
chmod 006 oddish7/venonat
chmod 004 wingull0

#=================Задание 4================================
echo '4.1'	
wc -l oddish7/herdier oddish7/venonat > /tmp/record 2> /dev/null

echo '4.2'
ls -lR 2> /tmp/4_err | grep '^-' | sort -k7 -r | head -n 3

echo '4.3'
cat s* */s* */*/s* 2> /dev/null | sort | cat –n

echo '4.4'
ls -lR 2> /tmp/errors | grep -v '^total$' | grep -v '^$' | grep -v '^\.\/' | sort -r -k 2 | tail -n 2 | awk '{print $2, $9}'

echo '4.5'
ls -lR 2>&1 | grep '^-' | grep "ka" | sort -k7 -r | head -n 3

echo '4.6'
ls -R oddish7 2> /dev/null | grep . | sort
#=================Задание 5================================
chmod 777 houndour4
chmod 777 houndour4/glameow
chmod 777 houndour4/amoongusswingull
rm wingull0
rm houndour4/glameow
rm Copy_*
rm houndour4/amoongusswingu*
#Чтобы показать удаление braviary добавим опцию -i для rm
rm -ri nidoranF6
rm -ri nidoranF6/braviary
#Окончательно удаляем директорию nidoranF6
rm -r nidoranF6
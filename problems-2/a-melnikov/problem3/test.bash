#!/bin/bash

mkdir -p resources

dirnames=(resources/protected_dir resources/read_only_dir resources/exec_only_dir resources/regular_dir)

for dirname in ${dirnames[@]}
do
  mkdir -p $dirname
  touch $dirname/regular_empty_file.txt
  echo "small file" > $dirname/small_file.txt
  echo "the file of a middle size" > $dirname/middle_file.txt
  echo "the big file, the largest out of existing" > $dirname/big_file.txt
  install -m 000 /dev/null $dirname/protected_file.txt
  install -m 444 /dev/null $dirname/read_only_file.txt
  install -m 222 /dev/null $dirname/write_only_file.txt
  install -m 111 /dev/null $dirname/exec_only_file.txt

  nonexistant_file_name=$dirname/nonexistant_file.txt
  touch $nonexistant_file_name
  ln -s $nonexistant_file_name $dirname/symlink.txt
  rm $nonexistant_file_name
done

chmod 000 ${dirnames[0]}
chmod 444 ${dirnames[1]}
chmod 111 ${dirnames[2]}
chmod 777 ${dirnames[3]}

python test.py

for dirname in ${dirnames[@]}
do
  chmod 777 $dirname
  rm -rf $dirname
done

unset dirnames

#!/bin/bash
if [ $# -ne 3 ]
then echo "given less than 3 args">&2
exit 1
fi

path="$1"
search_str="$2"
replace_str="$3"

# path="${path#src/}" в случае если скрипт вызывается из папки src

if [ ! -f "$path" ]
then echo "invalid file path" >&2
exit 1
fi

if [ ! -w "$path" ]
then echo "No rights for editing file" >&2
exit 1
fi

if [ -z "$search_str" ]
then echo "empty str" >&2
exit 1
fi

if ! grep -q "$search_str" "$path"
then echo "there is no search str in file" >&2
exit 1
fi

sed -i "" "s/$search_str/$replace_str/g" $path
timestamp=$(date +"%Y-%m-%d %H:%M:%S")
hash=$(shasum -a 256 $path | awk '{print $1}')
file_size=$(stat -f%z "$path")
echo "${path} - ${file_size} - ${timestamp} - ${hash} - sha256" >> src/files.log


if grep -q "$search_str" "$path"
then
echo "replacing wasnt done"
else
echo echo "replacing is done"
fi

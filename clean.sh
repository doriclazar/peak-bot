#!/bin/bash
dir_list=( \
	"__pycache__ \
	antenna/__pycache__ \
	body/__pycache__ \
	brain/__pycache__ \
	brain/fs_memory/__pycache__ \
	brain/db_memory/data_types/__pycache__ \
	brain/db_memory/__pycache__ \
	brain/processing/__pycache__ \
	tongue/__pycache__ \
	ears/__pycache__")
for dir_path in $dir_list
do
	if [ -d $dir_path ]; then
		for file in $(ls $dir_path)
		do
			rm $dir_path/$file
			echo "Removed $dir_path/$file"
		done
		rmdir $dir_path
		echo "Removed $dir_path"
	fi
done
file_list=( \
	"sqlite_database.db \
	brain/fs_memory/*.wav")
for file_path in $file_list
do
	if [ -f $file_path ]; then
		rm $file_path
		echo "Removed $file_path"
	fi
done
echo "Project is clean."

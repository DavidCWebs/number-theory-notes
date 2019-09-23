#!/bin/bash

for f in *.md;
do
	[[ "$f" == "README.md" ]] && continue;
	[[ -f $f ]] && echo -e $f >> manifest.txt;
done
jq -R -s 'split("\n")' < manifest.txt | jq '.[:-1]' > .vuepress/manifest.json


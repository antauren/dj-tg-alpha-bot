#!/bin/bash
#
# Update all requirements in files requirements/*.txt to freshest version
# Output new requirement to the same files
#
cd requirements &&  \
for i in `find ./*.txt`; do
    echo '== Updating file: ' $i  && \
    cat $i  | grep -v '^\-e' | cut -d = -f 1 | xargs pip install --upgrade && \
    pip freeze -r $i | awk '/^## /{exit}{print}' > $i.new && \
    mv $i.new $i;
done  && \
cd -
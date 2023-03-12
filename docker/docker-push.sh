#!/bin/bash

LATEST=""
VERSION_NUM=""
ID=""
HELP=""

while getopts "ln:i:h" arg; do
	case $arg in
		l) LATEST=1;;
		n) VERSION_NUM=$OPTARG;;
		i) ID=$OPTARG;;
		h) HELP=1
	esac
done

if [[ $HELP ]]; then
	echo "Print help info"
	exit 0
fi

if [[ ! $ID ]]; then
	echo "An image ID is required"
	echo "example: bash docker-push.sh -i e88"
	exit 1
fi

USERNAME="noesterle"
REPO_NAME="pterodactyl_exporter"

if [[ $VERSION_NUM ]]; then
	echo "docker tag $ID $USERNAME"/"$REPO_NAME:$VERSION_NUM"
	echo "docker push $USERNAME"/"$REPO_NAME:$VERSION_NUM"
fi

if [[ $LATEST ]]; then
	echo "docker tag $ID $USERNAME"/"$REPO_NAME:latest"
	echo "docker push $USERNAME"/"$REPO_NAME:latest"
fi


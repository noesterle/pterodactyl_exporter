if [[ $# -ne 2 ]]; then
	echo "Requires two arguement, the id of the image to push and the version number of the software"
	echo "example: bash docker-push.sh e88 1.0"
	exit 1
fi

USERNAME="noesterle"
REPO_NAME="pterodactyl_exporter"
docker tag $1 $USERNAME"/"$REPO_NAME:latest
docker tag $1 $USERNAME"/"$REPO_NAME:$2

docker push $USERNAME"/"$REPO_NAME:latest
docker push $USERNAME"/"$REPO_NAME:$2

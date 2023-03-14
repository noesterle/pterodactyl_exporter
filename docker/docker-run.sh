echo $2
if [[ $# -ne 1 ]]; then
	echo "Requires one arguement, the tag or id of the image to run"
	echo "example: bash docker-run.sh e88"
	exit 1
fi

docker run -d -p 9531:9531 --mount type=bind,source=$(pwd)/config.yml,target=/opt/pterodactyl_exporter/config/config.yml -t $1

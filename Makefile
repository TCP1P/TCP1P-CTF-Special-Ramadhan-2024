CMD=python3 .script/cli.py
add-all:
	${CMD} add-all
remove-all:
	${CMD} remove-all
start-all:
	${CMD} start-all
stop-all:
	${CMD} stop-all
rctf-deploy:
	rcds deploy
install-dependency:
	(cd ./.dependency/blockchain/images/ && bash ./build.sh)

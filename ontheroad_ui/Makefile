
build:
	yarn

start_server: export REACT_APP_HOST_IP=127.0.0.1
start_server: export REACT_APP_HOST_PORT=5000
start_server: build
	yarn start

# Docker Section
build_docker:
	docker build --label "label=ontheroad_ui_dev" -t johnstratoudakis/ontheroad_ui:dev -f Dockerfile.dev .

start_docker:
	docker run -p 3000:3000 --rm -it \
           -v ${PWD}:/app -v app/node_modules \
           johnstratoudakis/ontheroad_ui:dev
	#docker run -p 5000:80 --rm -it johnstratoudakis/ontheroad:ui
	#-e CHOKIDAR_USEPOLLING=true \
#Finally, -e CHOKIDAR_USEPOLLING=true enables a polling mechanism via chokidar (which wraps fs.watch, fs.watchFile, and fsevents) so that hot-reloading will work.

stop_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_ui_dev")
stop_docker:
	@echo "CONTAINER_ID=${CONTAINER_ID}"
	docker stop ${CONTAINER_ID}

debug_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_ui_dev")
debug_docker:
	docker exec -it ${CONTAINER_ID} /bin/sh

clean_docker:
	docker rm $$(docker ps -qa) || true
	docker rmi $$(docker images -qa) || true

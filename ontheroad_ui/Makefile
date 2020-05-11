
build_docker:
	docker build --label "label=ontheroad_ui" -t johnstratoudakis/ontheroad:ui .

start_docker:
	docker run -p 5000:80 --rm -it johnstratoudakis/ontheroad:ui

stop_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_ui")
stop_docker:
	@echo "CONTAINER_ID=${CONTAINER_ID}"
	docker stop ${CONTAINER_ID}
PYTHON=python3.8

clean:
	rm -rf venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || ${PYTHON} -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

start_server: venv
	. venv/bin/activate; FLASK_ENV=development ${PYTHON} main.py

get_local_version:
	curl http://127.0.0.1:5000/version

get_prod_version:
	curl https://app.johnstratoudakis.com/OnTheRoad/version

# Docker Section
build_docker:
	docker build --label "label=ontheroad_flask_dev" -t johnstratoudakis/ontheroad_flask:dev .

start_docker:
	docker run -p 5000:80 --rm -it johnstratoudakis/ontheroad_flask:dev 

stop_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_flask_dev")
stop_docker:
	@echo "CONTAINER_ID=${CONTAINER_ID}"
	docker stop ${CONTAINER_ID}

debug_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_flask_dev")
debug_docker:
	@echo "CONTAINER_ID=${CONTAINER_ID}"
	docker exec -it ${CONTAINER_ID} /bin/sh

clean_docker:
	docker rm $$(docker ps -qa) || true
	docker rmi $$(docker images -qa) || true

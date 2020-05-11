
clean:
	rm -rf venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3.7 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

start_server: venv
	. venv/bin/activate; FLASK_ENV=development python3.7 main.py

get_local_version:
	curl http://127.0.0.1:5000/version

get_prod_version:
	curl https://app.johnstratoudakis.com/OnTheRoad/version

build_docker:
	docker build --label "label=ontheroad_dev" -t johnstratoudakis/ontheroad:dev .

start_docker:
	docker run -p 5000:80 --rm -it johnstratoudakis/ontheroad:dev 

stop_docker: export CONTAINER_ID=$$(docker ps -qa --filter "label=label=ontheroad_dev")
stop_docker:
	@echo "CONTAINER_ID=${CONTAINER_ID}"
	docker stop ${CONTAINER_ID}
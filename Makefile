run:
	@echo 'Start server'
	docker-compose run --rm web-app sh -c "python manage.py runserver"

migrate:
	docker-compose run --rm web-app sh -c "python manage.py migrate" #2

migrations:
	docker-compose run --rm web-app sh -c "python manage.py makemigrations" #1

su:
	docker-compose run --rm web-app sh -c "python manage.py createsuperuser"

newapp:
	docker-compose run --rm web-app sh -c "python manage.py startapp $(app)"

shell:
	docker-compose run --rm web-app sh -c "python manage.py shell"

run_file:
	@sh script_in_file.sh
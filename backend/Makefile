.PHONY: devup devdown

devup:
	docker rm -f green_card_postgres

	docker run -d                                   \
		--name green_card_postgres                  \
		-e POSTGRES_DB=green_card                   \
		-e POSTGRES_PASSWORD=postgres               \
		-e TZ='Asia/Tashkent'		                \
		-p 5432:5432                                \
		-v green_card_data:/var/lib/postgresql/data \
		postgres:15.1

devdown:
	docker rm -f green_card_postgres

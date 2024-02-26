FROM mysql:8.0.32

ENV MYSQL_ROOT_PASSWORD password
COPY src/database/01_create_table.sql /docker-entrypoint-initdb.d/data.sql01
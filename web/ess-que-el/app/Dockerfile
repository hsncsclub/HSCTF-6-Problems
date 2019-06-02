FROM php:7.2-apache
RUN docker-php-ext-install mysqli
COPY src/ /var/www/
COPY src/public/ /var/www/html/

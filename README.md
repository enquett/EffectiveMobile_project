## Список используемных технологий

Балансировщик нагрузки - [nginx](https://nginx.org/ru/).
HTTP-сервер написан на Python с использованием [FastApi](https://fastapi.tiangolo.com/).
Контейнеризация - [docker](https://www.docker.com/).

## Схема взаимодействия

Nginx доступен на хосте на 80 порту. При попытке отправить get-запрос на 80 порт хоста, балансировщик перенаправит запрос на backend-приложение, которое вернет запрашиваемую информацию. 

## Установка и проверка работоспособности
***Клонирование репозитория***

```git clone https://github.com/enquett/EffectiveMobile_project.git```

***Установка docker***

Установка docker и docker compose описана в официальной документации - <https://docs.docker.com/manuals/>.
В текущем описана установка Docker на Ubuntu 24.04 с использованием документации:
Add Docker's official GPG key:
```
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add the repository to Apt sources:
```
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
```

```sudo apt update```

***Install the Docker packages***:

```sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin```

Install docker-compose:

```sudo apt-get install docker-compose-plugin```


***Переход в директорию project***

```cd project```

***Сборка контейнеров***

```docker compose up -d```

***Проверка работоспособности***

```curl http://127.0.0.1```

# Restaurant Menu

[![codecov](https://codecov.io/gh/Tomraydev/restaurant-menu/branch/master/graph/badge.svg?token=IC4IKSUABV)](https://codecov.io/gh/Tomraydev/restaurant-menu)

Dane incjalizujące są dodawane automatycznie przy starcie z pliku '0002_create_data.py'.  
Superuser jest tworzony automatycznie przy starcie.  
- username: admin  
- password: start1234  



## Quickstart
### Uruchomienie aplikacji
```bash
source .env/dev.env
docker compose up -d
```

Dostępne URL:
- API RESTowe - http://localhost:8001/api
- Dokumentacja API - http://localhost:8001/swagger
- Panel admina - http://localhost:8001/admin

###  Testowanie:  
Wyniki testów automatycznych są dostępne po kliknięciu w ikonę 'codecov' na górze tej strony.  
Aby uruchomić testy samemu, należy uruchomić aplikację zgodnie z instrukcją, a następnie w osobnym terminalu wykonać polecenia:
```bash
source .env/dev.env
cd restaurant-menu
python manage.py test
```

Testowanie maili  
Daty dodawania/modyfikacji dań i kart menu są ustawiane automatycznie dzięki użyciu parametrów 'auto_now', 'auto_now_add'.
Aby przetestować manualnie wysyłanie maili z przepisami zmodyfikowanymi wczoraj (zbiór będzie pusty, bo utworzyliśmy przepisy dzisiaj), można np. zmienić sprawdzany dzień na dzisiejszy poprzez modyfikację 'timedelta(1)' na 'timedelta(0)' w pliku 'restaurant-menu/api/tasks.py'.

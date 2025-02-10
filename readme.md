https://api.frankfurter.dev/v1/latest
from django.core.cache import cache

##### Docker (dev)
```bash
docker-compose up --build -d
docker exec -it test1-web-1 /bin/bash    
python manage.py migrate --no-input
```

http://localhost:8001/api/main/currencies/ - Чтобы получить данные о волюте
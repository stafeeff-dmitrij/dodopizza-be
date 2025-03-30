MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # ограничение доступа по ip
    'config.middleware.access.filter_ip.FilterIPMiddleware',

    # проверка кол-ва запросов к БД
    # 'silk.middleware.SilkyMiddleware',
    # 'config.middleware.count_bd_request.CheckCountDbRequestMiddleware',
]

# -*- coding: utf-8 -*-

SESSION_ENGINE = 'redis_sessions.session'

CHAT_REDIS_SESSIONS_STORAGE = 'poslednee_slovo:sessions'

#Для того, чтобы сгенерировать ключ, можете воспользоваться такой вот несложной строчкой
#  в консоли (на вас оттуда, кстати, смайлик смотрит):

#< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;

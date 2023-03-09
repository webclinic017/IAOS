# -*- coding: utf-8 -*-
__author__ = 'carl'

import logging

from db.myredis.redis_cli import RedisClient
from quotation.cache.cache import LocalBasicDataCache
from util.obj_util import loads_data

# ----  log ------ #
log = logging.getLogger("log_blueprint")
log_err = logging.getLogger("log_err")


# ----  log ------ #


def get_industry():
    """
    获取行业信息
    """
    rediscli = __getrediscli()
    res = rediscli.get("industry_set")
    if res is None:
        LocalBasicDataCache.store_smb_industry_map()
        res = rediscli.get("industry_set")
    return loads_data(res)


def __getrediscli():
    return RedisClient().get_redis_cli()
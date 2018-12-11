# -*- coding: utf-8 -*-
u"""
Created on 2018-12-11

@author: cheng.li
"""

import numpy as np
import pandas as pd


def fetch_data(code: str,
               start_date: str,
               end_date: str,
               freq: str) -> pd.Series:

    dates = pd.date_range(start_date, end_date, freq=freq)
    values = np.random.randn(len(dates))
    return pd.Series(data=values,
                     index=dates.date.astype(str))


if __name__ == '__main__':
    print(fetch_data(None, '2017-01-01', '2018-12-11', 'M'))

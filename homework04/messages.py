from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple

from typing import List, Tuple
from api import messages_get_history
from api_models import Message
import config

user_id = 287653812
Dates = List[datetime.date]
Frequencies = List[int]


plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот

    :param messages: список сообщений
    """
    dates = []
    frequencies = []

    for message in messages:
        message.date = datetime.utcfromtimestamp(message.date).strftime("%Y-%m-%d")
        dates.append(message.date)
        frequency = 0
        for object in messages:
            if object.date == message.date:
                frequency += 1
        frequencies.append(frequency)
    return dates, frequencies


def plotly_messages_freq(dates: Dates, freq: Frequencies) -> None:
    """ Построение графика с помощью Plot.ly

    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    x = dates
    y = freq
    data = [go.Scatter(x=x, y=y)]
    py.plot(data)

import datetime as dt
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    friends = get_friends(user_id, "bdate")

    friends = [User(**friend) for friend in friends]
    ages = []

    for friend in friends:
        if friend.bdate is not None:
            data = friend.bdate.split(".")
            if len(data) == 3:
                age = dt.now().year - int(data[2])
                born_month = int(data[1])
                born_day = int(data[0])
                if (dt.now().month < born_month) or (
                        dt.now().month == born_month and dt.now().day < born_day):
                    ages.append(age - 1)
                else:
                    ages.append(age)
    if ages:
        ages.sort()
        if len(ages) % 2 == 1:
            return ages[len(ages) // 2]
        else:
            return (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
    else:
        return None


if __name__ == '__main__':
    predict_age = age_predict(287653812)
    print(predict_age)


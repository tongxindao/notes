import sys
import json
import pandas as pd


def analysis(file, user_id):
    user_id = int(user_id)

    try:
        user_study = pd.read_json(file)
    except ValueError:
        return 0, 0

    df = user_study[user_study["user_id"] == user_id]["minutes"]

    return df.count(), df.sum()


def analysis_json(file, user_id):
    times = 0
    minutes = 0
    user_id = int(user_id)
    
    with open(file) as f:
        for item in json.load(f):
            if item["user_id"] != user_id:
                continue
            times += 1
            minutes += item["minutes"]

        return times, minutes


if __name__ == "__main__":
    times, minutes = analysis_json(sys.argv[1], sys.argv[2])

    print("user_id: {0}\ntimes: {1}\nminutes: {2}".format(sys.argv[2], times, minutes))

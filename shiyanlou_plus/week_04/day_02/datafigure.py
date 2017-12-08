import sys
import pandas as pd
import matplotlib.pyplot as plt


def user_plot(jfile, db_range, style):
  user_study = pd.read_json(jfile)
  db = user_study.groupby("user_id").sum().head(int(db_range))

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)

  ax.set_title("StudyData")
  ax.set_xlabel("User ID")
  ax.set_ylabel("Study Time")
  ax.plot(db.index, db.minutes, style)
  print("x axes data index: {0}\n y axes data minutes: {1}\n style: {2}".format(db.index, db.minutes, style))

  plt.show()


if __name__ == "__main__":
    jfile = sys.argv[1]
    db_range = sys.argv[2]
    style = sys.argv[3]

    user_plot(jfile, db_range, style)

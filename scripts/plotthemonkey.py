import matplotlib.pyplot as plt
import pandas as pd
from seamonkey import FILE_PATH

#####################



df = pd.read_csv(FILE_PATH)
print(df['days'])

plt.plot(df['days'], df['monkeys'], label='monkeys')
plt.xlabel('Days')
plt.ylabel('Sea monkeys')
plt.show()
plt.plot(df['days'], df['eggs'], label='eggs')
plt.show()
plt.plot(df['days'], df['food'], label='food')
plt.show()
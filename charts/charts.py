import matplotlib.pyplot as plt

def crear_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig('bar.png')
  plt.close()

def crear_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels=['a','b','c']
  values=[20,40,80]
  crear_pie_chart(labels,values)
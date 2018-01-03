from matplotlib import pyplot as plt

hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

plt.figure(figsize=(10,8))
plt.plot(exam_scores, hours_reported, linewidth=2)

hours_lower_bound = [i*0.8 for i in hours_reported]
hours_upper_bound = [i*1.2 for i in hours_reported]

plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2) # x, y_lower_bound, y_upper_bound, alpha. This is the shaded error

plt.title('Time spent studying vs final exam scores')
plt.xlabel("Score")
plt.ylabel('Hours studying (self-reported)')

plt.show()
plt.savefig("my_line_graph.png")
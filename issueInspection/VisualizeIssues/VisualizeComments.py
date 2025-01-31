import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from issueInspection.VisualizeIssues.VisualizeHelpFunctions import get_mean_comments, get_comments_to_mean_answertime, \
    mean_responstime_bodylength


def visualizeComments(comments, openIssues, answer_times, body_length):
    sns.set_palette("Set2")

    # Create GridSpec for flexible subplots arrangement
    fig = plt.figure(figsize=(10, 8))
    gs = GridSpec(3, 1, figure=fig)

    # Plot 1: comments vs. closed
    ax1 = fig.add_subplot(gs[0, 0])
    meanComments = get_mean_comments(comments,openIssues)
    ax1.bar([1,0], meanComments, color = ["b","r"])
    ax1.set_xticks([1,0])
    ax1.set_xticklabels(['True', 'False'])
    ax1.set_ylabel('Average Comments')
    ax1.set_xlabel('Open')

    # Plot 2: comments vs average answer time
    ax2 = fig.add_subplot(gs[1, 0])
    comments_answer_time = get_comments_to_mean_answertime(comments,answer_times)
    keys = [key for key in comments_answer_time.keys()]
    values = list(comments_answer_time.values())
    ax2.scatter(keys, values)
    ax2.set_xlabel("Number of comments")
    ax2.set_ylabel("Average Closing time")

    # Plot 3: body length vs comments
    interval =1000
    meanComments = mean_responstime_bodylength(interval, body_length, comments)
    ax3 = fig.add_subplot(gs[2, 0])
    scaled_keys = [key * interval for key in meanComments.keys()]
    values = list(meanComments.values())
    ax3.plot(scaled_keys, values)
    ax3.set_xlabel('Body Length')
    ax3.set_ylabel('Average Number of Comments')

    # Set common title for the entire figure
    fig.suptitle('Distribution Analysis of Issues', fontsize=16)


    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.6)

    # Display the plot
    plt.show()
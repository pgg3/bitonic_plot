
import matplotlib.pyplot as plt
import math
plt.rcParams.update({
    "font.family": "serif",  # use serif/main font for text elements
    "font.serif": "Times New Roman",
    "font.sans-serif": "Times New Roman",
    "font.monospace": "Inconsolata",
    "mathtext.fontset": "custom",
    "mathtext.cal": "txsys",
    "ps.usedistiller": 'xpdf',
    "ps.fonttype" : 42,
    "pdf.fonttype" : 42,
    "axes.labelpad": 0,
    "font.weight": "bold",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.01,
    "axes.unicode_minus": False
})

plot_dict = []
def bitonic_sort_draw(N):
    n_list = list(range(N))
    for k in range(1,int(math.log(N, 2))+1):
        for j in range(k-1, -1, -1):
            for i in range(N):
                temp = i ^ (2 ** j)
                if temp > i:
                    if i & (2 ** k) == 0:
                        plot_dict.append((i, temp, 0))
                    else:
                        plot_dict.append((i, temp, 1))

if __name__ == '__main__':

    new_fig = plt.figure(
        figsize=(16, 16)
    )
    new_ax = new_fig.add_subplot(111)
    # set all spines to invisible
    new_ax.spines['top'].set_color('none')
    new_ax.spines['bottom'].set_color('none')
    new_ax.spines['left'].set_color('none')
    new_ax.spines['right'].set_color('none')
    # set all ticks to invisible
    new_ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

    # NUM_TO_SORT
    N = 16

    # create input-output lines
    for i in range(N):
        new_ax.hlines(
            y=i,
            xmin=0,
            xmax=N**2,
            color='k',
            linewidth=1,
            zorder=-1
        )
        new_ax.text(
            x=N**2+0.2,
            y=i,
            s=str(i),
            color='k',
            verticalalignment='center'
        )
        new_ax.text(
            x=-0.5,
            y=i,
            s=str(i),
            color='k',
            verticalalignment='center'
        )

    # draw bitonic sort comparisons
    bitonic_sort_draw(N)

    i = 0
    line_width = 1
    arrow_width = 0.3
    head_width = 2*line_width
    color = 'darkorange'
    stage_distance = 50
    inner_stage_distance = 20
    move_distance = 2
    for k in range(1, int(math.log(N, 2))+1):
        for j in range(k):
            movement = 0
            for z in range(int(N/2)):
                compare = plot_dict[i]
                regret = 2**(k - j - 1)
                if compare[2] == 0:
                    new_ax.arrow(
                        x=movement*move_distance+stage_distance*k+inner_stage_distance*j,
                        y=compare[0],
                        dx=0,
                        dy=compare[1] - compare[0] - arrow_width,
                        color=color,
                        linewidth=line_width,
                        shape='full',
                        width=arrow_width,
                        head_length=arrow_width,
                        head_width=head_width
                    )
                else:
                    new_ax.arrow(
                        x=movement*move_distance+stage_distance*k+inner_stage_distance*j,
                        y=compare[1],
                        dx=0,
                        dy=compare[0] - compare[1] + arrow_width,
                        color=color,
                        linewidth=line_width,
                        shape='full',
                        width=arrow_width,
                        head_length=arrow_width,
                        head_width=head_width
                    )
                movement += 1
                movement %= regret
                i += 1

    # i = 0
    #
    # for compare in plot_dict:
    #     if compare[2] == 0:
    #         new_ax.arrow(
    #             x=i,
    #             y=compare[0],
    #             dx=0,
    #             dy=compare[1]-compare[0]-arrow_width,
    #             color=color,
    #             linewidth=line_width,
    #             shape='full',
    #             width=arrow_width,
    #             head_length=arrow_width
    #         )
    #     else:
    #         new_ax.arrow(
    #             x=i,
    #             y=compare[1],
    #             dx=0,
    #             dy=compare[0]-compare[1]+arrow_width,
    #             color=color,
    #             linewidth=line_width,
    #             shape='full',
    #             width=arrow_width,
    #             head_length=arrow_width
    #         )
    #     i += 1


    # invert y-axis, x-axis
    new_ax.invert_yaxis()
    # new_ax.invert_xaxis()
    # Show the plot
    plt.savefig('test.pdf')
    plt.show()
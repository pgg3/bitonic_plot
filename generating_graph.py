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
    "ps.fonttype": 42,
    "pdf.fonttype": 42,
    "axes.labelpad": 0,
    "font.weight": "bold",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.01,
    "axes.unicode_minus": False
})

plot_dict = []


def bitonic_sort_draw(N):
    n_list = list(range(N))
    for k in range(1, int(math.log(N, 2)) + 1):
        for j in range(k - 1, -1, -1):
            for i in range(N):
                temp = i ^ (2 ** j)
                if temp > i:
                    if i & (2 ** k) == 0:
                        plot_dict.append((i, temp, 0))
                    else:
                        plot_dict.append((i, temp, 1))


if __name__ == '__main__':
    # NUM_TO_SORT
    N = 1024

    new_fig = plt.figure(
        figsize=(N, N/2)
    )
    new_ax = new_fig.add_subplot(111)
    # set all spines to invisible
    new_ax.spines['top'].set_color('none')
    new_ax.spines['bottom'].set_color('none')
    new_ax.spines['left'].set_color('none')
    new_ax.spines['right'].set_color('none')
    # set all ticks to invisible
    new_ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)


    # draw bitonic sort comparisons
    bitonic_sort_draw(N)

    i = 0
    line_width = 1
    arrow_width = 0.3
    head_width = 2 * line_width
    color = 'darkorange'

    move_distance = 5
    # inner_stage_distance = move_distance * N / 4
    # stage_distance = inner_stage_distance
    inner_stage_distance = move_distance
    stage_distance = move_distance
    base_drift = 10
    stage_move = 0
    point_size = 100
    for k in range(1, int(math.log(N, 2)) + 1):
        inner_stage_move = 0
        for j in range(k):
            movement = 0
            for z in range(int(N / 2)):
                compare = plot_dict[i]
                regret = 2 ** (k - j - 1)
                if compare[2] == 0:
                    new_ax.arrow(
                        x=movement * move_distance + inner_stage_move + stage_move + base_drift,
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
                    new_ax.scatter(
                        x=movement * move_distance + inner_stage_move + stage_move + base_drift,
                        y=compare[0],
                        color=color,
                        marker='o',
                        s=point_size
                    )
                else:
                    new_ax.arrow(
                        x=movement * move_distance + inner_stage_move + stage_move + base_drift,
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
                    new_ax.scatter(
                        x=movement * move_distance + inner_stage_move + stage_move + base_drift,
                        y=compare[1],
                        color=color,
                        marker='o',
                        s=point_size
                    )
                movement += 1
                movement %= regret
                i += 1
                last_point = movement * move_distance + inner_stage_move + stage_move + base_drift
            # inner_stage_move += 2**(k-j-1) * move_distance
            inner_stage_move += 2**(k-j-1) * inner_stage_distance
            # inner_stage_move += N/(2**((k-j))) * move_distance
        stage_move += 2**(k) * stage_distance - 1

    final_line = last_point + 10
    # create input-output lines
    for i in range(N):
        new_ax.hlines(
            y=i,
            xmin=0,
            xmax=final_line,
            color='k',
            linewidth=1,
            zorder=-1
        )
        new_ax.text(
            x=final_line + 0.2,
            y=i,
            s=str(i),
            color='k',
            verticalalignment='center'
        )
        new_ax.text(
            x=-2,
            y=i,
            s=str(i),
            color='k',
            verticalalignment='center'
        )
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
    plt.tight_layout()
    plt.savefig('test.pdf', bbox_inches='tight', pad_inches=0.01)
    # plt.show()

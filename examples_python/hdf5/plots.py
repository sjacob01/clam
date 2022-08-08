import pathlib

from matplotlib import pyplot

import reports


def plot_lfd_vs_depth(
        tree: reports.TreeReport,
        clusters_by_depth: dict[int, list[reports.ClusterReport]],
        show: bool,
        output_dir: pathlib.Path,
):

    figure: pyplot.Figure = pyplot.figure(figsize=(16, 10), dpi=300)
    figure.suptitle(
        f'{tree.data_name}, {tree.metric_name}, ({tree.cardinality}, {tree.dimensionality})'
    )

    depths = list(sorted(clusters_by_depth.keys()))

    ax: pyplot.Axes = pyplot.axes((0.05, 0.1, 0.9, 0.85))
    ax.violinplot(
        dataset=[
            [c.lfd for c in clusters_by_depth[d]]
            for d in depths
        ],
        positions=depths,
    )
    ax.set_xlabel('depth - num_clusters')
    ax.set_ylabel('local fractal dimension')

    ax.set_xticks(
        depths,
        [f'{d}-{len(clusters_by_depth[d])}' for d in depths],
        rotation=90,
    )

    if show:
        pyplot.show()
    else:
        figure.savefig(
            output_dir.joinpath(f'{tree.data_name}__{tree.metric_name}.png'),
            dpi=300,
        )
    pyplot.close(figure)

    return

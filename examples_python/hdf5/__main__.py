import paths
import plots
import reports

# base_path = paths.REPORTS_DIR.joinpath(
#     'ark_1_no_buffer',
# )
# output_base = base_path.joinpath('plots')
# output_base.mkdir(exist_ok=True)

# for path in base_path.iterdir():
#     if not path.name.endswith('json'):
#         continue
#     r: reports.RnnReport = reports.RnnReport.parse_file(path)
#     assert len(r.is_valid()) == 0
#     r.plot(False, output_base)

base_path = paths.REPORTS_DIR.joinpath(
    'trees',
)
output_base = base_path.joinpath('plots')
output_base.mkdir(exist_ok=True)

for path in base_path.iterdir():
    if '__' not in path.name:
        continue

    print(f'reading from {path.name} ...')
    tree: reports.TreeReport = reports.TreeReport.parse_file(path.joinpath('tree.json'))
    clusters = reports.load_tree(path)
    clusters_by_depth = {
        d: [c for c in clusters if len(c.name) == d]
        for d in range(1, tree.max_depth + 1)
    }
    plots.plot_lfd_vs_depth(
        tree,
        clusters_by_depth,
        False,
        output_base,
    )

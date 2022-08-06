import paths
import report

base_path = paths.REPORTS_DIR.joinpath(
    'ark_1_no_buffer',
)
output_base = base_path.joinpath('plots')
output_base.mkdir(exist_ok=True)

for path in base_path.iterdir():
    if not path.name.endswith('json'):
        continue
    r: report.Report = report.Report.parse_file(path)
    assert len(r.is_valid()) == 0
    r.plot(False, output_base)

## Additional Notes

- Requires Python 3.x on the host; no external Python libraries are used.
- The module supports Linux, Windows, and macOS hosts. OS details use `lsb_release` or `/etc/os-release` (Linux), `systeminfo` (Windows), or `sw_vers` (macOS).
- Adjust `python_interpreter` if the Python 3 executable has a different name (e.g., `python`).
- The JSON output is a flattened map with string values to comply with Terraform's `external` data source requirements (e.g., `{"os_name": "Linux", "os_version": "5.15.0", "os_distribution": "Ubuntu 24.04.2 LTS", "python_version": "3.12.3", "java_version": "17.0.2", "nodejs_version": "18.16.0", "docker_version": "24.0.5", "terraform_version": "1.3.0", "git_version": "2.34.1"}`).
- Application versions (e.g., `python_version`, `java_version`) are included only if the application is detected; otherwise, the field is omitted.
- Detection requires the application to be in the system PATH (e.g., `python3`, `java`, `node`, `docker`, `terraform`, `git`).
- Generate documentation with `make docs`, which runs `terraform-docs` with headers and footers from `docs/`.
- CI/CD is handled by GitHub Actions workflows (`.github/workflows/lint.yml` for linting and `.github/workflows/validate.yml` for validation).
- See `examples/simple/README.md` for a basic usage example of the module.
- If unexpected files (e.g., `project.json`) appear, ensure they are excluded in `.gitignore` or manually removed before committing.

## Resources
- [Terraform External Data Source](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external)
- [Terraform Local Provider](https://registry.terraform.io/providers/hashicorp/local/latest/docs)

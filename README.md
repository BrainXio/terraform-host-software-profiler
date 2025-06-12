<!-- BEGIN_TF_DOCS -->
# Host Software Profiler Module Overview

This module collects software specifications from the host machine where Terraform is executed. It uses a Python script with standard library modules to gather details about the operating system (name, version, distribution) and common applications (e.g., Python, Java, Node.js, Docker, Terraform, Git), outputting the results as a JSON object saved to `software_profile.json`.

## Purpose
The module provides a reusable way to profile the software environment for inventory, compliance, or configuration purposes in infrastructure-as-code workflows.

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.3.0 |
| <a name="requirement_external"></a> [external](#requirement\_external) | >= 2.2.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | >= 2.4.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_external"></a> [external](#provider\_external) | >= 2.2.0 |
| <a name="provider_local"></a> [local](#provider\_local) | >= 2.4.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [local_file.software_output](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file) | resource |
| [external_external.software_profile](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_python_interpreter"></a> [python\_interpreter](#input\_python\_interpreter) | Python interpreter to use (e.g., 'python3') | `string` | `"python3"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_profile_file_path"></a> [profile\_file\_path](#output\_profile\_file\_path) | Path to the generated software profile JSON file |
| <a name="output_software_profile"></a> [software\_profile](#output\_software\_profile) | Software profile information as a flattened JSON object with string values, including OS (name, version, distribution) and detected applications (e.g., Python, Java, Node.js, Docker, Terraform, Git) with their versions |

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
<!-- END_TF_DOCS -->
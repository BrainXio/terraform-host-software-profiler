# Example: Basic Usage of brainxio/terraform-host-software-profiler

## Overview
This example demonstrates how to use the `brainxio/terraform-host-software-profiler` Terraform module to profile software platforms and applications on the host machine. The module generates a JSON file (`software_profile.json`) containing details such as OS (name, version, distribution) and detected applications (e.g., Python, Java, Node.js, Docker, Terraform, Git).

## Prerequisites
- Terraform >= 1.3.0
- Python 3.x installed on the host
- Applications to detect (e.g., `python3`, `java`, `node`, `docker`, `terraform`, `git`) must be in the system PATH

## Usage
1. Navigate to the `examples/simple` directory:
   ```bash
   cd examples/simple
   ```
2. Initialize Terraform:
   ```bash
   terraform init
   ```
3. Review the plan:
   ```bash
   terraform plan
   ```
4. Apply the configuration:
   ```bash
   terraform apply
   ```

This will execute the module, run the `software_profile.py` script, and generate `software_profile.json` in the current working directory.

## Example Output
- **File**: `software_profile.json` (e.g., `{"os_name": "Linux", "os_version": "5.15.0", "os_distribution": "Ubuntu 24.04.2 LTS", "python_version": "3.12.3", "java_version": "17.0.2", ...}`)
- **Terraform Outputs**:
  - `software_profile`: The JSON object with software details
  - `profile_file_path`: Path to `software_profile.json`

## Notes
- The `python_interpreter` variable defaults to `python3`. Adjust if your Python executable has a different name (e.g., `python`).
- Application versions are included only if detected; otherwise, fields are omitted.
- This example is a reference for integrating the module into larger Terraform configurations. See the main module's documentation for advanced usage.

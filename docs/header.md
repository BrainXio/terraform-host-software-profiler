# Host Software Profiler Module Overview

This module collects software specifications from the host machine where Terraform is executed. It uses a Python script with standard library modules to gather details about the operating system (name, version, distribution) and common applications (e.g., Python, Java, Node.js, Docker, Terraform, Git), outputting the results as a JSON object saved to `software_profile.json`.

## Purpose
The module provides a reusable way to profile the software environment for inventory, compliance, or configuration purposes in infrastructure-as-code workflows.

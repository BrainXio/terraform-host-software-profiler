terraform {
  required_version = ">= 1.3.0"
}

module "software_profile" {
  source             = "../../"
  python_interpreter = "python3"
}

output "software_profile" {
  value = module.software_profile.software_profile
}

output "profile_file_path" {
  value = module.software_profile.profile_file_path
}

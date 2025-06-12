output "software_profile" {
  description = "Software profile information as a flattened JSON object with string values, including OS (name, version, distribution) and detected applications (e.g., Python, Java, Node.js, Docker, Terraform, Git) with their versions"
  value       = data.external.software_profile.result
}

output "profile_file_path" {
  description = "Path to the generated software profile JSON file"
  value       = local_file.software_output.filename
}

data "external" "software_profile" {
  program = [var.python_interpreter, "${path.module}/files/software_profile.py"]
}

resource "local_file" "software_output" {
  content  = jsonencode(data.external.software_profile.result)
  filename = "${path.cwd}/software_profile.json"
}

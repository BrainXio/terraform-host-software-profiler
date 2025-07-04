terraform {
  required_version = ">= 1.3.0"
  required_providers {
    external = {
      source  = "hashicorp/external"
      version = ">= 2.2.0"
    }
    local = {
      source  = "hashicorp/local"
      version = ">= 2.4.0"
    }
  }
}

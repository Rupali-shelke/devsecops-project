terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

provider "local" {}

resource "local_file" "infra" {
  filename = "infrastructure.txt"
  content = "Environment: ${var.env}"  
}

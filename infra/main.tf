terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

data "external" "env_check" {
  program = ["sh", "-c", "curl -s http://169.254.169.254/latest/meta-data/ | jq -R '{result: .}'"]
}

resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}

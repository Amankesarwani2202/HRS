resource "aws_route53_zone" "my_zone" {
  name = "testing.com" 
}

resource "aws_route53_record" "alb_dns" {
  zone_id = var.alb_zone_id
  name    = "my-alb.testing.com" 
  type    = "A"
  alias {
    name                   = var.alb_dns_name
    zone_id                = aws_lb.my_alb.zone_id
    evaluate_target_health = true
  }
}

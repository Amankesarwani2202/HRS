resource "aws_lb" "my_alb" {
  name               = "my-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [var.ecs_security_group_id]
  subnets            = var.subnet_ids
}

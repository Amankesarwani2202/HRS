module "vpc" {
  source      = "./modules/vpc"
  environment = "development"  
}

module "ecs" {
  source      = "./modules/ecs"
  vpc_id      = module.vpc.vpc_id
  subnet_ids  = module.vpc.public_subnets
}

module "alb" {
  source                 = "./modules/alb"
  subnet_ids             = module.vpc.public_subnets  
  ecs_security_group_id  = "your_ecs_security_group_id"  
  vpc_id      = module.vpc.vpc_id
}

module "route53" {
  source         = "./modules/route53"
  alb_dns_name   = module.alb.alb_dns_name
  alb_zone_id  = module.alb.alb_zone_id 
}



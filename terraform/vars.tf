variable "python_runtime" {
  type    = string
  default = "python3.12"
}

variable "data_ingestion_bucket_prefix" {
  type    = string
  default = "ingested-data"
}

variable "code_ingestion_bucket_prefix" {
  type    = string
  default = "ingestion-code"
}

variable "lambda_name" {
  type    = string
  default = "toy_handler"
}

variable "region_name" {
  type = string
  default = "eu-west-2"
}

variable "default_timeout" {
  type    = number
  default = 5
}
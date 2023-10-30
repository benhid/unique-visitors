variable "resource_group_name" {
  description = "The name of the resource group in which to create the Cosmos DB Account"
  default     = "cosmosdb-postgresql-rg"
}
variable "resource_group_location" {
  description = "The location of the resource group"
  default     = "West Europe"
}
variable "storage_account_name" {
  description = "The name of the storage account to use for storing Terraform state"
  default     = "storage-tfstate-ac"
}
variable "cosmos_db_account_name" {
  description = "The name of the Cosmos DB Account"
  default     = "cosmosdb-postgresql-ac"
}
variable "cosmos_db_location" {
  description = "The name of the Azure region to host replicated data"
  default     = "West Europe"
}
variable "container_app_image" {
  description = "The name of the container image to use for the container app"
  default     = "docker.io/some-app:latest"
}
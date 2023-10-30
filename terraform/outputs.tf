output "cosmosdb_endpoint" {
  description = "The endpoint of the CosmosDB Account"
  value       = azurerm_cosmosdb_account.acc.endpoint
}
output "cosmosdb_primary_master_key" {
  description = "The primary master key of the CosmosDB Account"
  value       = azurerm_cosmosdb_account.acc.primary_key
  sensitive   = true
}
output "container_app_url" {
  description = "The URL of the Container App"
  value       = azurerm_container_app.some-app.latest_revision_fqdn
}
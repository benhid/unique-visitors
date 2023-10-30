resource "azurerm_cosmosdb_account" "acc" {
  name                      = var.cosmos_db_account_name
  location                  = azurerm_resource_group.rg.location
  resource_group_name       = azurerm_resource_group.rg.name
  offer_type                = "Standard"
  kind                      = "GlobalDocumentDB"
  enable_automatic_failover = false
  enable_free_tier          = true
  depends_on                = [
    azurerm_resource_group.rg
  ]
  geo_location {
    location          = var.cosmos_db_location
    failover_priority = 0
  }
  consistency_policy {
    consistency_level = "BoundedStaleness"
  }
}
resource "azurerm_cosmosdb_sql_database" "db" {
  name                = "visitors"
  resource_group_name = azurerm_cosmosdb_account.acc.resource_group_name
  account_name        = azurerm_cosmosdb_account.acc.name
}
resource "azurerm_cosmosdb_sql_container" "coll" {
  name                = "unique_hits"
  resource_group_name = azurerm_cosmosdb_account.acc.resource_group_name
  account_name        = azurerm_cosmosdb_account.acc.name
  database_name       = azurerm_cosmosdb_sql_database.db.name
  partition_key_path  = "/id"
}
resource "azurerm_container_app_environment" "some-app" {
  name                = "some-app"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}
resource "azurerm_container_app" "some-app" {
  name                         = "some-app"
  container_app_environment_id = azurerm_container_app_environment.some-app.id
  resource_group_name          = azurerm_resource_group.rg.name
  revision_mode                = "Single"
  ingress {
    external_enabled = true
    target_port      = 80
  }
  secret {
    name  = "cosmosdb-connection-string"
    value = azurerm_cosmosdb_account.acc.connection_strings[0]
  }
  registry {
    server = "docker.io"
  }
  template {
    container {
      name   = "some-app-container"
      image  = var.container_app_image
      cpu    = 0.25
      memory = "0.5Gi"
      env {
        name        = "DATABASE_URL"
        secret_name = "cosmosdb-connection-string"
      }
    }
  }
}
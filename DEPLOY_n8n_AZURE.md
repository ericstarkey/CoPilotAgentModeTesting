## Alternative: Deploy from Azure Container Registry (ACR)
If Docker Hub is unavailable or rate-limited, you can use Azure Container Registry (ACR) as an alternative image source:

### 1. Create an Azure Container Registry
```bash
az acr create --resource-group n8n-rg --name n8nacr2025es --sku Basic --admin-enabled true --location eastus
```

### 2. Log in to ACR
```bash
az acr login --name n8nacr2025es
```

### 3. Pull the n8n image locally
```bash
docker pull n8nio/n8n:latest
```

### 4. Tag the image for your ACR
```bash
docker tag n8nio/n8n:latest n8nacr2025es.azurecr.io/n8n:latest
```

### 5. Push the image to your ACR
```bash
docker push n8nacr2025es.azurecr.io/n8n:latest
```

### 6. Deploy the container from ACR
```bash
az container create \
  --resource-group n8n-rg \
  --name n8n \
  --image n8nacr2025es.azurecr.io/n8n:latest \
  --ports 5678 \
  --dns-name-label myn8n2025es \
  --environment-variables N8N_BASIC_AUTH_ACTIVE=true N8N_BASIC_AUTH_USER=admin N8N_BASIC_AUTH_PASSWORD=changeme \
  --os-type Linux \
  --cpu 1 \
  --memory 1.5 \
  --registry-login-server n8nacr2025es.azurecr.io \
  --registry-username $(az acr credential show --name n8nacr2025es --query username -o tsv) \
  --registry-password $(az acr credential show --name n8nacr2025es --query passwords[0].value -o tsv)
```

The container will be accessible at `http://myn8n2025es.eastus.azurecontainer.io:5678`.

---
# n8n on Azure Container Instances

This guide will help you deploy n8n (an open-source workflow automation tool) to Azure Container Instances (ACI) and make it accessible via a public URL.

## Steps

1. **Use the official n8n Docker image**
2. **Deploy to Azure Container Instances (ACI)**
3. **Expose the container to the internet**
4. **Access n8n via the public URL provided by Azure**

---

## 1. Prerequisites
- Azure CLI installed and logged in (`az login`)
- An Azure subscription

## 2. Deploy n8n to Azure Container Instances

You can deploy n8n using a single Azure CLI command:

```bash
az group create --name n8n-rg --location eastus
az container create \
  --resource-group n8n-rg \
  --name n8n \
  --image n8nio/n8n \
  --ports 5678 \
  --dns-name-label myn8n2025es \
  --environment-variables N8N_BASIC_AUTH_ACTIVE=true N8N_BASIC_AUTH_USER=admin N8N_BASIC_AUTH_PASSWORD=changeme
```

- Replace `<unique-dns-name>` with a unique name (e.g., `myn8ninstance2025`).
- The container will be accessible at `http://<unique-dns-name>.eastus.azurecontainer.io:5678`.

## 3. Access n8n
- Open the URL in your browser.
- Login with the username `admin` and password `changeme` (change these for production!).

---

## 4. Clean Up
To remove the resources when done:
```bash
az group delete --name n8n-rg --yes --no-wait
```

---

## Next Steps
- Secure with HTTPS (use Azure Application Gateway or a reverse proxy)
- Use Azure Storage for persistent data
- Configure environment variables for production

---

_Update this file as you iterate or add new deployment options._

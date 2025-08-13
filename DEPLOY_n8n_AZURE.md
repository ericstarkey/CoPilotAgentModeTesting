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
  --dns-name-label myn8ninstance2025es \
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

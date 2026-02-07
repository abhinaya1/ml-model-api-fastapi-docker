# Troubleshooting Guide

This document records common issues encountered during local and Docker-based
deployment, along with their resolutions.

---

## 1) `docker: command not found` (macOS)

**Cause**
- Docker Desktop not installed or not running

**Fix**
- Install Docker Desktop for Mac
- Ensure Docker is running
- Restart the terminal

---

## 2) `exec: "uvicorn": executable file not found in $PATH`

**Cause**
- uvicorn installed but not available as a CLI binary

**Fix**
Use module execution in Dockerfile:

```dockerfile
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Rebuild:
```bash
docker build --no-cache -t iris-api .
```

---

## 3) `/usr/local/bin/python: No module named uvicorn`

**Cause**
- uvicorn missing in container environment

**Fix**
Add to requirements.txt:
```txt
uvicorn[standard]
```

Rebuild:
```bash
docker build --no-cache -t iris-api .
```

Verify:
```bash
docker run --rm iris-api python -c "import uvicorn; print(uvicorn.__version__)"
```

---

## 4) curl times out on `/health`

**Cause**
- Host port already in use

**Fix**
Run on a different host port:
```bash
docker run --rm -p 8001:8000 iris-api
```

Access API:
- http://127.0.0.1:8001/docs

---

## Summary

Most deployment issues fall into three categories:
1. Missing dependencies
2. Incorrect Docker build context
3. Host port conflicts

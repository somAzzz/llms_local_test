# Qwen/Qwen3-Coder-Next-FP8 Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-06 23:10:42
- **Model**: Qwen/Qwen3-Coder-Next-FP8
- **API URL**: http://localhost:8000/v1/chat/completions
- **Test Cases**: 10
- **Test Mode**: Complex Comprehensive

## GPU Information

- **Model**: NVIDIA RTX PRO 6000 Blackwell Workstation Edition
- **Memory**: 97887 MB
- **Driver**: 580.126.09
- **Peak Memory (est.)**: N/A

## Test Results Summary

| Metric | Value |
|--------|-------|
| Successful Tests | 10/10 |
| **Avg Generation Speed** | **23.9 tok/s** |
| Total Time | 345.44s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 26.1 tok/s
- **Min**: 6.6 tok/s
- **Median**: 25.8 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 120.56s | 88 | 800 | **6.6** tok/s |
| Microservices Architecture | 23.43s | 95 | 600 | **25.6** tok/s |
| Complex Algorithms | 26.92s | 53 | 700 | **26.0** tok/s |
| Debug Task | 19.36s | 148 | 500 | **25.8** tok/s |
| Data Analysis Report | 23.11s | 107 | 600 | **26.0** tok/s |
| System Design Interview | 23.27s | 86 | 600 | **25.8** tok/s |
| Multi-turn Conversation | 31.35s | 135 | 800 | **25.5** tok/s |
| Technical Documentation | 27.34s | 84 | 700 | **25.6** tok/s |
| Database Optimization | 19.46s | 125 | 500 | **25.7** tok/s |
| ML Project | 30.64s | 133 | 800 | **26.1** tok/s |

## Test Details

### Full Backend System

- **Time**: 120.56s
- **Speed**: 6.6 tok/s
- **TTFT (est.)**: 12.056s

**Response Preview:**
```
Here's a complete, production-ready FastAPI REST API for a blog system with JWT authentication, SQLite database, Pydantic models, pytest tests, and Docker support.

---

## 📁 Project Structure

```
fastapi-blog-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry poi...
```

---

### Microservices Architecture

- **Time**: 23.43s
- **Speed**: 25.6 tok/s
- **TTFT (est.)**: 2.343s

**Response Preview:**
```
Here's a comprehensive, production-grade microservices architecture design for an e-commerce platform, adhering to modern best practices and scalability requirements.

---

## **1. Service Breakdown (Domain-Driven Design)**

Each service is bounded, autonomous, and follows the *Single Responsibility...
```

---

### Complex Algorithms

- **Time**: 26.92s
- **Speed**: 26.0 tok/s
- **TTFT (est.)**: 2.692s

**Response Preview:**
```
# A* and Dijkstra's Algorithms in Python

Below is a comprehensive implementation of both algorithms with detailed comments, visualizations, and test cases.

```python
import heapq
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# =================...
```

---

### Debug Task

- **Time**: 19.36s
- **Speed**: 25.8 tok/s
- **TTFT (est.)**: 1.936s

**Response Preview:**
```
## Bug Analysis

The main issue is in this line:
```python
t.join()  # BUG: This makes it sequential!
```

This is placed **inside the loop** after `t.start()`, which means each thread is started and immediately joined before the next thread starts. This defeats the purpose of concurrency entirely -...
```

---

### Data Analysis Report

- **Time**: 23.11s
- **Speed**: 26.0 tok/s
- **TTFT (est.)**: 2.311s

**Response Preview:**
```
Here's a complete, production-ready Python analysis pipeline for the retail sales dataset, following best practices for data science projects.

```python
# =============================================================================
# RETAIL SALES ANALYSIS PIPELINE
# ===============================...
```

---

### System Design Interview

- **Time**: 23.27s
- **Speed**: 25.8 tok/s
- **TTFT (est.)**: 2.327s

**Response Preview:**
```
Here's a comprehensive design for a scalable, production-grade URL shortening service (e.g., "Bitly-like"), covering all requested aspects with implementation-level details.

---

## 1. RESTful API Endpoints Design

### Core Endpoints
| Method | Endpoint | Description | Request Body | Response |
|--...
```

---

### Multi-turn Conversation

- **Time**: 31.35s
- **Speed**: 25.5 tok/s
- **TTFT (est.)**: 3.135s

**Response Preview:**
```
**Assistant**: Great—let’s dig into the `EXPLAIN` output. Can you share the full `EXPLAIN (ANALYZE, BUFFERS)` for one of those slow `SELECT` queries? That’ll tell us if it’s doing a full table scan, if indexes are being considered, and whether there’s I/O pressure.

---

**User**: Here’s the output ...
```

---

### Technical Documentation

- **Time**: 27.34s
- **Speed**: 25.6 tok/s
- **TTFT (est.)**: 2.734s

**Response Preview:**
```
# 📷 `imgcompressor` – High-Performance Image Compression CLI & Library

A fast, cross-platform Python CLI tool and library for lossy and lossless image compression supporting PNG, JPEG, and WebP formats. Designed for developers, designers, and DevOps engineers who need reliable image optimization in...
```

---

### Database Optimization

- **Time**: 19.46s
- **Speed**: 25.7 tok/s
- **TTFT (est.)**: 1.946s

**Response Preview:**
```
Let's analyze and optimize this query systematically.

---

### **1. Performance Issues**

| Issue | Explanation |
|-------|-------------|
| **Subquery with `IN`** | PostgreSQL may execute the subquery multiple times or materialize a large intermediate result set. With many US customers, the `IN` li...
```

---

### ML Project

- **Time**: 30.64s
- **Speed**: 26.1 tok/s
- **TTFT (est.)**: 3.064s

**Response Preview:**
```
# End-to-End Customer Churn Prediction Pipeline

Below is a complete ML pipeline for customer churn prediction that covers all requirements: EDA, feature engineering, class imbalance handling, model comparison, hyperparameter tuning, evaluation, feature importance, and deployment considerations.

``...
```

---


## Conclusion

**Performance Rating**: Average

- Average Speed: 23.9 tok/s

---
*Generated by benchmark script*

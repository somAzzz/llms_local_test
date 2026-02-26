# Qwen/Qwen3-Coder-Next-FP8 Performance Benchmark Report

## Test Information

- **Test Time**: 2026-02-26 21:53:14
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
| **Avg Generation Speed** | **138.6 tok/s** |
| Total Time | 54.07s |
| Total Tokens | 6600 |

### Speed Statistics

- **Max**: 148.4 tok/s
- **Min**: 53.7 tok/s
- **Median**: 148.1 tok/s

## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
| Full Backend System | 14.89s | 88 | 800 | **53.7** tok/s |
| Microservices Architecture | 4.05s | 95 | 600 | **148.3** tok/s |
| Complex Algorithms | 4.72s | 53 | 700 | **148.4** tok/s |
| Debug Task | 3.39s | 148 | 500 | **147.5** tok/s |
| Data Analysis Report | 4.05s | 107 | 600 | **148.1** tok/s |
| System Design Interview | 4.05s | 86 | 600 | **148.1** tok/s |
| Multi-turn Conversation | 5.39s | 135 | 800 | **148.3** tok/s |
| Technical Documentation | 4.73s | 84 | 700 | **147.9** tok/s |
| Database Optimization | 3.39s | 125 | 500 | **147.4** tok/s |
| ML Project | 5.41s | 133 | 800 | **147.9** tok/s |

## Test Details

### Full Backend System

- **Time**: 14.89s
- **Speed**: 53.7 tok/s
- **TTFT (est.)**: 1.489s

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

- **Time**: 4.05s
- **Speed**: 148.3 tok/s
- **TTFT (est.)**: 0.405s

**Response Preview:**
```
Here's a comprehensive, production-grade microservices architecture design for an e-commerce platform, adhering to modern best practices and scalability requirements.

---

## **1. Service Breakdown (Domain-Driven Design)**

Each service is bounded, autonomous, and follows the **Single Responsibilit...
```

---

### Complex Algorithms

- **Time**: 4.72s
- **Speed**: 148.4 tok/s
- **TTFT (est.)**: 0.472s

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

- **Time**: 3.39s
- **Speed**: 147.5 tok/s
- **TTFT (est.)**: 0.339s

**Response Preview:**
```
## Bug Analysis

The main issue is in this line inside the loop:

```python
t.join()  # BUG: This makes it sequential!
```

This causes the main thread to wait for each thread to complete *before starting the next one*, defeating the purpose of concurrency. The scraper runs sequentially instead of i...
```

---

### Data Analysis Report

- **Time**: 4.05s
- **Speed**: 148.1 tok/s
- **TTFT (est.)**: 0.405s

**Response Preview:**
```
Here's a complete, production-ready Python analysis pipeline for the retail sales dataset. This pipeline uses modern data science best practices and includes modular functions, clear documentation, and scalable design.

---

### 📦 **Assumptions about Dataset Structure**
*(Adjust column names if need...
```

---

### System Design Interview

- **Time**: 4.05s
- **Speed**: 148.1 tok/s
- **TTFT (est.)**: 0.405s

**Response Preview:**
```
Here's a comprehensive design for a scalable, production-grade URL shortening service (e.g., `shrt.co`), covering all requested aspects with concrete implementation details.

---

## **1. RESTful API Endpoints**

### **Core Endpoints**
| Method | Endpoint | Description | Request Body | Response |
|-...
```

---

### Multi-turn Conversation

- **Time**: 5.39s
- **Speed**: 148.3 tok/s
- **TTFT (est.)**: 0.539s

**Response Preview:**
```
**Assistant:** Great—let’s dig into the `EXPLAIN` output. Can you share the full `EXPLAIN (ANALYZE, BUFFERS)` for one of those slow `SELECT` queries? That’ll tell us if the planner is doing a sequential scan, if there’s index bloat, or if the estimates are wildly off (e.g., "rows=1" vs "rows=500,000...
```

---

### Technical Documentation

- **Time**: 4.73s
- **Speed**: 147.9 tok/s
- **TTFT (est.)**: 0.473s

**Response Preview:**
```
# 🖼️ **ImgCompressor CLI**  
*High-performance, batch-capable image compression tool with intelligent quality control and detailed statistics.*

---

## 📚 Table of Contents  
1. [Installation](#installation)  
2. [Quick Start & Usage Examples](#quick-start--usage-examples)  
3. [Configuration Option...
```

---

### Database Optimization

- **Time**: 3.39s
- **Speed**: 147.4 tok/s
- **TTFT (est.)**: 0.339s

**Response Preview:**
```
Let me analyze this query and provide a comprehensive optimization strategy.

## 1. Performance Issues Identified

**Subquery Execution Pattern:**
- The `IN (subquery)` pattern can be inefficient, especially with large result sets from the subquery
- PostgreSQL may execute the subquery multiple time...
```

---

### ML Project

- **Time**: 5.41s
- **Speed**: 147.9 tok/s
- **TTFT (est.)**: 0.541s

**Response Preview:**
```
# End-to-End Customer Churn Prediction Pipeline

Below is a complete ML pipeline for customer churn prediction that covers all requirements: EDA, feature engineering, class imbalance handling, model comparison, hyperparameter tuning, evaluation, feature importance, and deployment considerations.

``...
```

---


## Conclusion

**Performance Rating**: Excellent

- Average Speed: 138.6 tok/s

---
*Generated by benchmark script*
